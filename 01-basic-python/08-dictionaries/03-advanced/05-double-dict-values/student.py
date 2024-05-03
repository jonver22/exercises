# Write your code here
def double_dict_values(dictionary):
    doubled_dict = {}
    for key , value in dictionary.items():
        doubled_dict[key] = value * 2
    return doubled_dict