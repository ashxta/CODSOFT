title = 'PASSWORD GENERATOR'
d = '--**************--'
x = title.center(80)
y = d.center(85)
print(x)
print(y)
import random

def generate_password(length):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    symbols = "!@#*(),./\""
    
    b = length // 4
    c = length // 4
    d = length // 4
    e = length - (b + c + d)
    
    part_a = ""
    password = ""
    
    for a in range(b):
        part_a += random.choice(upper)
    for a in range(c):
        part_a += random.choice(lower)
    for a in range(d):
        part_a += random.choice(numbers)
    for a in range(e):
        part_a += random.choice(symbols)
    
    f = len(part_a)
    for a in range(f):
        password += random.choice(part_a)
    
    return password

def main():
    while True:
        try:
            length = int(input("Enter the Length of the password: "))
            password = generate_password(length)
            print("Generated Password:", password)
            
            while True:
                generate_another = input("Do you want to generate another password? (yes/no): ").lower()
                if generate_another in ('yes', 'y'):
                    break  
                elif generate_another in ('no', 'n'):
                    print("Exiting the password generator. Goodbye!")
                    return 
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
