title = 'TO DO LIST'
d = '--**************--'
x = title.center(80)
y = d.center(85)
print(x)
print(y)

import mysql.connector as con
def is_valid_date(day, month, year):
    # Check if the day, month, and year form a valid date
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            max_day = 29
        else:
            max_day = 28
    else:
        return False
    
    if 1 <= day <= max_day:
        return True
    else:
        return False

def db_setup():
    mydb = con.connect(host='localhost', user='root', password='root')
    cur = mydb.cursor()
    try:
        cur.execute('create database if not exists to_do_list')
        print("Database created")
    except:
        print("Database to_do_list already exists")
    mydb.close()

def tb_setup():
    mydb = con.connect(host='localhost', user='root', password='root', database='to_do_list')
    cur = mydb.cursor()
    try:
        cur.execute('create table if not exists task(task_id int primary key, task_name varchar(80), task_start varchar(20), task_deadline varchar(20), task_progress varchar(80), task_status varchar(10))')
        print("To-Do list Table setup done")
    except:
        print("Tables already exist")
    mydb.close()

def database_setup():
    while True:
        print("\npress 1 to setup database")
        print("Press 2 to setup tables")
        print("Press 3 to go back main menu\n")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            db_setup()
        elif ch == 2:
            tb_setup()
        elif ch == 3:
            return
        else:
            exit()

def add_task():
    mydb = con.connect(host='localhost', user='root', password='root', database='to_do_list')
    cur = mydb.cursor()
    
    task_id = int(input('Enter task id: '))
    task_name = input('Enter task name: ')
    
    # Input for start date
    day_input = int(input("Enter start day (1-31): "))
    month_input = int(input("Enter start month (1-12): "))
    year_input = int(input("Enter start year : "))
    if not (1 <= day_input <= 31):
        print("Invalid day number.")
        exit()
    if not (1 <= month_input <= 12):
        print("Invalid month number.")
        exit()
    if not is_valid_date(day_input, month_input, year_input):
        print("Invalid date.")
        exit()
    task_start = f"{day_input:02}/{month_input:02}/{str(year_input)[-2:]}"
    
    # Input for deadline
    day_input = int(input("Enter deadline day (1-31): "))
    month_input = int(input("Enter deadline month (1-12): "))
    year_input = int(input("Enter deadline year : "))
    if not (1 <= day_input <= 31):
        print("Invalid day number.")
        exit()
    if not (1 <= month_input <= 12):
        print("Invalid month number.")
        exit()
    if not is_valid_date(day_input, month_input, year_input):
        print("Invalid date.")
        exit()
    task_deadline = f"{day_input:02}/{month_input:02}/{str(year_input)[-2:]}"
    
    task_progress = input('Enter the progress of the task: ')
    task_status = input('Enter the status of the task [yes/no] : ')
    
    z = "insert into task values(%s, %s, %s, %s, %s, %s)"
    y = (task_id, task_name, task_start, task_deadline, task_progress, task_status)
    
    cur.execute(z, y)
    print("Task added successfully")
    
    mydb.commit()
    mydb.close()


def delete_task():
    mydb = con.connect(host='localhost', user='root', password='root', database='to_do_list')
    cur = mydb.cursor()
    
    task_id = int(input("Enter task id that you want to delete: "))
    z = "Delete from task where task_id = %s"
    y = (task_id,)
    
    cur.execute(z, y)
    if cur.rowcount <= 0:
        print("Enter the correct id")
    else:
        print(cur.rowcount, "Task successfully deleted")
    
    mydb.commit()
    mydb.close()

def update_task_name():
    mydb = con.connect(host='localhost', user='root', password='root', database='to_do_list')
    cur = mydb.cursor()
    
    task_id = int(input("Enter task id for which you want to update name: "))
    task_name = input("Enter updated task name: ")
    z = "update task set task_name = %s where task_id = %s"
    y = (task_name, task_id)
    
    cur.execute(z, y)
    if cur.rowcount <= 0:
        print("Enter the correct id")
    else:
        print(cur.rowcount, "Detail successfully updated")
    
    mydb.commit()
    mydb.close()

def update_task_start():
    mydb = con.connect(host='localhost', user='root', password='root', database='to_do_list')
    cur = mydb.cursor()
    
    task_id = int(input("Enter task id for which you want to update start date: "))
    
    # Input for start date
    day_input = int(input("Enter updated start day (1-31): "))
    month_input = int(input("Enter updated start month (1-12): "))
    year_input = int(input("Enter updated start year : "))
    if not (1 <= day_input <= 31):
        print("Invalid day number.")
        exit()
    if not (1 <= month_input <= 12):
        print("Invalid month number.")
        exit()
    if not is_valid_date(day_input, month_input, year_input):
        print("Invalid date.")
        exit()
    task_start = f"{day_input:02}/{month_input:02}/{str(year_input)[-2:]}"
    
    z = "update task set task_start = %s where task_id = %s"
    y = (task_start, task_id)
    
    cur.execute(z, y)
    if cur.rowcount <= 0:
        print("Enter the correct id")
    else:
        print(cur.rowcount, "Detail successfully updated")
    
    mydb.commit()
    mydb.close()

