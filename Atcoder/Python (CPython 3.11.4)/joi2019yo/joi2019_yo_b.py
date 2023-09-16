N = int(input())
X = list(map(int, input().split()))
M = int(input())
A = list(map(int, input().split()))

for i in A:
    if not X[i-1] + 1 in X:
        if X[i-1] != 2019:
            X[i-1] = X[i-1] + 1

for i in X:
    print(i)