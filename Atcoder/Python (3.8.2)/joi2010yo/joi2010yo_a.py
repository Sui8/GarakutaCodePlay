bsum = int(input())

books = []

for i in range(9):
  books.append(int(input()))
  
print(bsum - sum(books))