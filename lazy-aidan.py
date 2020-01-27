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
		print(self.to)

	def send(self, msg: str): 
		# Establish a secure session with gmail's outgoing SMTP server using your gmail account
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls()
		server.login(self.email,self.pwd)
		server.sendmail(self.email, self.to,msg)

updater = Aidan(email="", pwd="", to="", carrier="")
updater.send("")

'''
set settings to low accesss
#initialize with your info
updater = Aidan(email="", pwd="", to="", carrier="")
Aidan.send(msg="")
'''

