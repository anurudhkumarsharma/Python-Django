def try_except():
    while True:
        try:
            num1 = int(input('enter 1st number:'))
            num2 = int(input('enter 2nd number:'))
            result = num1+num2
            print('The result is:', result)

        except:
            print("Please only enter interger!")
            continue
        else:
            print('Yes thank you')
            break


try_except()
