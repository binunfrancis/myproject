# Script to send mail using Mailhog SMTP server running on Docker
# SMTP Port : 1025

import smtplib

SMTP_SERVER='192.168.0.10'
SMTP_PORT=1025

user = 'from@gmail.com'

msg = 'Test Mail'
to ='to@gmail.com'


def SendMail(MailFrom,MailBody,MailTo):
	print("Connecting to the server.....")
	s = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
	s.ehlo()
	print("Successfully connected to Server...")
	s.sendmail(MailFrom,MailTo,MailBody)
	s.quit()
	print("Mail have been sent successfully.....!")


SendMail(user,msg,to)