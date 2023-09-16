N = int(input()) - 1
A = list(map(int, input().split()))

for x in range(N):
    lold = len(A)
    
    for i in range(len(A) - 1):
        A.append(abs(A[i] - A[i+1]))

    del A[0:lold]

print(A[0])