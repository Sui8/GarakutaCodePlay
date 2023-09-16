N = int(input())

matches = []
teams = []

for i in range(N):
    teams.append(0)

for i in range(int(N*(N-1)/2)):
    matches.append(list(map(int, input().split())))
    

for i in matches:
    if i[2] > i[3]:
        teams[(i[0] - 1)] += 3

    elif i[2] == i[3]:
        teams[(i[0] - 1)] += 1
        teams[(i[1] - 1)] += 1

    else:
        teams[(i[1] - 1)] += 3


ranking = sorted(teams, reverse=True)

for i in range(N):
    print(ranking.index(teams[i]) + 1)