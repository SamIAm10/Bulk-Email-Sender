import yagmail

# enter the Gmail you are sending from
sender_email = "testemail6213@gmail.com"

# enter the names and emails you are sending to
recipients = [
    ('Name1', 'testemail6213@gmail.com', 'Position1')
	('Name2', 'testemail5354@gmail.com', 'Position2')
]

# enter the filepaths of the files you want to attach (must prefix with "r")
files = [
    r'Bulk-Email-Sender\src\test\test_file.txt', 
    r'Bulk-Email-Sender\src\test\test_image.jpg'
]

email = yagmail.SMTP(sender_email)

# edit your email here
for r in recipients:
    email.send(
        to = r[1],
        # edit your title here
        subject = f'Regarding position {r[2]}',
        # edit your message here
        contents = [f'Hello {r[0]},\n\n I am reaching out in regards to the position of {r[2]}. I hope you will consider me.\n\n Sincerely, first_name last_name'],
        attachments = files
    )