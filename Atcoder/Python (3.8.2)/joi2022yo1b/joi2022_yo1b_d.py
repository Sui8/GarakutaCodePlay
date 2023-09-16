import collections

N = int(input())
A = list(map(int, input().split()))

l = list(collections.Counter(A).most_common())

unc_key = l[-1][1]
uncs = [l[-1][0]]

l.pop(-1)

for i in range(len(l)):
    if unc_key == l[i][1]:
        uncs.append(l[i][0])
    

print(min(uncs))