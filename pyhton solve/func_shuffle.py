
def shuffle_list(list):
    from random import shuffle
    shuffle(list)
    return list
result=shuffle_list([1,2,3,4,5,6])
print(result)