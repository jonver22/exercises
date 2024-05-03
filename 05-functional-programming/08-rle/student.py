def rle_encode(data):
    result = []
    previous = "sw"
    index = -1
    for letter in data:
        
        if letter != previous:
            index += 1
            count = 1
            result.append((letter, count))
            previous = letter
            
        elif letter == previous:
            count += 1
            result[index] = (letter, count)
            previous = letter
            
    return result

# print(rle_encode("aaaabbbcc"))

def rle_decode(data):
    result = ""
    for (char, count) in data:
        letters = char * count
        result = result + letters
    return result

# print(rle_decode([('a', 4), ('b', 2)]))