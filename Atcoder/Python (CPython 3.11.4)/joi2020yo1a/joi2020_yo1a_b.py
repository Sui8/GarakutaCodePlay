N = int(input())
S = input()

boin = ["a", "i", "u", "e", "o"]
counter = 0

for i in range(N):
    if S[i] in boin:
        counter += 1

print(counter)