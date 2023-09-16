N = int(input())
S = list(input())

for i in range(N - 1):
    if S[i] == S[i+1]:
        S[i], S[i+1] = S[i].upper(), S[i+1].upper()

print("".join(S))