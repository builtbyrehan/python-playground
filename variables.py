# ==========================================
# Python Basics: Variables, Data Types,
# Input, Output & Type Conversion
# ==========================================


# ==========================================
# 1. VARIABLES
# ==========================================

name = "Rehan"
age = 20
height = 5.9
is_student = True

print(name)
print(age)
print(height)
print(is_student)


# Reassigning a variable
age = 21
print(age)


# ==========================================
# 2. DATA TYPES
# ==========================================

# String (str)
name = "Rehan"
print(name)
print(type(name))


# Integer (int)
age = 20
print(age)
print(type(age))


# Float (float)
height = 5.9
print(height)
print(type(height))


# Boolean (bool)
is_student = True
print(is_student)
print(type(is_student))


# ==========================================
# 3. PRINT STATEMENT
# ==========================================

print("Hello, World!")

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)


# ==========================================
# 4. USER INPUT
# ==========================================

name = input("Enter your name: ")

print("Hello,", name)


# ==========================================
# 5. INPUT RETURNS A STRING
# ==========================================

age = input("Enter your age: ")

print(age)
print(type(age))


# ==========================================
# 6. TYPE CONVERSION
# ==========================================

# String → Integer
age = input("Enter your age: ")
age = int(age)

print(age)
print(type(age))


# String → Float
height = input("Enter your height: ")
height = float(height)

print(height)
print(type(height))


# Integer → String
age = 20
age = str(age)

print(age)
print(type(age))


# ==========================================
# 7. CONVERTING INPUT DIRECTLY
# ==========================================

age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print("Age:", age)
print("Height:", height)


# ==========================================
# 8. PRACTICAL EXAMPLE
# ==========================================

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print("\n--- Student Profile ---")
print("Name:", name)
print("Age:", age)
print("Height:", height)