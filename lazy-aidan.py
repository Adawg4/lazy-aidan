#lazy-aidan
import smtplib

#carrier dict
carriers = {'All Tell' : '@alltelmessage.com',
            'AT&T' : '@txt.att.net',
            'Rogers' : '@pcs.rogers.com',
            'Sprint': '@messaging.sprintpcs.com',
            'T-Mobile' : '@tmomail.net',
            'Telus' :'@msg.telus.com',
            'Verizon' : '@vtext.com',
            'Virgin Mobile' : '@vmob1.com',
            'Orange' : '@o2.co.uk'}

class Aidan:
	def __init__(self, email, pwd, to, carrier=None):
		self.email = email
		self.pwd = pwd
		if carrier:
			to = str(to)+str(carriers[carrier])
		self.to = to
		self.carrier = carrier or None

	def send(self, msg: str): 
		# Establish a secure session with gmail's outgoing SMTP server using your gmail account
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls()
		server.login(self.email,self.pwd)
		server.sendmail(self.email, self.to,msg)
'''
How to use:
Create a burner gmail account: 
Go to this and fill out the details.
https://accounts.google.com/SignUp

Allow account access to the script.
Go to Google's Account Security Settings: www.google.com/settings/security
Find the field "Access for less secure apps". Set it to "Allowed".

Add this before the send function (preferably at the top) and initialize with your info
varname = Aidan(email="sender gmail adress", pwd="your password", to="to email/sms number", carrier="choose from the carrier list below")

Add this with a message with relevant info from your code
varname.send(msg="New message here")

Carrier list: (Paste the exact string into the the carrier="" in the Aidan() class)
All Tell
AT&T
Rogers
Sprint
T-Mobile
Telus
Verizon
Virgin Mobile
Orange
'''

