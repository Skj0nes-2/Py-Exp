
# Imports
import random as ran
import math as mt

# Establish Variables
length = 4; min = 0; max = 4; arr = [0]; iter = 0; dist = int(mt.dist(int(max), int(min)))
print(dist)
total_combos = length ** dist; digits = list(range(min, max + 1))

# Run loop
def getCombo():
    combo = ''
    iter = 0
    while iter != length:
        combo_digit = ran.choice(digits)
        combo = int(str(combo) + '' + str(combo_digit))
        iter = iter + 1
    return combo

while iter != total_combos:
    combo = getCombo()
    if combo not in arr:
        arr.append(combo)
        iter = iter + 1
arr.sort()
print(arr)