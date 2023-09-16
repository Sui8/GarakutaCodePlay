N = int(input())
A = list(map(int, input().split()))

Amax = max(A)
Amin = min(A)

for i in range(N):
    print(max([abs(Amax - A[i]), abs(Amin - A[i])]))