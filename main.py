number = int(input("Enter a number: "))

if number > 7:
    print("Hello")

name = input("Enter a name: ").strip()

if name == "John":
    print("Hello, John")
else:
    print("There is no such name")

numbers_input = input("Enter numbers separated by spaces: ")
numbers = numbers_input.split()

numbers_divisible_by_3 = []

for value in numbers:
    number = int(value)

    if number % 3 == 0:
        numbers_divisible_by_3.append(number)

print("Numbers divisible by 3:", numbers_divisible_by_3)

