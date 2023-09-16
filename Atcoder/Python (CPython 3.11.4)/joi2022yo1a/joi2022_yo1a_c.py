import collections

N = int(input())
S = input()

c = collections.Counter(S)

if len(list(c.values())) >= 3:
    print("Yes")

else:
    print("No")