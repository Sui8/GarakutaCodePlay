from bisect import bisect_left

N = int(input())

score = []

for i in range(N):
    score.append(int(input()) * -1)

ranking = sorted(score)

for i in score:
    print(bisect_left(ranking, i) + 1)