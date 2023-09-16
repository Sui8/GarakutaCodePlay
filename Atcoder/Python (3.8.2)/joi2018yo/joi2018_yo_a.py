import math

N, A, B, C, D = (int(i) for i in input().split())

if math.ceil(N / A) * B >= math.ceil(N / C) * D:
    print(math.ceil(N / C) * D)

else:
    print(math.ceil(N / A) * B)