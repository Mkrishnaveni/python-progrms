import smtplib
server = smtplib.SMTP('krishnaveni071996@gmail.com,:587')
server.ehlo()
server.starttls()
server.login("krishnaveni071996@gmail.com", "pavithra071996")
msg = "Wow I GOT IT..!"
server.sendmail("krishnaveni071996@gmail.com", "krishnaveni071996@gmail.com",msg)
server.quit()
print("sent")
