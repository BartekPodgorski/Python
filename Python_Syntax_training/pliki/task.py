print("Welcome in my program!!\nGive the name of the file which you would like to open")
name = input("Give the name of file: ")

def open_file(name):
    try:
        with open(name, "r",encoding="UTF-8") as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print("-------------")

open_file(name)
