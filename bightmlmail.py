#!/usr/bin/python

import smtplib
import base64

filename = "/tmp/test.txt"

# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

sender = 'krishnaveni071996@gmail.com'
reciever = 'krishnaveni071996@gmail.com'

marker = "AUNIQUEMARKER"

body ="""
This is a test email to send an attachement.
"""
# Define the main headers.
part1 = """From: From Person <krishnaveni071996@gmail.com>
To: To Person <krishnaveni071996@gmail.com>
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)

# Define the attachment section
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)
message = part1 + part2 + part3

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com:587')
   smtpObj.starttls()
   smtpObj.ehlo()
   smtpObj.login("krishnaveni071996@gmail.com","pavithra071996")
   smtpObj.sendmail("krishnaveni071996@gmail.com", "krishnaveni071996@gmail.com", message)
   smtpObj.quit()
   print "Successfully sent email"
except smtplib.SMTPException,error:
   print str(error)
   print "Error: unable to send email"
