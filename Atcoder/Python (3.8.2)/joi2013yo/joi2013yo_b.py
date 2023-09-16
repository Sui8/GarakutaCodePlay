N = int(input())

l = []
tmp1 = []
tmp2 = []
tmp3 = []
score = 0

for i in range(N):
    l.append(list(map(int, input().split())))

for i in range(len(l)):
    tmp1.append(l[i][0])
    tmp2.append(l[i][1])
    tmp3.append(l[i][2])

for i in range(len(l)):
    if tmp1.count(l[i][0]) == 1:
        score += l[i][0]

    if tmp2.count(l[i][1]) == 1:
        score += l[i][1]

    if tmp3.count(l[i][2]) == 1:
        score += l[i][2]

    print(score)
    score = 0