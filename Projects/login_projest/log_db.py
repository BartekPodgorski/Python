import keyboard
import loginDb

print("Bart Post")
print("If you want to login click 'Ctrl' , if you want to register click 'Alt', if you want to watch all accounts click 'Esc'")

while True:
	#login
	if keyboard.is_pressed('Ctrl'):

		adress = input("E-mail address: ")
		password = input("password: ")		
		flag1 = loginDb.login(adress, password)
		if flag1 == True:
			print("Welcome")
			break
		else:
			print("Incorrect login or password")
			break

	#Create account (add record)
	elif keyboard.is_pressed('Alt'):

		newAdress = input("Please enter the new adress: ")
		
		flag2 = loginDb.check_availability(newAdress)
		if flag2 == False:
			print("This adress is not avaible")
			newAdress = input("Please give other e-mail address: ")

		password1 = input("Please enter the new password: ")
		password2 = input("Confirm the password: ")
		if password1 == password2:
			print("Hello in Bart Post")
			loginDb.add_account(newAdress, password1)
			break
		else:
			print("Incorrect password")
			break

	elif keyboard.is_pressed('Esc'):
		loginDb.show_all()
		break

