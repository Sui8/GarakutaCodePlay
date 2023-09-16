N = int(input())
A = list(map(int, input().split()))

counter = 0
x = 1
  
while True:
    
  for i in range(N):
    if A[i] % 2 != 0:
        print(counter)
        exit(0)

    else:
        A[i] = (A[i] / 2)
    
  counter += 1