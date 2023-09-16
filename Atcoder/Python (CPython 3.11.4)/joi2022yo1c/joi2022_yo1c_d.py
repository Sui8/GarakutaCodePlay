N, M = (int(x) for x in input().split())

l = []
ball_pos = []

for i in range(1, N+1):
    ball_pos.append(i)

for i in range(M):
    l.append(list(map(int, input().split())))

for i in range(M):
    ball_pos[l[i][0] - 1] = l[i][1]

for i in ball_pos:
    print(i)