#!/usr/bin/python
import smtplib 

sender = 'krishnaveni071996@gmail.com'
receivers = ['krishnaveni071996@gmail.com']
message = """From: From person <krishnaveni071996@gmail.com>
To: To Person <krishnaveni071996@gmail.com>
Subject: SMTP e-mail test
This is a test e-mail message.
"""
try: 
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print "Succcessfully sent email"
except SMTPException:
except smtplib.SMTPException:
  smtlib.SMTP('smtp.gmail,587')
  print "ERROR: unable to send email"
