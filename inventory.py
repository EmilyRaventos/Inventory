import sqlite3

# Define connection and cursor

connection = sqlite3.connect("store_transactions.db")

cursor = connection.cursor()

# Create stores table

# This table represents store locations

command1 = """CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY, location TEXT)"""

cursor.execute(command1)

# Create purchases table

# This table represents purchase transactions

command2 = """CREATE TABLE IF NOT EXISTS
purchases(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT,
FOREIGN KEY(store_id) REFERENCES stores(store_id))"""

cursor.execute(command2)

# Add to stores

# 

cursor.execute("INSERT INTO stores VALUES (21, 'Minneapolis, MN')")
cursor.execute("INSERT INTO stores VALUES (95, 'Chicago, IL')")
cursor.execute("INSERT INTO stores VALUES (64, 'Iowa City, IA')")

# Add to purchases

cursor.execute("INSERT INTO purchases VALUES (54, 21, 15.49)")
cursor.execute("INSERT INTO purchases VALUES (23, 64, 21.12)")

# Get results

# Retrieves data from the purchases table using a SELECT statement dn stores teh results in the 'results' variable.

cursor.execute("SELECT * FROM purchases")

results = cursor.fetchall()
print(results)

# Update

# This updates a specific record in the 'purchases' table by changing the 'total_cost' for a purchase with 'purchase_id of 54.

cursor.execute("UPDATE purchases SET total_cost = 3.67 WHERE purchase_id = 54")
print(results)

# Delete

cursor.execute("DELETE FROM purchases WHERE purchase_id = 54")
print(results)