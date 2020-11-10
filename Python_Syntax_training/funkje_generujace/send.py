def generator_square():
    number = 0
    while True:
        print("start number",number)
        number = number + 1
        number = yield  number * number
        print("po yield number",number)
        print("po yield sample",number)

generatedNumbers = []

number_generator = generator_square()

number_generator.send(None)

for i in range(20):
    generatedNumbers.append(number_generator.send(i))

print(generatedNumbers)

for i in range(30,50):
     generatedNumbers.append(number_generator.send(i))

print(generatedNumbers)

