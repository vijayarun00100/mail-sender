import smtplib 
username='blockloader78@gmail.com' 
message=input('what is the message:') 
reciver=input('reciver mail:') 
password=input('xxxxxxxxxxx') 
server=smtplib.SMTP('smtp.gmail.com',587)  

server.starttls() 
server.login(username,password) 
server.sendmail(username,reciver,message) 
server.quit() 
