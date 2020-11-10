import keyboard
print("Bart Post")
print("If you want login click 'Ctrl' , if you want register click 'Alt'")

while True:
	#login
	if keyboard.is_pressed('Ctrl'):

		adress = input("E-mail address: ")
		password = input("password: ")
		login = adress + " " + password	
		with open("login.txt" , "r", encoding ="UTF-8") as f:
			if login in f.read():
				print("welcome")
				break
			else:
				print("Incorrect login or password")
				break
	#Create account
	elif keyboard.is_pressed('Alt'):

		newAdress = input("Please enter the new adress: ")
		with open("login.txt" , "r", encoding ="UTF-8") as f:
			if newAdress in f.read():
				print("This adress is not avaible")
				newAdress = input("Please give other e-mail address: ")

		password1 = input("Please enter the new password: ")
		password2 = input("Confirm the password: ")
		if password1 == password2:
			print("Hello in Bart Post")
			with open("login.txt", "a+", encoding ="UTF-8") as file:
				file.write(newAdress + " " + password1 + "\n")
			break
		else:
			print("Incorrect password")
			break
