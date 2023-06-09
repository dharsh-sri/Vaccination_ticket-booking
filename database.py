import sqlite3

# Connect to the database or create a new one if it doesn't exist
conn = sqlite3.connect('vaccination_app.db')
cursor = conn.cursor()

# Create Admin Table
cursor.execute('''CREATE TABLE IF NOT EXISTS Admin (
                    id INTEGER,
                    name TEXT,
                    email_id TEXT PRIMARY KEY,
                    password TEXT,
                    otp INTEGER
                )''')

# Create User Table
cursor.execute('''CREATE TABLE IF NOT EXISTS User (
                    id INTEGER,
                    name TEXT,
                    email_id TEXT PRIMARY KEY,
                    password TEXT,
                    otp INTEGER
                )''')

# Create Vaccination Center Table
cursor.execute('''CREATE TABLE IF NOT EXISTS VaccinationCenter (
                    center_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    admin_email_id TEXT,
                    place TEXT,
                    center_name TEXT,
                    dosage INTEGER,
                    working_hour TEXT,
                    FOREIGN KEY (admin_email_id) REFERENCES Admin(email_id)
                )''')

# Create Vaccination Slots Table
cursor.execute('''CREATE TABLE IF NOT EXISTS VaccinationSlots (
                    slot_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    center_id INTEGER,
                    slot_date TEXT,
                    available_slot INTEGER CHECK(available_slot <= 10),
                    user_email_id TEXT,
                    FOREIGN KEY (center_id) REFERENCES VaccinationCenter(center_id),
                    FOREIGN KEY (user_email_id) REFERENCES User(email_id)
                )''')

# Create User History Table
cursor.execute('''CREATE TABLE IF NOT EXISTS UserHistory (
                    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_email_id TEXT,
                    slot_id INTEGER,
                    center_id INTEGER,
                    slot_date TEXT,
                    FOREIGN KEY (user_email_id) REFERENCES User(email_id),
                    FOREIGN KEY (slot_id) REFERENCES VaccinationSlots(slot_id),
                    FOREIGN KEY (center_id) REFERENCES VaccinationCenter(center_id)
                )''')

# Commit the changes and close the connection
conn.commit()
conn.close()
