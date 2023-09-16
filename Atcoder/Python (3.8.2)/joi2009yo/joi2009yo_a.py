A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

s = A[5] - A[2]
m = A[4] - A[1]
h = A[3] - A[0]

if s < 0:
  s = 60 + s
  m -= 1
  
if m < 0:
  m = 60 + m
  h -= 1
  
print(f"{h} {m} {s}")

s = B[5] - B[2]
m = B[4] - B[1]
h = B[3] - B[0]

if s < 0:
  s = 60 + s
  m -= 1
  
if m < 0:
  m = 60 + m
  h -= 1
  
print(f"{h} {m} {s}")

s = C[5] - C[2]
m = C[4] - C[1]
h = C[3] - C[0]

if s < 0:
  s = 60 + s
  m -= 1
  
if m < 0:
  m = 60 + m
  h -= 1
  
print(f"{h} {m} {s}")

