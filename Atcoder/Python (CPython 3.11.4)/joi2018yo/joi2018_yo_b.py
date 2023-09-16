N = int(input())
A = list(map(int, input().split()))

counter = 0
max_c = 0

for i in range(N):
    if A[i] == 1:
        counter += 1

    else:
        if counter > max_c:
            max_c = counter

        counter = 0

if counter > max_c:
    max_c = counter

print(max_c + 1)