import smtplib
import getpass
a=smtplib.SMTP('smtp.gmail.com',587)
print(a.ehlo())
a.starttls()

email=getpass.getpass('enter your email:')
password=getpass.getpass('enter your password:')
print(a.login(email,password))

from_address=email
to_address=email
subject=input('enter the subject line:')
message=input('enter the message body:')
msg= 'subject: ' + subject+ '\n'+ message
a.sendmail(from_address,to_address,msg)
a.quit()