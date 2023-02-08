#First create a password in your e.g. google  security section you can create a app password for mail ---- for my computer windows mail section. and keep that password secure.



from email.message import EmailMessage
import getpass

#getpass is a function in the Python Standard Library's getpass module. It provides a secure way to handle password prompts.
#The function getpass(prompt='Password: ') displays the specified prompt string on the screen and reads input from the user. The user's input is not echoed to the screen, making it safe to use for password prompts. The input is returned as a string.

import smtplib

print("This is the being print just to show that your file has start running.")
#("pass ***********")

message=EmailMessage() 
#The line message = EmailMessage() creates an instance of the EmailMessage class from the email module in the Python Standard Library

print(message)
print("Ya! it seems to be working fine.")
sender="ashutoshtiwari6143@gmail.com"
recipient="neerutiwari12345@gmail.com"

#message['From'] is accessing the 'From' header field of an EmailMessage object in Python. note header field are case insensitive.

message["From"]=sender;
message["To"]=recipient;
message["Subject"]="Greeting from {}, please do not reply as this is an automated email".format(recipient)

body=input("Please Enter your content in text form. \n -: ")
message.set_content(body)

print(message)

mail_server = smtplib.SMTP_SSL('smtp.gmail.com')

#This SSL/TLS is the same protocol that's used to add a secure transmission layer to HTTP, making it HTTPS. Within the smtplib, there are two classes for making connections to an SMTP server: The SMTP class will make a direct SMTP connection, and the SMTP_SSL class will make a SMTP connection over SSL/TLS. 

mail_server.set_debuglevel(1)

#debuglevel - 1 to show what is happening behind the scene.

password = getpass.getpass(prompt= ' \n Enter password: ')

print('You entered:', password)

mail_server.login(sender,password )

print("login was succesful in case you are seeing this may be...")
mail_server.send_message(message)
mail_server.set_debuglevel(1)
mail_server.quit()
#so its important to quit the server.
