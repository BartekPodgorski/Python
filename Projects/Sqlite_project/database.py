import sqlite3

# Query The database return all records
def show_all():
	conn = sqlite3.connect('customer.db')

	c = conn.cursor()
	
	c.execute("SELECT rowid, * FROM customers")
	items = c.fetchall()
	
	for item in items:
		print(item)

	conn.commit()
	conn.close()

#Add a new record to The Table
def add_record(first, last, email):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("INSERT INTO customers VALUES(?,?,?)", (first,last,email))
	conn.commit()
	conn.close()

#Delete a record and we have to sent string

def delete_record(id):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("DELETE FROM customers WHERE rowid = (?)", id)
	conn.commit()
	conn.close()

#Add many records

def add_many_records(list):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.executemany("INSERT INTO customers VALUES(?,?,?)", list)
	conn.commit()
	conn.close()

# Lookup with where

def email_lookup(email):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("SELECT * FROM customers WHERE email = (?)", (email, ))
	items = c.fetchall()

	for item in items:
		print(item)

	conn.commit()
	conn.close()