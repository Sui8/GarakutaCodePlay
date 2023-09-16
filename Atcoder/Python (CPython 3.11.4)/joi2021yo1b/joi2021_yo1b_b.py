N = int(input())

S = input()

counter = 0

for i in range(N):
    if S[i] == "I" and counter == 0:
        counter = 1

    if S[i] == "O" and counter == 1:
        counter = 2

    if S[i] == "I" and counter == 2:
        print("Yes")
        exit(0)

print("No")