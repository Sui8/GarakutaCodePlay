import math

N = int(input())

N = 1000 - N

counter = 0

while N >= 500:
  N -= 500
  counter += 1

while N >= 100:
  N -= 100
  counter += 1

while N >= 50:
  N -= 50
  counter += 1

while N >= 10:
  N -= 10
  counter += 1

while N >= 5:
  N -= 5
  counter += 1

while N > 0:
  N -= 1
  counter += 1
    
print(counter)