A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

a_sum = A*P

if P > C:
  b_sum = B + ((P - C) * D)

else:
  b_sum = B

if a_sum >= b_sum:
    print(b_sum)

else:
    print(a_sum)