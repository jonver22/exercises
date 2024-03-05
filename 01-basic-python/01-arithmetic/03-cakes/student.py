# Write your code here
def cakes(eggs, butter, flour):
    cakes_for_Eggs = eggs // 5
    cakes_for_butter = butter // 250
    cakes_for_flour = flour // 250
    return min(cakes_for_Eggs,cakes_for_butter,cakes_for_flour)
