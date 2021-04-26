def ckeck_even_list(number_list):
    even_numbers=[]
    for number in number_list:
        if number%2 == 0:
            return even_numbers.append(number)
        else:
            pass
    
result=ckeck_even_list([1,2,3,4,5])
print(result)