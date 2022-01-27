import easyimap as e 
import getpass

email=getpass.getpass('enter your email:')
password=getpass.getpass('enter your password:')
a=e.connect('imap.gmail.com',email,password)
print(a.listids())
b=a.mail(a.listids()[0])
print(b.title)