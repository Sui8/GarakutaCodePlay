import collections

A = input()
B = list(map(int, input().split()))

c = collections.Counter(B)

print(c.most_common()[0][1])
