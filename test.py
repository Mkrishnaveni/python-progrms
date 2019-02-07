import smtplib

# Specifying the from and to addresses

fromaddr = 'krishnaveni071996@gmail.com'
toaddrs  = 'krishnaveni071996@gmail.com'

# Writing the message (this message will appear in the email)

msg = 'hello krish'

# Gmail Login

username = 'krishnaveni071996@gmail.com'
password = 'pavithra071996'

# Sending the mail  

server = smtplib.SMTP('krishnaveni071996@gmail.com',587)
server.starttls()
server.login(krishnaveni071996@gmail.com,pavithra071996)
server.sendmail(krishnaveni071996@gmail.com, krishnaveni071996@gmail.com, hey)
server.quit()
