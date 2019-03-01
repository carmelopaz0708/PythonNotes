"""
MATH
Python can perform various mathematical functions. The basic arithmetic operators (+, -, *, /, %) function the same as with any other programming language. Other math functions native only to Python include the exponent (**) and the floor division operator (//). The function type() is not a math function but a builtin Python function that outputs to the console the data type inside the (). This is a useful tool for debugging when you are unsure of what data type you're dealing with.

@auth siege
@rev 09/15/18
"""

# Initialize inputs
var1 = float(input("Enter a value: "))  # Input command, accepts only a float variable type
var2 = float(input("Enter a value: "))

# Type display
typ1Var = type(var1)
typ2Var = type(var2)

# Python math functions
sumVar = var1 + var2    # Addition, adds var1 to var2
difVar = var1 - var2    # Subtraction, minuses var2 from var1
mulVar = var1 * var2    # Multiplication, multiplies var1 with var2
divVar = var1 / var2    # Division, divides var1 by var2
modVar = var1 % var2    # Modulus, performs regular division but returns only the remainder
flrVar = var1 // var2   # Floor Division, performs regular division but removes the fractional part (mantissa)
expVar = var1 ** var2   # Exponent, raises var1 to the power of var2

# Print data type
print("\nvar1: ", typ1Var)
print("var2: ", typ2Var)

# Print math results
print(var1, ' + ', var2, ' = ', sumVar)
print(var1, ' - ', var2, ' = ', difVar)
print(var1, ' * ', var2, ' = ', mulVar)
print(var1, ' / ', var2, ' = ', divVar)
print(var1, ' % ', var2, ' = ', modVar)
print(var1, ' // ', var2, ' = ', flrVar)
print(var1, ' ** ', var2, ' = ', expVar)
