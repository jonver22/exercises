# Write your code here
def sum_dict_values(x):
    lst = list(x.values())
    result = 0
    for item in lst:
        result = result + item
    return result

def sum_dict_values(dictionary):
    return sum(dictionary.values())
        