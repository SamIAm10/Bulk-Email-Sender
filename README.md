# Bulk Email Sender
A simple program that uses a template and sends a customized email (with optional attachments) from a Gmail account to multiple recipients.

I originally created this to reach out to multiple recruiters with my resume and transcript, but have repurposed the code to apply to more general use cases.

## Installation
1. `pip install yagmail`
2. `pip install keyring`

## Usage
First, you must [allow less secure apps](https://myaccount.google.com/lesssecureapps) for your Google account, otherwise this won't work (you can turn this back off when you're done).

Next, edit the variables in "emailer.py" to suit your needs, then run it. For the first run, it will ask you if you want to save your password. Enter "y" if you don't want to provide your password for every run.
