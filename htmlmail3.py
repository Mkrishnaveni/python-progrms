import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "krishnaveni071996@gmail.com"
password = input("pavithra071996")


# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    smtpObj = smtplib.SMTP(smtp_server,port)
    smtpObj.ehlo() # Can be omitted
    smtpObj.starttls(context=context) # Secure the connection
    # Can be omitted
    smtpObj.login("krishnaveni071996@gmail.com", "pavithra071996")
    smtpObj.sendmail("krishnaveni071996@gmail.com","krishanveni071996@gmail.com",message)
    smtpObj.quit

    # TODO: Send email here
except SMTPException:
    # Print any error messages to stdout
    print "Error:Unable to send mail"


