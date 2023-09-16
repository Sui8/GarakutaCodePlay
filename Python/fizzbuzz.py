count = int(input("count: "))

for i in range(1, count+1):
    if i % 15 == 0:
        print(f"FizzBuzz: {i}")

    elif i % 3 == 0:
        print(f"Fizz: {i}")

    elif i % 5 == 0:
        print(f"Buzz: {i}")

    else:
        pass

    count += 1
