import collections

N = list(map(int, input().split()))

c = collections.Counter(N)

print(c.most_common()[0][0])