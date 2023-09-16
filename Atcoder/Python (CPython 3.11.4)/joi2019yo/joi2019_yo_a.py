A, B, C  = (int(x) for x in input().split())

coin = 0
days = 0

while True:
    if coin < C:
        coin += A
        days += 1

        if days % 7 == 0:
            coin += B

    else:
        print(days)
        exit(0)