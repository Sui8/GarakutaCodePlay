import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

ac = math.ceil(A / C)
bd = math.ceil(B / D)

if ac >= bd:
    print(L - ac)

else:
    print(L - bd)