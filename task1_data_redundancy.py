import mysql.connector

db = mysql.connector.connect(
    host="thomas.proxy.rlwy.net",
    user="root",
    password="WvvsADfQImKPbdshEKGKluBeFVTYhjPV",
    database="railway",
    port=18989
)

cursor = db.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS records (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15)
)
""")

db.commit()

def check_record(id, name, email):
    cursor.execute("SELECT * FROM records WHERE id=%s", (id,))
    if cursor.fetchone():
        return "REDUNDANT - Duplicate ID"

    cursor.execute("SELECT * FROM records WHERE email=%s", (email,))
    if cursor.fetchone():
        return "REDUNDANT - Duplicate Email"

    cursor.execute("SELECT * FROM records WHERE name=%s", (name,))
    if cursor.fetchone():
        return "FALSE POSITIVE"

    return "UNIQUE"

while True:
    print("\n1 Add Record")
    print("2 Exit")

    choice = input("Choice: ")

    if choice == "1":
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")

        result = check_record(id, name, email)
        print(result)

        if result == "UNIQUE":
            sql = "INSERT INTO records VALUES (%s,%s,%s,%s)"
            val = (id, name, email, phone)
            cursor.execute(sql, val)
            db.commit()
            print("Inserted successfully")

    elif choice == "2":
        break
cursor = db.cursor()
cursor.execute("delete")
db.commit()
print("data deleted")    

db.close()