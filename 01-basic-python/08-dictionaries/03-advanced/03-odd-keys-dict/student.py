# Write your code here
def odd_keys_dict(x):
    dictionary = {}
    for key,value in x.items():
        if key % 2 != 0:
            dictionary[key] = value
            
    return dictionary