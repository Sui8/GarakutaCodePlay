sc = []
ss = []

for i in range(4):
    sc.append(int(input()))

for i in range(2):
    ss.append(int(input()))

print(sum(sc) + max(ss) - min(sc))