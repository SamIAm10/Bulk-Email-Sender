import yagmail

recipient_emails = input("Path to receiver list: ")
sender_email = "testemail6213@gmail.com"

body = [
    "test message"
]

file1 = "test_file.txt"

yag = yagmail.SMTP(sender_email)

for r in recipient_emails:
    yag.send(
        to = r,
        subject = "test title",
        contents = body,
        attachments = file1
    )
