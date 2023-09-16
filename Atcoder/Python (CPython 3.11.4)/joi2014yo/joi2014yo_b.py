N, M = (int(x) for x in input().split())

costs = []
points = []
judgel = []

for i in range(N):
    costs.append(int(input()))
    points.append(0)

for i in range(M):
    judgel.append(int(input()))

for i in range(M):
    for j in range(N):
        if costs[j] <= judgel[i]:
                  points[j] += 1
                  break

print(points.index(max(points)) + 1)