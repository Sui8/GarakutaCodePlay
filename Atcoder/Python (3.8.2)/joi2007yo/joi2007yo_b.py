students = []
badguy = []

for i in range(28):
    students.append(int(input()))

for i in range(1, 31):
    if not i in students:
        badguy.append(i)
        
badguy.sort()
print(badguy[0])
print(badguy[1])