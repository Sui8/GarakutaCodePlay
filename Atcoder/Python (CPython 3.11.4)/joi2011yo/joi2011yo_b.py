S = input()
N = int(input())

rings = []
counter = 0

for i in range(N):
    a = input()
    rings.append(a + a)


for i in range(N):
    if S in rings[i]:
        counter += 1

print(counter)