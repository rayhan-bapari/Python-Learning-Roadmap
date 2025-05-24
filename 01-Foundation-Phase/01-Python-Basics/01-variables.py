name = "Md.Rayhan Bapari"
age = 27
height = 5.45
phone = None
has_job = True

# Print Results
print(name)
print(age)
print(height)
print(phone)
print(has_job)

# Types
print(type(name))
print(type(age))
print(type(height))
print(type(phone))
print(type(has_job))

# Assign Multiple Values
user_name, user_age, user_height = name, age, height
print(user_name)
print(user_age)
print(user_height)

# One Value to Multiple Variables
a = b = c = 'Test'
print(a)
print(b)
print(c)

# Unpack a Collection
user_info = [user_name, user_age, user_height]
print(user_info)

x, y, z = user_info
print(x)
print(y)
print(z)

# Global Variables
def userinfo():
    print('I am ' + str(user_info[1]) + ' Years Old')
userinfo()

def userinfo():
    global name
    name = input('What is your name? ')
    print('My Name is ' + name)
userinfo()