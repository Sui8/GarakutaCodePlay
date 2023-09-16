N, A, B = (int(x) for x in input().split())
L = input()

T1 = L[0:A-1]
T2 = L[A-1:B]
T3 = L[B:N]

T2 = T2[::-1]

print(T1 + T2 + T3)