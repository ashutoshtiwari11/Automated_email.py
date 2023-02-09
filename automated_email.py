#First create a password in your e.g. google  security section you can create a app password for mail ---- for my computer windows mail section. and keep that password secure.

from email.message import EmailMessage
import getpass

#getpass is a function in the Python Standard Library's getpass module. It provides a secure way to handle password prompts.
#The function getpass(prompt='Password: ') displays the specified prompt string on the screen and reads input from the user. The user's input is not echoed to the screen, making it safe to use for password prompts. The input is returned as a string.

import smtplib

print("This is being print just to show that your file has start running.")
#("pass ***********")

message=EmailMessage() 
#The line message = EmailMessage() creates an instance of the EmailMessage class from the email module in the Python Standard Library


def add_attachment():
    import os.path
    attachment_path=input("Please enter the path of your attachment. \n:")
    attachment_filename= os.path.basename(attachment_path)
    import mimetypes
    mime_type=mimetypes.guess_type(attachment_path)
    print(mime_type)
    #separating mime type and sub type it is a tuple.
    mime_type, mime_subtype=mime_type[0].split('/',1)
    print(mime_type)
    print(mime_subtype)
    
    
    with open(attachment_path,'rb') as ap:
        try:
         message.add_attachment(ap.read(),
                               maintype=mime_type, 
                               subtype=mime_subtype,
                               filename=attachment_filename)
        except:
            print("there was an error in attachment addition.")
            
            

print("Ya! it seems to be working fine.")
sender="ashutoshtiwari6143@gmail.com"
recipient="neerutiwari12345@gmail.com"

#message['From'] is accessing the 'From' header field of an EmailMessage object in Python. note header field are case insensitive.

message["From"]=sender;
message["To"]=recipient;
message["Subject"]="Greeting from {}, please do not reply as this is an automated email".format(recipient)

print(message)
attachment=input("Do You want to add an attachment ? If yes type y else type n. \n:")
if(attachment == "y"):
    add_attachment()
    #I will not print message in case of attachment because it will take long to print in case of image or long pdf.
else:
    body=input("Please Enter your content in text form. \n -: ")
    message.set_content(body)
    print(message)



mail_server = smtplib.SMTP_SSL('smtp.gmail.com')

#This SSL/TLS is the same protocol that's used to add a secure transmission layer to HTTP, making it HTTPS. Within the smtplib, there are two classes for making connections to an SMTP server: The SMTP class will make a direct SMTP connection, and the SMTP_SSL class will make a SMTP connection over SSL/TLS. 

#mail_server.set_debuglevel(1)

#debuglevel - 1 to show what is happening behind the scene.

password = getpass.getpass(prompt= ' \n Enter password: ')

print('You entered:', password)

mail_server.login(sender,password )

print("login was succesful in case you are seeing this may be...")
mail_server.send_message(message)
#mail_server.set_debuglevel(1)
mail_server.quit()
#so its important to quit the server.
