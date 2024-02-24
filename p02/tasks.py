# ---- 1
print('Variables')
number = 12
string = ' -string-  '
fraction = 45.33
print("Int: %d, Str: %s, Fraction number: %d" % (number, string, fraction))

str_number = str(number)
str_fraction = str(fraction)
print('Convert to string: ' + str_number + string + str_fraction)


# ---- 2
print('Математичні операції')
x = 10
y = 7
print('\nx=%d, y=%d' % (x, y))
print('Додавання x+y: ', x + y)
print('Віднімання x-y: ', x - y)
print('Множення x*y: ', x * y)
print('Ділення: x/y', x / y)
print('Підняття до степеня x^y: ', x ** y)
print('Цілочисельне ділення x//y: ', x // y)
print('Остача від цілочисельного ділення x%y: ', x % y)

# int float str
n = int(input('Введіть число '))
f = float(input('Введіть число '))

s1 = str(12345)
print('Рядок: ' + s1)


# ---- 3
# Write a Python program that calculates the area of a circle based on the radius entered by the user.

pi = 3.1415
r = float(input("Input the radius of the circle : "))
# Calculate the area of the circle using the formula: area = π * r^2
area = pi * r ** 2
# Display the result, including the radius and calculated area
print("The area of the circle with radius " + str(r) + " is: " + str(area))

# ---- 4
# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

# Prompt the user to input an integer and store it in the variable 'a'
a = int(input("Input an integer: "))
# Create new integers 'n1', 'n2', and 'n3' by concatenating 'a' with itself one, two, and three times, respectively
n1 = int("%s" % a)          # Convert 'a' to an integer
n2 = int("%s%s" % (a, a))   # Concatenate 'a' with itself and convert to an integer
n3 = int("%s%s%s" % (a, a, a))  # Concatenate 'a' with itself twice and convert to an integer
# Calculate the sum of 'n1', 'n2', and 'n3' and print the result
print(n1 + n2 + n3)

# ---- 6
# Write a Python program to get the volume of a sphere with radius.
# The volume of the sphere is : V = 4/3 × π × r^3. = π × d^3 / 6.
# Define the value of pi
pi = 3.1415926535897931
# Define the radius of the sphere
r = 6.0
# Calculate the volume of the sphere using the formula
V = 4.0/3.0 * pi * r**3
# Print the calculated volume of the sphere
print('The volume of the sphere is: ', V)

# ---- 6
# Знайти суму усіх парних і непраних чисел в діапазоні від (а) до (б)



# ---- a.1
# Write a Python program to find out what version of Python you are using.

# import sys  # Import the sys module to access system-specific parameters and functions
# Print the Python version to the console
# print("Python version")
# Use the sys.version attribute to get the Python version and print it
# print(sys.version)
# Print information about the Python version
# print("Version info.")
# Use the sys.version_info attribute to get detailed version information and print it
# print(sys.version_info)


# ---- a.2
# Write a Python program to display the current date and time.

# Import the 'datetime' module to work with date and time
# import datetime
# Get the current date and time
# now = datetime.datetime.now()
# Create a datetime object representing the current date and time
# Display a message indicating what is being printed
# print("Current date and time : ")
# Print the current date and time in a specific format
# print(now.strftime("%Y-%m-%d %H:%M:%S"))
# Use the 'strftime' method to format the datetime object as a string with the desired format

# ---- a.3
# Write a Python program that prints the calendar for a given month and year.
# Import the 'calendar' module
# import calendar
# Prompt the user to input the year and month
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# Print the calendar for the specified year and month
# print(calendar.month(y, m))