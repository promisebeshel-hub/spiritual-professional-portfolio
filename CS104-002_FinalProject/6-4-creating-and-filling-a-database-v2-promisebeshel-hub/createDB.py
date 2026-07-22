import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('people.db')
cursor = conn.cursor()

# Create the users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        auth_level INTEGER
    )
''')

conn.commit()
conn.close()

print("Database 'people.db' and table 'users' created successfully.")
