A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

time = 0

if A < 0:
    time += C * (0 - A) + D
    time += E * B

else:
    time += E * (B - A)

print(time)