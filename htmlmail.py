#!/usr/bin/python
import smtplib
import email.utils

message = """From: From Person <krishnaveni071996@gmail.com>
To: To Person <krishnaveni071996@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""
try:
   smtpObj = smtplib.SMTP('smtp.gmail.com:587')
   smtpObj.starttls()
   smtpObj.ehlo()
   smtpObj.login("krishnaveni071996@gmail.com","pavithra071996")
   smtpObj.sendmail("krishnaveni071996@gmail.com","krishnaveni071996@gmail.com",message)
   smtpObj.quit()            
   print "Successfully sent email"
except smtplib.SMTPException:
   print "Error: unable to send email"
