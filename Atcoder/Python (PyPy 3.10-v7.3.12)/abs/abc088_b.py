N = int(input())
a = list(map(int, input().split()))

Alice = 0
Bob = 0
c = 0

a.sort(reverse=True)

for i in range(N):
    point = a.pop(0)

    if c == 0:
        Alice += point
        c = 1

    else:
        Bob += point
        c = 0

print(Alice-Bob)