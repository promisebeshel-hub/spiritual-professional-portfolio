import sqlite3
from users import users_data

# Connect to the database
conn = sqlite3.connect('people.db')
cursor = conn.cursor()

# Insert each record into the users table
for user in users_data:
    cursor.execute('''
        INSERT INTO users (username, password, auth_level)
        VALUES (?, ?, ?)
    ''', (user['username'], user['password'], user['auth_level']))

conn.commit()
conn.close()

print("Data inserted successfully into users table.")

