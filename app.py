import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import dotenv
import os

data = pd.read_excel('email_addresses.xlsx')
dotenv.load_dotenv()
password = os.getenv("GMAIL_PASSWORD")
sender = os.getenv("GMAIL_SENDER")
subject = 'TESTTESTTESTTESTTEST'
body = """
hi
        this is a test
        multiline text 3 quotes
        import smtplib library
        .env hides password 
        create .env file and store password etc there 
        use pandas to open excel file
        

Regards
Anna
"""

# Set up the SMTP server
# Change to 'smtp.office365.com' if you have an Outlook account
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)

for index, row in data.iterrows():
    receiver = row['Email']
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

# Attach the text message
    msg.attach(MIMEText(body, 'plain'))
    # Send the email
    server.send_message(msg)

    print(f'Emails sent successfully to {receiver}')

# Quit the SMTP server
server.quit()