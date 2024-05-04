from email.message import EmailMessage
import ssl 
import smtplib
from p import password

email_sender = 'jyo020424@gmail.com'
email_password =  password # Replace 'your_password' with your actual password

email_receiver = 'telugujyothi04@gmail.com'
#'hetisar571@shanreto.com'  # Fix typo in variable name

subject = "email sedning through python"
body = """
helo hetisr571,
this is jyothi here, iam sending this email using python code with the help of Emailmessage class email.message module
and ssl and smtplib modules which provides connection between client(python code) to SMTP (simple mail transver potocal)
server and provides security while making connection with the server and the smtplib.smtp_ssl() make sure the path is close after 
sending messages, this controls the opening and closing of the sessions immedaitly within the with block.
    
    * set_content() will set the body content of the email.

     *context = ssl.create_default_context():   The default context aims to provide a balance between security and compatibility, ensuring that connections
          are secure while remaining compatible with a wide range of servers and clients
  
     * the login() and sendmail() are responsible for loging into our account before seding messages and 
        seding mail to  the specified mail.

      *The email content must be encoded as bytes before being sent over the network using em.as_string().encode('utf-8').
"""

em = EmailMessage()
em['from'] = email_sender
em['to'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string().encode('utf-8'))  
