# lazy-aidan
>  An easy sms/email notifier that lets you send yourself updates on how your code is doing.



##  How to use:

### Create a burner gmail account: 
Go to this and fill out the details.
https://accounts.google.com/SignUp

### Allow account access to the script.
Go to Google's Account Security Settings: www.google.com/settings/security
Find the field "Access for less secure apps". Set it to "Allowed".

### Add this before the send function (preferably at the top) and initialize with your info
```
varname = Aidan(email="sender gmail adress", pwd="your password", to="to email/sms number", carrier="choose from the carrier list below")
```

### Add this with a message with relevant info from your code
```
varname.send(msg="New message here")
```

### Carrier list: (Paste the exact string into the the carrier="" in the Aidan() class)
* All Tell
* AT&T
* Rogers
* Sprint
* T-Mobile
* Telus
* Verizon
* Virgin Mobile
* Orange


##  Cheers!
