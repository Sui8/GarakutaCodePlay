N = input()

counter = 0

new = []

for i in N:
    if i == "A":
        new.append("X")

    elif i == "B":
        new.append("Y")
        
    elif i == "C":
        new.append("Z")

    else:
        new.append(chr(ord(i) - 3))

print(''.join(new))