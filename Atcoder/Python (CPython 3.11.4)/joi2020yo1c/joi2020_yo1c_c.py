N = int(input())
A = list(map(int, input().split()))

ans = 0
a_max = 0

for i in range(N - 1):
    if A[i] <= A[i+1]:
        if ans == 0:
            ans += 2

        else:
            ans += 1

    else:
        if ans > a_max:
            a_max = ans
            
        ans = 0

if ans > a_max:
    a_max = ans

if a_max == 0:
    a_max = 1

print(a_max)