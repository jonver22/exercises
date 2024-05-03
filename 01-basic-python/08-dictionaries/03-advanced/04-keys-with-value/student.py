# Write your code here
def keys_with_value(dictionary, x):
    lst = []
    for key,value in dictionary.items():
        if x == value:
            lst.append(key)
    return lst
    