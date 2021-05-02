def ckeck_even_list(number_list):
    even_numbers = []
    for number in number_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers


print(ckeck_even_list([1, 2, 3, 4, 5, 1000, 20, 3, 6, 80]))
