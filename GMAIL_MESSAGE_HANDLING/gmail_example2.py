import email
import imaplib
from bs4 import BeautifulSoup

username = "cloud3tenant3@gmail.com"
passwd = "Symbol@123"

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, passwd)
print(mail.select('inbox'))

result, dta = mail.uid('search', None, "ALL")
print(dta)

inbox_item_list = dta[0].split()
latest_email = inbox_item_list[0]

result2, email_data = mail.uid('fetch', latest_email, '(RFC822)')

raw_email = email_data[0][1].decode("utf-8")

email_msg = email.message_from_string(raw_email)

# print(dir(email_msg))

print(email_msg['Subject'])
print(email_msg['To'])
print(email_msg['From'])

# print(email_msg.get_payload())

for part in email_msg.walk():
    print("Content Main Type:", part.get_content_maintype())
    print("Filename:", part.get_filename())
    content_type = part.get_content_type()
    print(dir(part))
    print("Content_type:", content_type)
    if 'html' in content_type:
        html_ = part.get_payload()
        print(html_)
        soup = BeautifulSoup(html_, 'html.parser')

        # Getting the table
        table = soup.find('table')
        table_rows = table.find_all('tr')
        for tr in table_rows:
            td = tr.find_all('td')
            row = [i.text.strip() for i in td]
            print(row)
