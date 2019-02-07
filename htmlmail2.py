import email.message
import smtplib

msg = email.message.Message()
msg['Subject'] = 'foo'
msg['From'] = 'krishnaveni071996@gmail.com'
msg['To'] = 'krishnaveni071996@gmail.com'
msg.add_header('Content-Type','text/html')
msg.set_payload('Body of <b>message</b>')

# Send the message via local SMTP server.
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login(krishnaveni,
        pavithra071996)
s.sendmail(msg['krishnaveni071996@gmail.com'], [msg['krishnaveni071996@gmail.com']], msg.as_string())
s.quit()
