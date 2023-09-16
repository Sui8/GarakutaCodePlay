N = int(input())

S = input()

counter = 0
pos = 0

for i in range(N):
    if pos == 0 and S[i] != "I":
        counter += 1

    if pos == 1 and S[i] != "O":
        counter += 1

    if pos == 0:
        pos = 1

    else:
        pos = 0

print(counter)