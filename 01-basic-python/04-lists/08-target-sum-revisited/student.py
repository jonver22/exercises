# Write your code here
def target_sum(ns, target):
    ns.sort()
    count_x = 0
    count_y = 0
    for x in ns:
        count_y = 0
        for y in ns:
            if count_x != count_y:
              if x + y == target:
                return True
            count_y = count_y + 1

        count_x = count_x + 1
    return False

target_sum([1, 2, 2, 3, 3, 3, 8, 8], 16)