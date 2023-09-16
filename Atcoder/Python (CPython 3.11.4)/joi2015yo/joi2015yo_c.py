H, W = (int(x) for x in input().split())

wmap = []

for i in range(H):
    wmap.append(list(input()))

for i in range(H):
    if wmap[i][0] == "c":
        wmap[i][0] = 0

    else:
        wmap[i][0] = -1

    for j in range(1, W):
        if wmap[i][j] == "c":
            wmap[i][j] = 0

        else:
            if wmap[i][j-1] == -1:
                wmap[i][j] = -1

            else:
                wmap[i][j] = wmap[i][j-1] + 1

for i in range(H):
    print(*wmap[i])