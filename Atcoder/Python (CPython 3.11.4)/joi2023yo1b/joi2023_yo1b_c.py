N = int(int(input()) / 2)
S = input()

if S[:N] == S[N:]:
    print("Yes")

else:
    print("No")