N = int(int(input()))
A = list(map(int, input().split()))
M = int(int(input()))
B = list(map(int, input().split()))

score = 0

for i in range(N):
    score += A[i]

    for j in range(M):
        if B[j] == score:
            score = 0

print(score)