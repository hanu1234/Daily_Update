from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from bs4 import BeautifulSoup
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
import csv
from apiclient import errors
import re

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


class GmailHandlerApi:
    def __init__(self):
        self.mail = None
        self.email_sub = None
        self.email_from = None
        self.email_msg = None
        self.file = None
        self.save_dir = os.path.dirname(__file__)

    def _get_url_link(self, soup):
        """
        Get the url link from soup object
        :param soup:
        :return: url links
        """
        links = []
        for link in soup.find_all('a'):
            links.append(link.get('href'))
        return links

    def _get_html_table_rows(self, soup):
        """
        Assuming html contains only one table
        Get the rows from html table
        :param soup:
        :return:
        """
        rows = []
        table = soup.find('table')
        if not table:
            print("No table in html")
            return 1
        table_rows = table.find_all('tr')
        for row in table_rows:
            td = row.find_all('td')
            th = row.find_all('th')
            if th:
                row = [i.text.strip() for i in th]
            else:
                row = [i.text.strip() for i in td]
            rows.append(row)
        return rows

    def _get_data_from_csv(self, filename, key='User Name'):
        """
        Get the bulk user credentials stored in csv file
        :param filename: credential dict
        :param key
        :return:
        """
        csv_data = {}
        with open(filename) as f:
            csv_reader = csv.DictReader(f)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                csv_data[row[key]] = row
                line_count += 1
        return csv_data

    def create_gmail_service(self):

        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('gmail', 'v1', credentials=creds)
        return service

    def get_gmail_messages(self, service, subj):
        results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
        messages = results.get('messages', [])
        if not messages:
            print("No messages found.")
            return None
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            for header in msg['payload']["headers"]:
                if header['name'] == 'Subject':
                    if subj in header['value']:
                        print(f"Subject line:{header['value']}")
                        return msg
        return None

    def get_raw_message(self, subj_line):
        services = self.create_gmail_service()
        msg = self.get_gmail_messages(services, subj_line)
        if msg:
            return msg

    def _get_message_html_content_soup(self, raw_message):
        for part in raw_message["payload"]['parts']:
            if part['mimeType'] == 'multipart/related':
                html_content = base64.urlsafe_b64decode(part['parts'][0]['body']['data'].encode('UTF-8'))
                soup = BeautifulSoup(html_content, 'html.parser')
                return soup

    def get_user_attachments(self, raw_message, service):
        for part in raw_message['payload']['parts']:
            print(part)
            if part['filename']:
                if 'data' in part['body']:
                    data = part['body']['data']
                else:
                    att_id = part['body']['attachmentId']
                    att = service.users().messages().attachments().get(userId='me', messageId=raw_message['id'],
                                                                       id=att_id).execute()
                    data = att['data']

                file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))
                self.file = ''.join([self.save_dir, part['filename']])
                print(self.file)
                if not os.path.isfile(self.file):
                    with open(self.file, 'wb') as fp:
                        fp.write(file_data)

    def get_email_reports_url_link(self):
        if raw_msg := self.get_raw_message("report from Extreme Networks"):
            msg_html_content_soup = self._get_message_html_content_soup(raw_msg)
            url_links = self._get_url_link(msg_html_content_soup)
            return url_links[0]

    def get_sender_email_id(self, subj_line):
        services = self.create_gmail_service()
        msg = self.get_gmail_messages(services, subj_line)
        if msg:
            for header in msg['payload']["headers"]:
                if header['name'] == 'From':
                    print(f"From:{header['value']}")
                    return header['value']

    def get_url_to_set_password_for_new_user(self):
        if raw_msg := self.get_raw_message("Welcome to ExtremeCloud IQ"):
            msg_html_content_soup = self._get_message_html_content_soup(raw_msg)
            url_links = self._get_url_link(msg_html_content_soup)
            return url_links[1]

    def get_user_approval_url(self):
        if raw_msg := self.get_raw_message("Approve User Credential"):
            msg_html_content_soup = self._get_message_html_content_soup(raw_msg)
            url_links = self._get_url_link(msg_html_content_soup)
            return url_links[0]

    def get_password_reset_link(self):
        if raw_msg := self.get_raw_message("Password Reset Verification"):
            msg_html_content_soup = self._get_message_html_content_soup(raw_msg)
            url_links = self._get_url_link(msg_html_content_soup)
            return url_links[0]

    def get_login_credential(self):
        if raw_msg := self.get_raw_message("Login Credentials"):
            msg_snippet = raw_msg['snippet']

            try:
                access_key_pattern = re.compile(r"(Your Access Key:\s|Your Password:\s)(?:[\d_]\S+|\S*[%@#$]\S*|\w+)")
                id_pattern = re.compile(r"(Your ID:\s|Your Login:\s)(?:[\d_]\S+|\S*[%@#$]\S*|\w+)")

                access_key = access_key_pattern.search(msg_snippet).group(0).split()[-1]
                login_id = id_pattern.search(msg_snippet).group(0).split()[-1]

                print(f"Your Access key is:{access_key}")
                print(f"Your Login ID is:{login_id}")
                return access_key, login_id

            except Exception as e:
                print(e)

    def get_login_credential_from_attachments(self):
        services = self.create_gmail_service()
        msg = self.get_gmail_messages(services, "Login Credentials")
        if msg:
            self.get_user_attachments(msg, services)
            credentials = self._get_data_from_csv(self.file)
            print(credentials)
            return credentials

    def get_cloud_pin_for_wi_fi_network(self):
        if raw_msg := self.get_raw_message("PIN for Wi-Fi Network"):
            msg_snippet = raw_msg['snippet']
            print(msg_snippet)
            pin_pattern = re.compile(r"(is: )(?:[\d_]\S+|\S*[%@#$]\S*|\w+)")
            pin = pin_pattern.search(msg_snippet).group().split()[-1]
            print(pin)
            return pin

    def get_cloud_cwp_pin_event_report(self):
        services = self.create_gmail_service()
        raw_msg = self.get_gmail_messages(services, "Cloud CWP PIN Events Report")

        data = {}
        if raw_msg:
            raw_html_soup = self._get_message_html_content_soup(raw_msg)
            table_rows = self._get_html_table_rows(raw_html_soup)
            data['Login Time'] = table_rows[1][0]
            data['SSID Name'] = table_rows[1][1]
            data['User Name'] = table_rows[1][2]
            data['Client Mac Address'] = table_rows[1][3]
            print(data)
            self.get_user_attachments(raw_msg, services)
            csv_data = self._get_data_from_csv(self.file, 'Client MAC Address')
            print(csv_data)
            if re.search(r'PIN authentication events between', raw_msg['snippet']):
                pattern = re.compile(r'\d+-\d+-\d+\W\d+:\d+')
                to_from = re.findall(pattern, raw_msg['snippet'])
                data['from'] = to_from[0]
                data['to'] = to_from[1]
            return data, csv_data

    def get_cloud_cwp_no_pin_event_report(self):
        if raw_msg := self.get_raw_message("Cloud CWP PIN Events Report"):
            msg_snippet = raw_msg['snippet']
            if re.search(r'There were no PIN authentication ', msg_snippet):
                pattern = re.compile(r'\d+-\d+-\d+\W\d+:\d+')
                to_from = re.findall(pattern, msg_snippet)
                from_ = to_from[0]
                to = to_from[1]
                return from_, to


if __name__ == "__main__":
    obj = GmailHandlerApi()
    # url_link = obj.get_email_reports_url_link()
    # obj.get_sender_email_id("Welcome to ExtremeCloud IQ!")
    obj.get_cloud_cwp_pin_event_report()

