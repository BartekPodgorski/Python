import sqlite3
#Create DB
#conn = sqlite3.connect('logins.db')
#c = conn.cursor()
#c.execute("""CREATE TABLE accounts(
#				login text,
#				password text
#		)""")
#conn.commit()
#conn.close()

def add_account(newAdress, password1):
	conn = sqlite3.connect('logins.db')
	c = conn.cursor()
	c.execute("INSERT INTO accounts VALUES(?,?)", (newAdress, password1))
	conn.commit()
	conn.close()

def check_availability(newAdress):
	conn = sqlite3.connect('logins.db')
	c = conn.cursor()
	c.execute("SELECT login FROM accounts WHERE login IN (?)",(newAdress, ))
	item = c.fetchone()
	if item[0] == newAdress:
		return False
	else:
		return True
	conn.commit()
	conn.close()

def show_all():
	conn = sqlite3.connect('logins.db')
	c = conn.cursor()
	c.execute("SELECT * FROM accounts")
	items = c.fetchall()
	for element in items:
		print(element)
	conn.commit()
	conn.close()

def login(adress, password):
	conn = sqlite3.connect('logins.db')
	c = conn.cursor()
	c.execute("SELECT * FROM accounts WHERE login = (?) AND password = (?)",(adress, password))
	element = c.fetchone()
	if element == None:
		return False
	else:
		return True
	conn.commit()
	conn.close()