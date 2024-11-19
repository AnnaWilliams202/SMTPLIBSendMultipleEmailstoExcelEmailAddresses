# SMTPLIBSendMultipleEmailstoExcelEmailAddresses
The code will read email addresses from the your_file.xlsx file and send an email with the subject and the body message to each address. The script will print a confirmation message for each email sent successfully.
Install Required Libraries:
Ensure you have the necessary library installed by running the following command in your terminal:
pip install pandas
Prepare the Excel File:
Create an Excel file named your_file.xlsx containing a column labeled Email with the recipients' email addresses.
Library Imports:
The script imports pandas for reading Excel files and smtplib for sending emails.

Load the Excel File:
It reads the Excel file containing email addresses into a Pandas DataFrame.

Email Setup:
The sender's email, password, subject, and body of the message are defined.

SMTP Server Initialization:
An SMTP server is set up with Gmail's SMTP server, and the sender's email is logged in.

Sending Emails:
The script iterates through the DataFrame rows, retrieves each recipient's email, and constructs the email message.

The email is sent to each recipient, and a confirmation message is printed to the console.
Closing the SMTP Connection:

Finally, the script quits the SMTP server connection.
