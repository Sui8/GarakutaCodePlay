N = input()

mx = len(N) - 2

counter = 0

for i in range(mx):
    if N[i:i+3] == "JOI":
        counter += 1

print(counter)

counter = 0

for i in range(mx):
    if N[i:i+3] == "IOI":
        counter += 1

print(counter)