N, M = (int(x) for x in input().split())

A = []

for i in range(M):
    A.append(int(input().split()[0]))

counter = 0
money = 0

A.sort(reverse=True)


for i in range(M - 1):
    if A[i] < N:
        money += N - A[i]

print(money)