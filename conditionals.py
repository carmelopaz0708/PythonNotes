"""
CONDITIONAL STATEMENTS
  Conditional statements enable programs to make decisions. These are blocks of code that perform specific tasks when a certain condition is satisfied. These tasks can either perform
once or multiple times(recursion), depending on the type of conditional statement used. Conditional statements are very powerful and proper utilization of these lines of codes can
drastically decrease code memory, allowing for faster processes.

@siege
@init 12/13/18
"""

print("\nExample 1: The if-elif-else statement")
# If-elif-else performs code under its branch when a certain condition is met. It is run only once.
# You can only have one if block and one else block. elif blocks can be appended multiple times in the code
var1 = float(input("Enter you're grade: "))
if var1 > 100:
  print("Something's fishy.")
elif var1 == 100:
  print("You perfected the subject!")
elif 90 <= var1 < 100:
  print("You passed with flying colors!")
elif 80 <= var1 < 90:
  print("You did well")
elif 75 <= var1 < 80:
  print("You're OK")
else:
  print("You need to read the books more")

print("\nExample 2: The while loop")
# Executes a given set of code as long as the given condition is true. Set a counter inside the for loop or else the code will run forever and crash the system. Note that while
# loops behave differently in other programming languages (e.g. Java, C++, etc.) and use a different kinds of syntax. In some cases, they have better functionality as compared to
# Python.
i = 1
var2 = float(input("Enter a number from 1 to 10: "))
if 1 <= var2 <= 10:
  while i <= var2:
    print("This statement has been printed", i, "times!")
    i += 1
elif var2 < 0:
  print("Out of bounds!")
elif var2 > 10:
  print("Out of bounds!")

print("\nExample 3: The for loop")
# Used explicitly in iteration and recursion in a sequence(e.g. list, tuple, dictionary, set or string). Functions the same as the while loop. Note that for loops behave
# differently in other programming languages (e.g. Java, C++, etc.) and use a different kinds of syntax. In some cases, they have better functionality in other languages as
# compared to Python.
var3 = ["eggs", "butter", "cream", "milk", "sugar"]
for i in var3:
  print("You are going to buy", i)

var4 = input("\nEnter a string: ")
j = 0
for i in var4:
  print("The letter", i, "is in index", j, "of the input statement.")
  j += 1
