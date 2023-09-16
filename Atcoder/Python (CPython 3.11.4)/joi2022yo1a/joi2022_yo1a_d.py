N, M = (int(x) for x in input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

counter = 0

for i in range(N):
    if A[i] in B:
        counter += 1

print(counter)