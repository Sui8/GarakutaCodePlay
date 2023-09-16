A, B, C = (int(x) for x in input().split())

if C - B < 0 and C - A >= 0:
    print(1)

else:
    print(0)