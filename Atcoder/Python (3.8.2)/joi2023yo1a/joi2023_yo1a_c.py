N = int(input())

S = input()

Ball = 1

Counter = 0

for i in range(N):
    
    if S[i] == "L":
        
        if not Ball == 1:
            Ball -= 1

    else:

        if Ball == 3:
            Counter += 1

        else:
            Ball += 1

            if Ball == 3:
                Counter += 1

print(Counter)