# Inventory Overview

{Provide a description of the software that you wrote and how it integrates with a SQL Relational Database. Describe how to use your program.}

I wrote this software to help practice and demonstrate the skills I've been developing using databases, SQLite, and Python. This program demonstrates common database operations like creating tables, inserting data, selecting data, updating records, and deleting records.

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

SQLite is one of the most commonly used databases. It is a fast, lightweight database that doesn't require a separate server.

I created two tables for this program. The Stores table represents store locations and includes columns for Store IDs and Locations. The Purchases table represents purchase transactions and includes columns for the Purchase IDs, Store IDs, and Total Cost. The column each of these tables has in common is "store_id."

# Development Environment

Some tools I used in development:
- SQLite (sqlite3)
- Python
- Visual Studio Code

I built this using the Python programming language and SQLite library. Python is a high-level, widely used programming language and SQLite is a C Library. Both work very well together.

# Useful Websites

Some websites I found to be helpful as I learned more about databases and SQLite are:

- Sqlitetutorial (https://www.sqlitetutorial.net/)
- W3Schools (https://www.w3schools.com/sql/default.asp)

# Future Work

- How each purchase is displayed when selected
- Add a menu in Python for actions to be done in SQLite (inserting data, updating and deleting records, etc.)
- Figure out how to add functions to accomplish the second list item efficiently.
