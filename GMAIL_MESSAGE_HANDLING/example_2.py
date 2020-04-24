import imaplib
import email
import re


class GmailNotification:
    def __init__(self):
        pass

    def get_gmail_message_subject(self, email_id, password):
        """
        Get the email subject
        :param email_id: (str) valid email id
        :param password:(str)  corresponding email id password
        """
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(email_id, password)
        mail.select('inbox')

        email_type, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        print("First Email ID: ", first_email_id)
        print("Latest Email ID: ", latest_email_id)

        typ, data = mail.fetch(str(latest_email_id), '(RFC822)')

        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1].decode())
                email_subject = msg['subject']
                email_from = msg['from']
                print("Email from: ", email_from)
                print("*INFO* Message Subject is :", email_subject)
                return email_subject
            else:
                return -1

    def get_gmail_message_body(self, email_id, password):
        """
        Get the body of email
        :param email_id:(str) valid email id
        :param password:(str)  corresponding email id password
        """
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(email_id, password)
        mail.select('inbox')

        email_type, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        print("First Email ID: ", first_email_id)
        print("Latest Email ID: ", latest_email_id)

        typ, data = mail.fetch(str(latest_email_id), '(RFC822)')

        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1].decode())
                email_subject = msg['subject']
                email_from = msg['from']
                print("Email from: ", email_from)
                print("Message Subject is:", email_subject)
                try:
                    for body in msg.get_payload():
                        print("Email Body: ", body.get_payload(decode=True))
                        print("Email Message Content is: ", msg.get_payload())
                        return body.get_payload(decode=True)
                except Exception as e:
                    print("Email Message : ",  msg.get_payload(decode=True))
                    print("Email Message Content is:", msg.get_payload())
                    return msg.get_payload()
            else:
                return -1

    def get_url_to_set_password_for_new_user(self, email, password):
        """
        read setup password link  from the gmail message content
        :param email_id:(str) valid email id
        :param password:(str)  corresponding email id password
        """
        msg_sbj = self.get_gmail_message_subject(email, password)
        print("Message Subject is:", msg_sbj)
        if "Welcome to ExtremeCloud IQ" in msg_sbj:
            msg_body = self.get_gmail_message_body(email, password).decode()
            url = re.search("(?P<url>https?://[^\s]+)", msg_body).group("url")
            print("Setup Password URL is:", url )
            return url
        else:
            return -1

    def verify_username_for_new_user(self, email, password):
        """
        read setup password link  from the gmail message content
        :param email_id:(str) valid email id
        :param password:(str)  corresponding email id password
        """
        msg_sbj = self.get_gmail_message_subject(email, password)
        print("Message Subject is:", msg_sbj)
        if "Login Credentials" in msg_sbj:
            msg_body = self.get_gmail_message_body(email, password).decode()
            user = re.search("([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)", msg_body)
            username = user.group(1)
            print("Setup Password URL is:", username )
            return username
        else:
            return -1

object= GmailNotification()
object.verify_username_for_new_user("cloud1tenant1@gmail.com", "Symbol@123")