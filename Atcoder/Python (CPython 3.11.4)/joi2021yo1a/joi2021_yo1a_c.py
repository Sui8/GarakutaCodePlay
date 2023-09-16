N, M = (int(x) for x in input().split())

A = list(map(int, input().split()))

B = list(map(int, input().split()))

C = []

C = list(set(A) & set(B))

C.sort()

for i in C:
    print(i)