N = int(input())
A = list(map(int, input().split()))

ranking = sorted(A)

for i in range(N):
    print(ranking.index(A[i]) + 1)