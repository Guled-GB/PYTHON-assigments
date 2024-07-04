import math

# Function to calculate area of a circle given radius
def calculate_area_of_circle(radius):
    return math.pi * (radius ** 2)

# Function to calculate circumference of a circle given radius
def calculate_circumference_of_circle(radius):
    return 2 * math.pi * radius

# Asking user for their information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

# Converting age to an integer
age = int(age)

# Printing the collected information
print("\n--- User Information ---")
print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)

# Comparing the lengths of first and last names
if len(first_name) > len(last_name):
    print("First name is longer than last name.")
elif len(first_name) < len(last_name):
    print("Last name is longer than first name.")
else:
    print("Both first and last names have the same length.")

# Performing arithmetic operations
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# Printing the results of arithmetic operations
print("\n--- Arithmetic Operations ---")
print("Sum:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponentiation:", exp)
print("Floor Division:", floor_division)

# Calculating and printing the area of a circle with radius 5
radius = 5
area_of_circle = calculate_area_of_circle(radius)
print("\n--- Circle Calculations ---")
print("Given radius:", radius)
print("Area of the circle:", area_of_circle)

# Calculating and printing the circumference of a circle with radius 5
circum_of_circle = calculate_circumference_of_circle(radius)
print("Circumference of the circle:", circum_of_circle)
