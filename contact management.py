title = 'CONTACT LIST MANAGEMENT'
d = '--**************--'
x = title.center(80)
y = d.center(85)
print(x)
print(y)

import mysql.connector as con

def db_setup():
    mydb = con.connect(host='localhost', user='root', passwd='root')
    cur = mydb.cursor()
    try:
        cur.execute('create database if not exists contact_list_management')
        print("Database created")
    except:
        print("Database contact_list_management already exists")
    mydb.close()

def tb_setup():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='contact_list_management')
    cur = mydb.cursor()
    try:
        cur.execute('create table if not exists contacts(contact_id int primary key, name varchar(100), phone varchar(15), email varchar(100), address varchar(200))')
        print("Contacts Table setup done")
    except:
        print("Table contacts already exists")
    mydb.close()

def database_setup():
    while True:
        print("\nPress 1 to setup database")
        print("Press 2 to setup tables")
        print("Press 3 to go back to main menu\n")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            db_setup()
        elif ch == 2:
            tb_setup()
        elif ch == 3:
            return
        else:
            exit()

def add_contact():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='contact_list_management')
    cur = mydb.cursor()
    
    contact_id = int(input('Enter contact ID: '))
    name = input('Enter name: ')
    phone = input('Enter phone number: ')
    email = input('Enter email: ')
    address = input('Enter address: ')
    
    z = "insert into contacts(contact_id, name, phone, email, address) values(%s, %s, %s, %s, %s)"
    y = (contact_id, name, phone, email, address)
    
    cur.execute(z, y)
    print("Contact added successfully")
    mydb.commit()
    mydb.close()

def delete_contact():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='contact_list_management')
    cur = mydb.cursor()
    contact_id = int(input("Enter contact ID that you want to delete: "))
    z = "Delete from contacts where contact_id=%s"
    y = (contact_id,)
    cur.execute(z, y)
    if cur.rowcount <= 0:
        print("Enter the correct ID")
    else:
        print(cur.rowcount, "Contact successfully deleted")
    mydb.commit()
    mydb.close()

def update_contact_name():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='contact_list_management')
    cur = mydb.cursor()
    contact_id = int(input("Enter contact ID to update name: "))
    name = input("Enter updated name: ")
    z = "update contacts set name=%s where contact_id=%s"
    y = (name, contact_id)
    cur.execute(z, y)
    if cur.rowcount <= 0:
        print("Enter the correct ID")
    else:
        print(cur.rowcount, "Contact name updated successfully")
    mydb.commit()
    mydb.close()

def update_contact_number():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='contact_list_management')
    cur = mydb.cursor()
    contact_id = int(input("Enter contact ID to update number: "))
    number = input("Enter updated phone number: ")
    z = "update contacts set phone=%s where contact_id=%s"
    y = (number, contact_id)
    cur.execute(z, y)
    if cur.rowcount <= 0:
        print("Enter the correct ID")
    else:
        print(cur.rowcount, "Contact number updated successfully")
    mydb.commit()
    mydb.close()

def update_contact_email():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='contact_list_management')
    cur = mydb.cursor()
    contact_id = int(input("Enter contact ID to update email: "))
    email = input("Enter updated email: ")
    z = "update contacts set email=%s where contact_id=%s"
    y = (email, contact_id)
    cur.execute(z, y)
    if cur.rowcount <= 0:
        print("Enter the correct ID")
    else:
        print(cur.rowcount, "Contact email updated successfully")
    mydb.commit()
    mydb.close()

def update_contact_address():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='contact_list_management')
    cur = mydb.cursor()
    contact_id = int(input("Enter contact ID to update address: "))
    address = input("Enter updated address: ")
    z = "update contacts set address=%s where contact_id=%s"
    y = (address, contact_id)
    cur.execute(z, y)
    if cur.rowcount <= 0:
        print("Enter the correct ID")
    else:
        print(cur.rowcount, "Contact address updated successfully")
    mydb.commit()
    mydb.close()

def display_contact_list():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='contact_list_management')
    cur = mydb.cursor()
    cur.execute("SELECT name, phone FROM contacts")
    contacts = cur.fetchall()
    print("Contacts List:")
    print("---------------")
    print("|  Name\t|  Phone  |")
    print("---------------")
    for contact in contacts:
        print(f"|  {contact[0]}\t|  {contact[1]}  |")
    print("---------------")
    mydb.close()

def search_contact():
    mydb = con.connect(host='localhost', user='root', passwd='root', database='contact_list_management')
    cur = mydb.cursor()
    keyword = input("Enter name, phone number, email, or address to search: ")
    keyword = f"%{keyword}%"
    cur.execute("SELECT name, phone, email, address FROM contacts WHERE name LIKE %s OR phone LIKE %s OR email LIKE %s OR address LIKE %s", (keyword, keyword, keyword, keyword))
    contacts = cur.fetchall()
    if not contacts:
        print("No contacts found.")
    else:
        print("Search Results:")
        print("--------------------------------------------")
        print("|   Name\t|   Phone\t|   Email\t|   Address   |")
        print("--------------------------------------------")
        for contact in contacts:
            print(f"|   {contact[0]}\t|   {contact[1]}\t|   {contact[2]}\t|   {contact[3]}   |")
        print("--------------------------------------------")
    mydb.close()

def update_contact():
    while True:
        print("1. Update Name")
        print("2. Update Phone Number")
        print("3. Update Email")
        print("4. Update Address")
        print("5. Return to Contact Management Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            update_contact_name()
        elif choice == '2':
            update_contact_number()
        elif choice == '3':
            update_contact_email()
        elif choice == '4':
            update_contact_address()
        elif choice == '5':
            return
        else:
            print("Invalid choice. Please try again.")

def contact_menu():
    while True:
        print("\nContact Management Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Return to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            display_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            return
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        print("\nMain Menu:")
        print("1. Setup Database")
        print("2. Setup Tables")
        print("3. Contact Management")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            db_setup()
        elif choice == '2':
            tb_setup()
        elif choice == '3':
            contact_menu()
        elif choice == '4':
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
