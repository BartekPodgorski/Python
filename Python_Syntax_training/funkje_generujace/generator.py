def generate_even_numbers():
    print("start")
    for element in range(5):
        print("przed yield")
        if(element%2 == 0):
            yield element
            print("po yield")
            


evenNumberGenerator = (element**2
                       for element in range(401)
                       if(element%2 == 0))


a = generate_even_numbers()

def generate_10_numbers():
    x = 0
    while x<10:
        yield x
        x +=1
liczby = generate_10_numbers()
print(next(liczby))
print(next(liczby))
print(next(liczby))
print(list(generate_10_numbers()))
