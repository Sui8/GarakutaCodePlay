N = int(input())

A = list(map(int, input().split()))

indx = A.index(max(A))

if indx == 0:
    del A[0]
    print(0)
    print(sum(A))

elif indx == -1:
    del A[-1]
    print(sum(A))
    print(0)

else:
    print(sum(A[0:indx]))
    print(sum(A[(indx+1):]))