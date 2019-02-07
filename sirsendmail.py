"""The first step is to create an SMTP object, each object is used for connection 
with one server."""

import smtplib
server = smtplib.SMTP('krishnaveni071996@gmail.com', 587)

#Next, log in to the server
server.login("krishna veni", "pavithra071996")

#Send the mail
msg = "hello"
Hello!" # The /n separates the message from the headers
server.sendmail("krishnaveni071996@gmail.com", "krishnaveni071996@gmail.com", msg)

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "krishnaveni071996@gmail.com"
toaddr = "krishnaveni071996@gmail.com"
msg = MIMEMultipart()
msg['From'] = krishnaveni071996@gmail.com
msg['To'] = krishnaveni071996@gmail.com
msg['Subject'] = "Python email"

body = "Python test mail"
msg.attach(MIMEText(body, 'plain'))

import smtplib
server = smtplib.SMTP('krishnaveni071996@gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("krishna veni", "pavithra071996")
text = msg.as_string()
server.sendmail(krishnaveni071996@gmail.com, krishnaveni071996@gmail.com, text)

import smtplib
 
def sendemail(krishnaveni071996@gmail.com, krishnaveni071996@gmail.com, 
              subject, message,
              krishna veni, pavithra071996,
              smtpserver='krishnaveni071996@gmail.com:587'):
    header  = 'From: %s
' % from_addr
    header += 'To: %s
' % ','.join(to_addr_list)
    header += 'Cc: %s
' % ','.join(cc_addr_list)
    header += 'Subject: %s

' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(krishna veni,pavithra071996)
    problems = server.sendmail(krishnaveni071996@gmail.com, krishnaveni071996@gmail.com, message)
    server.quit()
