title = 'PASSWORD GENERATOR'
d = '--**************--'
x = title.center(80)
y = d.center(85)
print(x)
print(y)
import random
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
numbers="1234567890"
symbols="!@#*(),.\/"
length=int(input("Enter the Length of the password: "))
b = length // 4
c = length // 4
d = length // 4
e = length - (b + c + d)
part_a=""
password=""
for a in range(b):
    part_a+=random.choice(upper)
for a in range(c):
    part_a+=random.choice(lower)
for a in range(d):
    part_a+=random.choice(numbers)
for a in range(e):
    part_a+=random.choice(symbols)
f=len(part_a)
for a in range(f):
    password+=random.choice(part_a)
print(password)
