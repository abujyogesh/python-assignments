def unique_list(numbers):
    unique=[]
    for item in numbers:
        if item not in unique:
            unique.append(item)
    return unique



print("unique elements::",unique_list([10,20,30,40,50,50,40,30,20,10]))
