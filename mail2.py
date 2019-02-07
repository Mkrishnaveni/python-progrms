import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("tamilselvanmalar@gmail.com", "tamilmalar")

msg = "wow i got it..!"
server.sendmail("batch2zippyops@gmail.com", "tamilselvanmalar@gmail.com",msg)
server.quit()
print("sent")
