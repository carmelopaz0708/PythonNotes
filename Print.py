"""
PRINT FUNCTION

The PRINT function is a commonly used function in Python. PRINT outputs the variable or string written inside its (). Its primary use is in debugging programs, as print allows the
user to check the program's behaviour.
"""

print("\nExample 1:Print function")
print("The characters inside the \"\" or \'\' are printed to the console.")

print("\nExample 2: Newline")
print("Use \\n to print Strings in a new line.")

print("\nExample 3: Tabulation")
print("\tThis statement has been tabulated using \\t")

print("\nExample 4: Homogeneous variable concatenation (String variables only)")
print('This' + ' string' + ' is' + ' concatenated.')

print("\nExample 5: Mixed variable concatenation (integers and strings combined):")
var1 = 2    # Variable data types are automatically detected in Python
var2 = 3
sumVar = var1 + var2
print(var1, " + ", var2, " = ", sumVar)

print("\nExample 6: Print formatting")
# Organizes printing mixed variables
print("{} {} {}{}".format("You can print", "like this too and still look", 100, "%."))

print("\nExample 7: Escape characters")
print('The \ is an escape character that ignores the succeeding \', \" or \\. For example, \"this is a quote\".')

print("\nExample 8: Raw string")
# Add r before the "" or '' inside the print statement to print as raw string. Useful for printing directories like C:\Documents\Python
print(r"Raw string prints the statement whole and ignores special characters. \t, \n, \\ and others are ignored.")

print("\nExample 9: Data type")
# Using type() displays the variable's data type. Can be used with any variable
unknown1 = 12
unknown2 = 12.2
unknown3 = 'abc'
print(type(unknown1))
print(type(unknown2))
print(type(unknown3))
