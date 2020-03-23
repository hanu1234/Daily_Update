import imaplib
import email
import os

svdir = 'C:\\Daily_Update\\GMAIL_MESSAGE_HANDLING\\'

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login("cloud1tenant1@gmail.com", "Symbol@123")

# Select the inbox
mail.select('inbox')

# It will return the list of ids for each email in the account.
email_type, data = mail.search(None, 'ALL')
mail_ids = data[0]

id_list = mail_ids.split()
first_email_id = int(id_list[0])
latest_email_id = int(id_list[-1])

typ, msgs = mail.fetch(str(latest_email_id), '(RFC822)')  # i is the email id
# typ, msgs = mail.search(None, '(SUBJECT "insert subject here")')
msgs = msgs[0][1]

m = email.message_from_string(msgs.decode())
if m.get_content_maintype() != 'multipart':
    pass

for part in m.walk():
    if part.get_content_maintype() == 'multipart':
        continue
    if part.get('Content-Disposition') is None:
        continue

    filename = part.get_filename()
    if filename is not None:
        sv_path = os.path.join(svdir, filename)
        if not os.path.isfile(sv_path):
            fp = open(sv_path, 'wb')
            fp.write(part.get_payload(decode=True))
            fp.close()
