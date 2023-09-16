N, M = (int(x) for x in input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = []

for i in range(N+M):
    if len(A) < 1:
        C.append(B.pop(0))

    elif len(B) < 1:
        C.append(A.pop(0))
    
    elif A[0] <= B[0]:
        C.append(A.pop(0))

    else:
        C.append(B.pop(0))

for i in C:
    print(i)