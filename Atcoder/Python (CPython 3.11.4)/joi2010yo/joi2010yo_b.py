N, M = (int(x) for x in input().split())

mmap = []
dice = []

pos = 0

for i in range(N):
    mmap.append(int(input()))

for i in range(M):
    dice.append(int(input()))


for i in range(M):
    pos += dice[i]
    
    if pos >= N-1:
        print(i+1)
        exit(0)

    pos += mmap[pos]

    if pos >= N-1:
        print(i+1)
        exit(0)
    
print(M)