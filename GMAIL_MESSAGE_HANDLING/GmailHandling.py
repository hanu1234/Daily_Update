import imaplib
import email
import re
import os


class GmailHandling:
    def __init__(self):
        self.mail = None
        self.email_sub = None
        self.email_from = None
        self.save_dir = 'C:\\Daily_Update\\GMAIL_MESSAGE_HANDLING\\'

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
            try:
                for body in msg.get_payload():
                    print("Email Body: ", body.get_payload(decode=True))
                    print("Email Message Content is: ", msg.get_payload())
                    return self.email_sub, body.get_payload(decode=True), data
            except Exception as e:
                print("Exception: ", e)
                print("Email Message : ", msg.get_payload(decode=True))
                print("Email Message Content is:", msg.get_payload())

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

    def get_login_credential_attachment_from_mail(self, mail_id, password):
        """

        :param mail_id:
        :param password:
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

                filename = part.get_filename()
                if filename is not None:
                    sv_path = os.path.join(self.save_dir, filename)
                    if not os.path.isfile(sv_path):
                        fp = open(sv_path, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close()


obj = GmailHandling()
obj.get_login_credential_attachment_from_mail("cloud1tenant1@gmail.com", "Symbol@123")
url = obj.get_url_to_set_password_for_new_user("cloud1tenant1@gmail.com", "Symbol@123")
print(url)