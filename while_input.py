def func():
    print('\n'*10)
    result=input("           Hello Rajat Sharma!\nHow are you?\n")
    if result=='good':
       print("That's Cool")
    else:
       while result!='good':
         result=input("I will keep asking this ,until you are not good.If you want me to stop, then type 'good':")
    print(result)
func()
   