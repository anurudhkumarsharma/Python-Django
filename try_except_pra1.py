#Write a function that asks for an integer and prints the square of it. Use a while loop with a try,
#except, else block to account for incorrect inputs.

#Input an integer: null
#An error occurred! Please try again!
#Input an integer: 2
#Thank you, your number squared is:  4

def ask():
   while True: 
    try:
        number=int(input("enter an integer:"))
        print('Thank you, your number squared is:',number**2)
    except:
        print('An error occurred! Please try again!')
        
    else:
        break
ask()