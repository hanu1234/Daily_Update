import imaplib
import email
import re
import os


class GmailHandler:
    def __init__(self):
        self.mail = None
        self.email_sub = None
        self.email_from = None
        self.save_dir = os.path.dirname(__file__) + '/tools/credentials/'

    def gmail_initialization(self, mail_id, password):
        """
        Initialize gmail account object for reading gmail
        :param mail_id:
        :param password: password of the email
        :return:
        """
        # using imap module connect the gmail imap server
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.mail.login(mail_id, password)

        # select the inbox
        self.mail.select('inbox')

        # search all the mail mails in inbox
        typ, data = self.mail.search(None, 'ALL')
        email_ids = data[0]

        return email_ids

    def get_emial_sub_msg_body(self, mail_id, password):
        """
        Get the email subject line and email body content
        :param mail_id:
        :param password:
        :return:
        """
        email_id = self.gmail_initialization(mail_id, password)

        id_list = email_id.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        # Fetch the email with particular id
        typ, data = self.mail.fetch(str(latest_email_id), '(RFC822)')

        msg = None
        for response in data:
            if isinstance(response, tuple):
                msg = email.message_from_string(response[1].decode())
                self.email_sub = msg['subject']
                self.email_from = msg['from']
                print(self.email_sub)
                print(self.email_from)
            try:
                print(msg.get_payload(decode=False))
                for body in msg.get_payload():

                    print("Email Body: ", body.get_payload(decode=True))
                    print("Email Message Content is: ", msg.get_payload())
                    return self.email_sub, body.get_payload(decode=True), data
            except Exception as e:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                return self.email_sub, msg.get_payload(), data

    def get_url_to_set_password_for_new_user(self, mail_id, password):
        """
        Get the url link to set the new user password
        :param mail_id: Valid email id
        :param password: Corresponding email id password
        :return:
        """
        mail_sub, mail_body, _ = self.get_emial_sub_msg_body(mail_id, password)
        if "Welcome to ExtremeCloud IQ" in mail_sub:
            url = re.search("(?P<url>https?://[^\s]+)", mail_body.decode()).group("url")
            return url

    def get_user_approval_url(self, mail_id, password):
        """

        :param mail_id:
        :param password:
        :return:
        """
        mail_sub, mail_body, _ = self.get_emial_sub_msg_body(mail_id, password)
        if "Approve User Credential" in mail_sub:
            url = re.search("(?P<url>https?://[^\s\">]+)", mail_body).group("url")
            rm = re.compile(r'&amp;')
            return re.sub(rm, '&', url)

    def get_login_credential_attachment_from_mail(self, mail_id, password, filename):
        """
        Download credentials from the gmail attachments
        :param mail_id:
        :param password:
        :param filename:
        :return:
        """
        mail_sub, mail_body, data = self.get_emial_sub_msg_body(mail_id, password)
        if "Login Credentials" in mail_sub:
            msg = email.message_from_string(data[0][1].decode())
            for part in msg.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue

                filename = filename
                if filename is not None:
                    sv_path = os.path.join(self.save_dir, filename)
                    print(sv_path)
                    if not os.path.isfile(sv_path):
                        fp = open(sv_path, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close()
                        return 1

    def get_login_credentials(self, mail_id, password):
        """
        Get Single user login credentials sent from xiq
        :param mail_id:
        :param password:
        :return:
        """
        mail_sub, mail_body, data = self.get_emial_sub_msg_body(mail_id, password)
        if "Login Credentials" in mail_sub:
            msg = email.message_from_string(data[0][1].decode())
            for part in msg.walk():
                if part.get_content_maintype() == 'text':
                    clean = re.compile(r'<[^>]+>')  # clean up the html tags
                    m = re.sub(clean, ' ', part.get_payload())
                    line = " ".join(m.split())
                    user_id = re.findall(r'Your ID\W+\w+', line)[0].split()[-1]
                    access_code = re.findall(r'Your Access Key\W+\w+', line)[0].split()[-1]
                    print("User Id:{}   Access_Key:{}".format(user_id, access_code))
                    return access_code, user_id
                if part.get('Content-Disposition') is None:
                    continue
        return None, None


if __name__ == "__main__":
    obj = GmailHandler()
    # obj.get_login_credential_attachment_from_mail("cloud1tenant1@gmail.com", "Symbol@123", "bulk_user.csv")
    url = obj.get_user_approval_url("cloud1tenant1@gmail.com", "Symbol@123")
    print(url)

