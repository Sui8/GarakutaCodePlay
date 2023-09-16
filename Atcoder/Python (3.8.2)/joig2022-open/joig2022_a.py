N = int(input())
A = list(map(int ,input().split()))

A.sort(reverse=True)

del A[0]
del A[-1]

print(sum(A))