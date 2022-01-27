import imaplib
import getpass

a=imaplib.IMAP4_SSL('imap.gmail.com')
email=getpass.getpass('enter your email:')
password=getpass.getpass('enter your password:')
a.login(email,password)
print(a.list())
a.select('Trash')


#typ, data = a.search(None,'SUBJECT "hi rajat" ')
#email_id=data[0]
#result, email_data= a.fetch(email_id, '(RFC822)')
#print(email_data)anurudhsharma014@gmail.com