def update_task_deadline():
    mydb = con.connect(host='localhost', user='root', password='root', database='to_do_list')
    cur = mydb.cursor()
    
    task_id = int(input("Enter task id for which you want to update deadline: "))
    
    # Input for deadline
    day_input = int(input("Enter updated deadline day (1-31): "))
    month_input = int(input("Enter updated deadline month (1-12): "))
    year_input = int(input("Enter updated deadline year : "))
    if not (1 <= day_input <= 31):
        print("Invalid day number.")
        exit()
    if not (1 <= month_input <= 12):
        print("Invalid month number.")
        exit()
    if not is_valid_date(day_input, month_input, year_input):
        print("Invalid date.")
        exit()
    task_deadline = f"{day_input:02}/{month_input:02}/{str(year_input)[-2:]}"
    
    z = "update task set task_deadline = %s where task_id = %s"
    y = (task_deadline, task_id)
    
    cur.execute(z, y)
    if cur.rowcount <= 0:
        print("Enter the correct id")
    else:
        print(cur.rowcount, "Detail successfully updated")
    
    mydb.commit()
    mydb.close()


def update_task_progress():
    mydb = con.connect(host='localhost', user='root', password='root', database='to_do_list')
    cur = mydb.cursor()
    
    task_id = int(input("Enter task id for which you want to update progress: "))
    task_progress = input("Enter updated progress: ")
    z = "update task set task_progress = %s where task_id = %s"
    y = (task_progress, task_id)
    
    cur.execute(z, y)
    if cur.rowcount <= 0:
        print("Enter the correct id")
    else:
        print(cur.rowcount, "Detail successfully updated")
    
    mydb.commit()
    mydb.close()

def update_task_status():
    mydb = con.connect(host='localhost', user='root', password='root', database='to_do_list')
    cur = mydb.cursor()
    
    task_id = int(input("Enter task id for which you want to update status: "))
    task_status = input("Enter updated status: ")
    z = "update task set task_status = %s where task_id = %s"
    y = (task_status, task_id)
    
    cur.execute(z, y)
    if cur.rowcount <= 0:
        print("Enter the correct id")
    else:
        print(cur.rowcount, "Detail successfully updated")
    
    mydb.commit()
    mydb.close()

def display_task():
    mydb = con.connect(host='localhost', user='root', password='root', database='to_do_list')
    cur = mydb.cursor()
    while True:
        print('\nPress 1 to display all the records')
        print('Press 2 to display a certain task')
        print('Press 3 to return\n')
        nd = eval(input("Enter no.: "))
        if nd == 1:
            cur.execute("Select * from task")
            records = cur.fetchall()
            print('|TASK_ID|', '|     NAME   |',  '|   START   |', '|   DEADLINE   |', '|PROGRESS|', '|STATUS|')
            for i in records:
                print(i[0], '\t', i[1], '\t', i[2], '\t', i[3], '\t', i[4], '\t', i[5])
            print("Task list successfully displayed")
        elif nd == 2:
            task_id = eval(input("Enter the id of the task for which you want to see the data: "))
            y = (task_id,)
            z = "select * from task where task_id = %s"
            cur.execute(z, y)
            records = cur.fetchall()
            print('|TASK_ID|', '|NAME|', '|START|', '|DEADLINE|', '|PROGRESS|', '|STATUS|')
            for i in records:
                print(i[0], '\t', i[1], '\t', i[2], '\t', i[3], '\t', i[4], '\t', i[5])
            print("Task successfully displayed")
        elif nd == 3:
            return()
        else:
            print('Error, use the correct numbers')
    mydb.commit()
    mydb.close()

def task_menu():
    while True:
        print("Press 1 to add a task")
        print("Press 2 to delete a task")
        print("Press 3 to update the name of a task")
        print("Press 4 to update the start date of a task")
        print("Press 5 to update the deadline of a task")
        print("Press 6 to update the progress of a task")
        print("Press 7 to update the status of a task")
        print("Press 8 to display task data")
        print("Press 9 to go back main menu")
        
        ch = eval(input("Enter your choice: "))
        if ch == 1:
            add_task()
        elif ch == 2:
            delete_task()
        elif ch == 3:
            update_task_name()
        elif ch == 4:
            update_task_start()
        elif ch == 5:
            update_task_deadline()
        elif ch == 6:
            update_task_progress()
        elif ch == 7:
            update_task_status()
        elif ch == 8:
            display_task()
        elif ch == 9:
            return()
        else:
            exit()

def main():
    while True:
        print("\n\t\t\t PLEASE SELECT AN OPERATION \n")
        print("\t\t\t1. Press 1 to setup database")
        print("\t\t\t2. Press 2 to setup tables")
        print("\t\t\t3. Press 3 to perform operations on tasks")
        print("\t\t\t4. Press 4 to exit\n")
        ch = eval(input("Enter your choice: "))
        if ch == 1:
            db_setup()
        elif ch == 2:
            tb_setup()
        elif ch == 3:
            task_menu()
        elif ch == 4:
            exit()
        else:
            exit()

if __name__ == "__main__":
    main()


