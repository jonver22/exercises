# Write your code here
import re
def is_valid_time(string):
    return re.fullmatch('[2][0-3]|[0-1][0-9]:([0-5][0-9]:)([0-5][0-9])(.[0-9]{3})?', string)
    