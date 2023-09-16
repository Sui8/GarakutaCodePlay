N, M = (int(x) for x in input().split())

A = []

for i in range(N):
    A.append(int(input()))

for k in range(M):
    for i in range(N-1):
        if A[i] % (k+1) > A[i+1] % (k+1):
            A[i], A[i+1] = A[i+1], A[i]

for i in A:
    print(i)