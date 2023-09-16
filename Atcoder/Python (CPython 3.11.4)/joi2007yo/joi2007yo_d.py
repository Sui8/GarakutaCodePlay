n = int(input())
m = int(input())

k = []
cards = []


for i in range(m):
    k.append(int(input()))

for i in range(n*2):
    cards.append(i+1)

for i in range(m):
    if k[i] == 0:
        riA = cards[0:n]
        riB = cards[n:(n*2)]
        cards = []

        for j in range(n):
            cards.append(riA[j])
            cards.append(riB[j])

    else:
        riA = cards[0:k[i]]
        riB = cards[k[i]:(n*2)]

        cards = riB + riA

for i in range(n*2):
    print(cards[i])