def generator_square():
    number = 0
    while True:
        number = number + 1
        yield  number * number

generatedNumbers = []

number_generator = generator_square()

for _ in range(20):
    generatedNumbers.append(next(number_generator))

print(generatedNumbers)

for _ in range(30):
     generatedNumbers.append(next(number_generator))

print(generatedNumbers)
