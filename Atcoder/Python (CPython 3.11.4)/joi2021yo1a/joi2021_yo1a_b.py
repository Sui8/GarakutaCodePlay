import collections

N = int(input())

S = list(input())

Sdash = []

c = collections.Counter(S)

for i in range(c["J"]):
    Sdash.append("J")

for i in range(c["O"]):
    Sdash.append("O")

for i in range(c["I"]):
    Sdash.append("I")

print("".join(Sdash))