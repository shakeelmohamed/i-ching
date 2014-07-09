"""
Steps for the I-Ching:

1. Flip 3 coins at once
2. Heads are 3 points, tails are 2 points
3. If odd, draw unbroken line. If even, draw line with a break in the center. Write he numerical value next to it.
4. Repeat, steps 1-3, but draw the line above the first line. Do this until you have 6 lines.
"""
from random import randint
lines = []
sums = []

for i in range (0, 6):
    sum = 0
    for x in range(0,3):
        val = randint(0,1)
        if val == 0:
            val = 2
        else:
            val = 3
        sum = sum + val
    sums.append(sum)

counter = 1
for i in reversed(sums):
    if i % 2 == 0:
        print '-- --' + str(i)
    else:
        print '-----' + str(i)
