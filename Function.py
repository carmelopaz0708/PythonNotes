"""
FUNCTIONS

Functions are a useful tool in Python. Simply put, functions separate blocks of code inside your program. These partitions perform a specific task and are separate from the rest unless called (function call). By creating functions, you're effectively isolating processes from each other and dedicate resources onto one function without affecting the others. Functions also make your code readable, understandable and easier to debug by human coders, since we can study one part of the program without analyzing the program as a whole. Functions become of much greater use for longer programs where processes become more complicated.

@auth siege
@rev 02/28/19
"""

def main():
    print("\nExample 1: User Defined Function")
    print("This is a main function.")
    print("This would normally be the program entry point, but any function be used as an entry point in Python")
    # Other languages such as Java and C rely on a main() function as an entry point. This isn't required in Python but its good practice to have one.


def function2(var_func2):
    # This is an example of a function doing a specific tasks in a program. Longer programs would be easier to follow given a systematic use of functions.
    # This function takes input var1_func2 and uses it inside the scope of function2(). The value of var_func2 is parsed from outside the function using the corresponding function call.
    # The input to a function doesn't necesarily have to be a string, it could be a variable or a constant as well
    print("\nExample 2: Input to function 01")
    print(var_func2)


def function3(var_func3):
    print("\nExample 3: Input to function 02")
    print(var_func3)


def function4(var_func4):
    print("\nExample 4: Input to function 03")
    print(var_func4)
    
    
def function5():
    print("\nExample 5: Using a return statement")
    # If you want to use the the variable obtained from a function, use a return statement.
    var1 = int(input("Enter base: "))
    var2 = int(input("Enter exp: "))
    power = var1 ** var2
    return power
    

def function6(var3):
    # The returned value from function6() is used by function7()
    print("The answer is ", var3)


def function7():
    print("\nExample 6: Dedicated function")
    # This function accepts user input and outputs it to the console. The process happens only in function5()
    name = input("What is your name? ")
    thumbs = int(input("How many opposable thumbs do you have? "))
    print("\nHello {}, nice to meet you!".format(name))
    print("If you have", thumbs, "opposable thumbs then I have", thumbs * 2, "more!")


# User algorithm
main()
# function2() parses a string as an input. Other data types can be parsed directly into a function as an input
function2("The input to var_func2 was taken from the syntax \'function2(args)\' where args is this sentence.")
statement = "This statement was created globally but was called to use by a function."
function3(statement)    # function3() parses a variable created outside of the function. Other functions can use that variable as well.           
function4(statement.upper())    # function4() parses the same variable but only this time, is attached with a constructor. This is also possible
x = function5() # The value returned from function6() is assigned to x
function6(x)    # The variable x is now parsed into the function7()
function7()     # function5() doesn't pass any input in it cause all the inputs are created when running the function (and are subsequently lost after use)
