import yagmail

# enter the email you are sending from
sender_email = "testemail6213@gmail.com"

# enter the emails you are sending to
recipient_emails = [
    "testemail6213@gmail.com"
]

# enter the subject of the email
title = "test title"

# enter the body of the message
body = [
    "test message\n\n"
    "test paragraph"
]

# enter the filepaths of the files you want to attach
files = [
    r"Bulk-Email-Sender\src\test\test_file.txt", 
    r"Bulk-Email-Sender\src\test\test_image.jpg"
]

yag = yagmail.SMTP(sender_email)

for r in recipient_emails:
    yag.send(
        to = r,
        subject = title,
        contents = body,
        attachments = files
    )