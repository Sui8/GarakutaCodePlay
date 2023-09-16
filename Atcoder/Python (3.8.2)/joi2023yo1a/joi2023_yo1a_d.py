import collections

N = int(input())

A = list(map(int, input().split()))

B = []

for key, value in collections.Counter(A).items():
    if value == 1:
        print(key)