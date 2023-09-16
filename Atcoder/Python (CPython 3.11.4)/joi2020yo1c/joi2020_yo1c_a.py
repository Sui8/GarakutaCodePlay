X, L, R = (int(x) for x in input().split())

ans = 99999999999
realans = 99999999999

for i in range(L, R+1):
    if abs(X - i) < ans:
        ans = abs(X - i)
        realans = i

print(realans)