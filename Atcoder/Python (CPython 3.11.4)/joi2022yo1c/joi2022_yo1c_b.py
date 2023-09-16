import math

S = int(input())
A = int(input())
B = int(input())

if A >= S:
    print(250)

else:
    print(250 + (100 * math.ceil((S - A) / B)))