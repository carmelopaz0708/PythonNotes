"""
PRINT FUNCTION
  The PRINT function is a commonly used function in Python. PRINT outputs the variable or string written inside its (). Its primary use is in debugging programs, as print allows the
user to check the program's behaviour.
  Special characters can be used inside "". These are escape characters (such as \' and \") and special characters (such as \t, \n, etc.) The description is listed below:
  \' - Ignores the preceeding '
  \" - Ignores the preceeding "
  \t - Tabulation, indents the string
  \r - Carriage Return, places the cursor back to home
  \n - Newline Character, generates a newline with carriage return
  \b - Backspace, generates a backspace
  \a - Alarm, generates an alarm sound (only if hardware enabled)

@auth siege
@init 02/28/19
"""

print("\nExample 1:Print function")
print("This string is printed to the console")

print("\nExample 2: String Concatenation")
# The '+' sign is used to join two strings together. The * is used to print a string multiple times.
print("This whole string is made up of " + "two different strings that were concatenated.")
print("This string is printed three times. " * 3)

print("\nExample 3: Mixed Variable Concatenation: ")
# Concatenating a string and a number uses the comma operator. This results in a string.
# Note that the same result can also be obtained via print formatting
var1 = 2    # Variable data types are automatically detected in Python (no need to initialize type data)
var2 = 3
sumVar = var1 + var2
print(var1, " + ", var2, " = ", sumVar)

print("\nExample 4: Print Formatting")
# This is a cleaner way to format your print statements. Works with strings, numbers and mixed types.
# The curly brace becomes the string placeholder. Statements inside the format will be printed in order.
print("{} {} {}{}".format("You can print", "like this too and still look", 100, "%."))

print("\nExample 5: Raw string")
# Raw string prints the string as a whole, ignoring special and escape characters. This is useful for printing file directories and addresses.
# To print a raw string, attach an r before the string inside the print function.
print(r"Raw string prints the statement whole and ignores special characters. \t, \n, \\ and others are ignored.")
