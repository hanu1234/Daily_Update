import imaplib
import email
import re


class GmailNotification:
    def __init__(self):
        pass

    @staticmethod
    def get_gmail_subject_msg_body(email_id, password):
        """
        Get the email subject
        :param email_id: (str) valid email id
        :param password:(str)  corresponding email id password
        """
        # Using IMAP Module connect the imap server
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(email_id, password)

        # Select the inbox
        mail.select('inbox')

        # It will return the list of ids for each email in the account.
        email_type, data = mail.search(None, 'ALL')  # data = [b'1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]
        mail_ids = data[0]

        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        print("First Email ID: ", first_email_id)
        print("Latest Email ID: ", latest_email_id)

        # Fetch the email with particular id, We’ll fetch the email using RFC822 protocol
        typ, data = mail.fetch(str(latest_email_id), '(RFC822)')  # i is the email id

        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1].decode())

                email_subject = msg['subject']
                email_from = msg['from']

                print("Email from: ", email_from)
                print("Message Subject is :", email_subject)
                return email_subject, msg
            else:
                return -1

    def get_gmail_message_body(self, email, password):
        """
        :param msg: Gmail msg object
        :return:
        """
        email_subject, msg = self.get_gmail_subject_msg_body(email, password)
        try:
            for body in msg.get_payload():
                print("Email Body: ", body.get_payload(decode=True))
                print("Email Message Content is: ", msg.get_payload())
                return email_subject, body.get_payload(decode=True)
        except Exception as e:
            print("Exception: ", e)
            print("Email Message : ", msg.get_payload(decode=True))
            print("Email Message Content is:", msg.get_payload())
            return email_subject, msg.get_payload()

    def get_setup_password_link(self, email, password):
        """
        Get setup password link for xiq
        :param email:
        :param password:
        :return:
        """
        mail_subject, mail_body = self.get_gmail_message_body(email, password)
        if "Welcome to ExtremeCloud IQ" in mail_subject:
            # (?P<url>https?://[^\s]+)  -->?P<url> Named capturing group
            # ? zero or one match
            # [^\s] -->\s any whitespace character , [^\s] match any character other than white space characters
            url = re.search("(?P<url>https?://[^\s]+)", mail_body.decode()).group("url")
            return url


if __name__ == "__main__":
    obj = GmailNotification()
    obj.get_setup_password_link("cloud1tenant1@gmail.com", "Symbol@123")

