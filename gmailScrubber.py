# Import mail module
import imaplib

# User credentials
my_email = 'Enter Your Email Here'
app_password = 'Enter your Gmail App Password Here'

# Initialize the gmail server
imap = imaplib.IMAP4_SSL("imap.gmail.com")

# Login to to gmail with credentials
imap.login(my_email, app_password)

# Selecting the gmail inbox
imap.select("INBOX")

# Selecting the mail to delete
status, message_id_list = imap.search(None, 'FROM "Enter the senders address here"')

# convert the string to ids to list the email ids
messages = message_id_list[0].split(b' ')

# Deleting messages
print('Deleting messages...')
count = 1
for mail in messages:
    # mark the mail as deleted
    imap.store(mail, "+FLAGS", "\\Deleted")

    print(count, "message(s) deleted.")
    count += 1
print("All of the selected message(s) have been deleted.")

# Delete all the selected messages
imap.expunge()

# Close the mailbox
imap.close()

# Logout from the server
imap.logout()
