#Pooja would like to withdraw X $US from an ATM. The cash machine will only 
#accept the transaction if X is a multiple of 5, and Pooja's account balance 
#has enough cash to perform the withdrawal transaction (including bank charges). 
#For each successful withdrawal the bank charges 0.50 $US. Calculate Pooja's account balance after an 
#attempted transaction.

x= int(input('enter the account that you want to withdraw:'))
acc_balance =round(float(input('enter the account balance:')),2)
if x%5==0 and x<=acc_balance:
    r=round(((acc_balance-x)-0.5),2)
    print(r)
else:
    print(acc_balance)
