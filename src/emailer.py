import yagmail

# enter the Gmail you are sending from
sender_email = "testemail6213@gmail.com"

# enter the emails you are sending to
recipient_emails = [
    "testemail6213@gmail.com",
	"testemail5354@gmail.com"
]

# enter the subject of the email
title = "test title"

# enter the body of the message
body = [
    "test message\n\n"
    "test paragraph"
]

# enter the filepaths of the files you want to attach (must prefix with "r")
files = [
    r"Bulk-Email-Sender\src\test\test_file.txt", 
    r"Bulk-Email-Sender\src\test\test_image.jpg"
]

email = yagmail.SMTP(sender_email)

for r in recipient_emails:
    email.send(
        to = r,
        subject = title,
        contents = body,
        attachments = files
    )