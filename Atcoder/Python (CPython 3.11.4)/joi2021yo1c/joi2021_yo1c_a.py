A, B = (int(x) for x in input().split())

if A - B > A + B:
    print(A - B)
    print(A + B)

else:
    print(A + B)
    print(A - B)