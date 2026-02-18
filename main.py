import mysql.connector
from datetime import datetime

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="medication_db"
)

cursor = db.cursor()

def add_medicine():
    name = input("Enter medicine name: ")
    dosage = input("Enter dosage (e.g., 500mg): ")
    reminder_time = input("Enter reminder time (HH:MM:SS): ")
    notes = input("Enter notes: ")

    query = """
    INSERT INTO medicines (name, dosage, reminder_time, notes)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (name, dosage, reminder_time, notes))
    db.commit()
    print("Medicine added successfully!")

def view_medicines():
    cursor.execute("SELECT * FROM medicines")
    records = cursor.fetchall()

    print("\n---- Medicine List ----")
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]}, Dosage: {row[2]}, Time: {row[3]}, Notes: {row[4]}")

def check_reminders():
    current_time = datetime.now().strftime("%H:%M:%S")
    cursor.execute("SELECT name, reminder_time FROM medicines")

    print("\n---- Reminder Check ----")
    for name, reminder_time in cursor.fetchall():
        if str(reminder_time) == current_time:
            print(f"⏰ Time to take {name}!")

def menu():
    while True:
        print("\n1. Add Medicine")
        print("2. View Medicines")
        print("3. Check Reminder")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_medicine()
        elif choice == '2':
            view_medicines()
        elif choice == '3':
            check_reminders()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

menu()
