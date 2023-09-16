import itertools as it

N = int(input())
A = list(map(int, input().split()))

counter = 0

for i in it.combinations(A, 3):
    i = list(i)
    if i[0] * i[1] == i[2]:
        counter += 1

print(counter)