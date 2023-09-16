Q = int(input())

S = []

shelf = []

for i in range(Q):
    S.append(input())

for i in range(Q):
    if S[i] == "READ":
        print(shelf.pop(-1))

    else:
        shelf.append(S[i])