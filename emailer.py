import yagmail

receiver = "to@gmail.com"
body = [
    
]

filename = "test.csv"

yag = yagmail.SMTP("from@gmail.com")
for i in range(5):
    yag.send(
        to = receiver,
        subject = "test title",
        contents = body,
        attachments = filename,
    )
