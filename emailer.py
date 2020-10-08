import yagmail

receivers = input("Path to receiver list: ")

body = [
    "test message"
]

filename = "test.csv"

yag = yagmail.SMTP("from@gmail.com")

for r in receivers:
    yag.send(
        to = r,
        subject = "test title",
        contents = body,
        attachments = filename,
    )
