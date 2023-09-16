import math

times = []

for i in range(4):
  times.append(int(input()))
  
s = sum(times)

print(math.floor(s / 60))
print(s - (60 * math.floor(s / 60)))