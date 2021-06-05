
try:
    f=open('testfile','r')
    f.write("my name is lakhan")
except:
    print('All other errors')
finally:
    print('I run always')

