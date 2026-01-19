# Task 2: Variables, Data Types & Type Conversion

# Declaring variables of different data types
integer_var = 10
float_var = 25.5
string_var = "Python"
boolean_var = True

# Printing values and their types
print("Integer value:", integer_var, "Type:", type(integer_var))
print("Float value:", float_var, "Type:", type(float_var))
print("String value:", string_var, "Type:", type(string_var))
print("Boolean value:", boolean_var, "Type:", type(boolean_var))

print("\n--- Arithmetic Operations ---")
# Arithmetic operations
sum_result = integer_var + float_var
product_result = integer_var * float_var

print("Sum:", sum_result)
print("Product:", product_result)

print("\n--- Type Conversion ---")
# Taking user input
user_input = input("Enter a number: ")

try:
    int_value = int(user_input)
    float_value = float(user_input)

    print("Integer conversion:", int_value)
    print("Float conversion:", float_value)

except ValueError:
    print("Invalid input! Please enter a numeric value.")

print("\n--- String Concatenation ---")
# Concatenating string and number
age = 21
print("My age is " + str(age))

print("\n--- Dynamic Typing Demonstration ---")
# Dynamic typing example
var = 100
print("Value:", var, "Type:", type(var))

var = "Now I am a string"
print("Value:", var, "Type:", type(var))
