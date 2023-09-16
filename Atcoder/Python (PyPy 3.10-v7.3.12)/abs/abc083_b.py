N, A, B = map(int, input().split())

asum = 0

for i in range(1, N+1):
    X = list(str(i))
    X = list(map(int, X))

    if sum(X) >= A and sum(X) <= B:
        asum += i

print(asum)