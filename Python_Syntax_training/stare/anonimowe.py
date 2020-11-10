
def podwoj(x):
    return x*2

print(podwoj(4))

print((lambda x: x * 2)(4))

my_list = [2,14,22,7,6,4,5,17]
my_list_filtered = list(filter(lambda x: x % 2 ==0,my_list))
my_list_filtered2 = [x for x in my_list if (x % 2 ==0)]
