# Notes on "Automate the Boring Stuff with Python Programming"

## About

This project is a WIP based on [Automate the Boring Stuff with Python Programming](https://www.udemy.com/automate/) by Al Sweigart. This repository is intended to serve as a personal quick reference guide and not a full-fledged tutorial. For more in-depth coverage, please consult the cited Udemy course, or review the free e-book available [here](http://automatetheboringstuff.com/).

<div id='id-toc'/>

## Table of Contents

- Section 1: [Python Basics](#id-section1)
- Section 2: [Flow Control](#id-section2)
- Section 3: [Functions](#id-section3)
- Section 4: [Handling Errors with Try/Except](#id-section4)
- Section 6: [Lists](#id-section6)

<div id='id-section1'/>

## Section 1: Python Basics

### 1.2 - Basic Terminology and Using IDLE

#### Expressions

- Expressions consist of values and operators that reduce down to a single value (including combinations of numbers and strings), e.g.:

  ```python
  2 + 2                 # 4

  'Alice' + 'Bob'       # 'AliceBob'

  'Hello' + '!' * 10    # 'Hello!!!!!!!!!!'
  ```

#### Variables

- Declaring a variable:

  ```python
  spam = 'Hello'

  spam + ' World'   # Hello World
  ```

### 1.3 - Writing Our First Program

- Create a file named `file.py` containing the following code:

  ```python
  # This program says hello and asks for your name:

  print('What is your name?')
  myName = input()
  print('Nice to meet you, ' + myName)
  print('The length of your name is:')
  print(len(myName))
  print('What is your age?')
  myAge = input()
  print('You will be ' + str(int(myAge) + 1) + ' in a year.')
  ```

  - `print()` displays the contents (arguments) within its parentheses on the screen.

  - `input()` accepts the value of the user's keyboard input and returns a **string** value.

    - **NOTE:** The program will wait until the input is entered before continuing to execute the remaining code.

  - `len()` takes a string argument and evaluates to the integer value of the string's length:

    ```python
    len('Al')   # 2
    ```

  - `str()` takes an argument and converts it into a string data type:

    ```python
    str(42)     # '42'
    ```

  - `int()` takes an argument and converts it into an integer data type:

    ```python
    int('42')    # 42
    ```

    - **NOTE:** If you want to convert to a **floating point** number (i.e., a number with a decimal point) rather than an integer (i.e., a whole number), use `float()`:

      ```python
      float('3.14')   # 3.14
      ```

- **NOTE:** On OS X, you may need to run `python3` rather than `python` to run the current version of Python.

[Back to ToC](#id-toc)

<div id='id-section2'/>

## Section 2: Flow Control

### 2.4 - Flow Charts and Basic Flow Control Concepts

#### Booleans

- Booleans have two values: `True` and `False` (which **must** be capitalized).

#### Comparison Operators

  - Overview:

    | Operator    | Meaning                   |
    | :---------: | ------------------------- |
    | ==          | Equal to                  |
    | !=          | Not equal to              |
    | <           | Less than                 |
    | >           | Greater than              |
    | <=          | Less than or equal to     |
    | >=          | Greater than or equal to  |

  - Expressions with comparison operators evaluate to a Boolean value:

    ```python
    42 == 42      # True

    42 >= 100     # False

    # Integers and strings will never be equal to each other:

    42 == '42'    # False

    # However, floats and integers can be equal to each other:

    42.0 == 42    # True
    ```

#### Boolean Operators

  - Overview:

    ```python
    # The "and" operator returns true when all values are true:

    True and True     # True

    True and False    # False

    # The "or" operator returns true when at least one value is true:

    True or False     # True

    # The "not" operator evaluates to the opposite Boolean value:

    not True          # False
    ```

  - Example:

    ```python
    myAge = 26

    myPet = 'cat'

    myAge > 20 and myPet == 'cat'   # True
    ```

### 2.5 - If, Else, and Elif Statements

- Example:

  ```python
  # If the condition after the "if" statement is true, then the indented line
  # below the conditional statement will run, and the "else" block is skipped:

  if answer < 42:
    print('Too low')

  # If the preceding "if" statement (or "elif" statement) is false, then the
  # subsequent "elif" statement will be evaluated:

  elif answer > 42:
    print('Too high')

  # If all prior conditional statements are false, the "else" block will run:

  else:
    print('Correct')
  ```

  - **NOTE:** New "blocks" are designated by increasing indentation and begin only after statements that end with a colon (`:`).

- Python allows for "truthy" and "falsey" evaluations, e.g.:

  ```python
  print('Enter a name.')

  name = input()

  if name:
      print('Thank you for entering a name.')
  else:
      print('You did not enter a name.')
  ```

  - **TIP:** If you want to evaluate the truthiness of a value, execute the `bool()` function with the value passed in as an argument, e.g.:

    ```python
    bool(42)        # True

    bool(0)         # False

    bool('Hello')   # True

    bool('')        # False
    ```

### 2.6 - While Loops

- Examples:

  ```python
  # Prints "Hello, world." to the console five times:

  spam = 0

  while spam < 5:
      print('Hello, world.')
      spam = spam + 1

  # Requests input until user enters required string:

  name = ''

  while name != 'your name':
      print('Please type your name.')
      name = input()

  print('Thank you.')
  ```

- The `break` statement is used to break out of a loop (including an infinite loop), e.g.:

  ```python
  name = ''

  while True:
      print('Please type your name.')
      name = input()
      if name == 'your name':
          break

  print('Thank you.')
  ```

- The `continue` statement is used to return to the start of the loop and reevaluate the loop's condition:

  ```python
  # Prints 1, 2, 4, and 5.  Number 3 is not printed due to "continue":

  spam = 0

  while spam < 5:
      spam = spam + 1
      if spam == 3:
          continue
      print(spam)
  ```

### 2.7 - For Loops

- Example:

  ```python
  # The variable "i" is set to 0 on the first iteration, and its value is
  # printed to the console on each iteration.  The value of "i" increases
  # by 1 on each iteration up to (but not including) 5.  The iteration
  # process terminates once the value of "i" is set to 5:

  for i in range(5):
      print(i)
  ```

  - **NOTE:** If `range()` is given only **one** argument, then Python will generate a sequence of numbers starting at 0, and the stopping point will be the value of the argument (which must be an integer).  However, `range()` can accept up to three arguments (all of which must be integers):

    ```python
    # range([start], stop[, step])
    ```

    - `start`: Starting number of the sequence.
    - `stop`: Generate numbers up to (but not including) this number.
    - `step`: Difference between each number in the sequence.

- For loops are able to use `break` and `continue` statements in the same manner as while loops.

[Back to ToC](#id-toc)

<div id='id-section3'/>

## Section 3: Functions

### 3.8 - Python's Built-In Functions

#### Standard Library

- Python comes with a set of modules called the **[Standard Library](https://docs.python.org/3/library/)**.  Each module is a Python program that contains a related group of functions you can use in your programs (e.g., numeric and mathematical modules).  Before you can use the functions in a module, you must **import** the module with an `import` statement, e.g.:

  ```python
  # Returns a random integer from 1 to 10:

  import random

  random.randint(1, 10)
  ```

  - In the example above, `randint()` is a function within the `random` module.  You specify which function you want to use in a module by using dot notation.

- You can specify **multiple** modules for import by separating their names with **commas**, e.g.:

    ```python
    import random, sys, os, math
    ```

- It is generally considered best to use the syntax outlined above when using a function in a Standard Library module. However, if you want to import and call a function **directly** without needing to reference the module name each time, use the `from` form of an import statement, e.g.:

  ```python
  # Imports all functions from the "random" module, not the module itself:

  from random import *

  randint(1, 10)
  ```

- **TIP:** To terminate a program early, use the `exit()` function of the `sys` module, e.g.:

  ```python
  # Terminates after printing "Hello":

  import sys

  print('Hello')
  sys.exit()
  print('Goodbye')
  ```

#### Third-Party Modules

- Modules can be installed by using the `pip` (or `pip3`) tool from the terminal, e.g.:

  ```
  $ pip install ${MODULE_NAME}
  ```

  - **NOTE:** See [here](http://automatetheboringstuff.com/appendixa/) for more information on installing third-party modules.

- One noteworthy module is **[pyperclip](https://pypi.org/project/pyperclip/)** which allows you to copy and paste text to and from the clipboard, e.g.:

  ```python
  import pyperclip

  pyperclip.copy('The text to be copied to the clipboard.')
  pyperclip.paste()   # 'The text to be copied to the clipboard.'
  ```

### 3.9 - Writing Your Own Functions

- Define a function by using the `def` keyword, e.g.:

  ```python
  # Define a function called "hello()" that accepts a "name" parameter:

  def hello(name):
      print('Hello, ' + name)

  hello('Alice')      # "Hello, Alice"
  ```

- All function calls return a value.  You can specify what value should be returned by the function by using a `return` statement, e.g.:

  ```python
  def plusOne(number):
      return number + 1

  newNumber = plusOne(5)

  print(newNumber)    # 6
  ```

  - **NOTE:** If the value returned is considered "empty" (or if the return statement is omitted entirely), Python still returns a value called `None` (i.e., a value that represents a lack of a value).  The `None` value will not be visibly displayed in the console.

- Some functions accept **Keyword Arguments**, which are used as optional arguments to pass to a function call. For example, the `print()` function adds a newline character by default to the end of the string it prints. However, this behavior can be modified by changing the value of `end` keyword argument:

  ```python
  # Prints "Hello" and "World" on two separate lines:

  print('Hello')
  print('World')

  # Prints "Hello World" on one line:

  print('Hello', end=' ')
  print('World')
  ```

  - **NOTE:** The `print()` function also contains a `sep` keyword argument that specifies what character should be used to separate multiple arguments (an empty space by default), e.g.:

    ```python
    # Prints 'cat dog mouse':

    print('cat', 'dog', 'mouse')

    # Prints 'cat, dog, mouse':

    print('cat', 'dog', 'mouse', sep=', ')
    ```

### 3.10 - Global and Local Scopes

- Variables inside of a function can have the same name as variables outside of the function, but they are considered two separate variables due to scope.  Variables defined in a function belong to that function's **Local Scope**, whereas all variables defined outside of functions belong to the application's **Global Scope**, e.g.:

  ```python
  spam = 42       # Global variable

  def eggs():
      spam = 42   # Local variable
  ```

- Key Points:

  1.  Code in the global scope cannot use any local variables.

  2.  Code in a local scope can access global variables.

  3.  Code in one function's local scope cannot use variables in another local scope.

  4.  You can use the same name for different variables if they are in different scopes.

- If you want to reassign the value of a global variable (e.g. `eggs = 42`) from within a local scope, you cannot simply say `eggs = 'Hello'`, as this will merely create a local variable named "eggs" within the local scope. Rather, you must use a `global` statement, e.g.:

  ```python
  eggs = 42

  def spam():
      global eggs
      eggs = 'Hello'    # Overwrites 42 in global "eggs" variable
      print(eggs)       # Prints 'Hello'

  spam()

  print(eggs)           # Prints 'Hello'
  ```

[Back to ToC](#id-toc)

<div id='id-section4'/>

## Section 4: Handling Errors with Try/Except

### 4.11 - Try and Except Statements

- By default, a Python application will crash if an error occurs while executing code:

  ```python
  def div42by(divideBy):
    return 42 / divideBy

  print(div42by(2))     # 21.0
  print(div42by(0))     # (Will crash the application)
  print(div42by(21))    # (Will not be printed)
  ```

- In order to detect and handle errors while still allowing the program to run, you must use `try`/`except` statements:

  ```python
  def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

  print(div42by(2))     # 21.0
  print(div42by(0))     # 'Error: You tried to divide by zero.'
  print(div42by(21))    # 2.0
  ```

  - **NOTE:**  `ZeroDivisionError` is one of Python's [Built-in Exceptions](https://docs.python.org/2/library/exceptions.html). You can omit the exception type if you want Python to handle all errors via the code in the `except` block.

[Back to ToC](#id-toc)

<div id='id-section6'/>

## Section 6: Lists

### 6.13 - The List Data Type

- A **List** is a value containing sequential, comma-delimited items within square brackets.  To access items in a list, use an integer index for the item's position in the list (starting with 0):

  ```python
  spam = [['cat', 'bat', 'rat'], 'elephant']

  spam[0]           # ['cat', 'bat', 'rat']

  spam[1]           # 'elephant'

  spam[0][1]        # 'bat'

  # You can also access items in reverse order by using a negative integer,
  # with -1 starting as the last item in the list:

  spam[0][-1]       # 'rat'

  # An item's value can be reassigned by accessing the index:

  spam[0] = 'mouse'

  spam              # ['mouse', 'elephant']
  ```

- To view the **Length** of a list, use the `len()` function, e.g.:

  ```python
  spam = ['cat', 'bat', 'rat']

  len(spam)   # 3
  ```

- A **Slice** can access (not mutate) multiple items in a list by specifying the index at which the slice begins and the index at which the slice ends (non-inclusive), e.g.:

  ```python
  spam = ['cat', 'bat', 'rat']

  spam[0:2]   # ['cat', 'bat']

  # You can redefine multiple items in a list by using a slice:

  spam[1:3] = ['dog', 'fish']

  spam        # ['cat', 'dog', 'fish']
  ```

  - **TIP:** You can omit either number on each side of the colon. If you omit the number to the left of the colon, the slice will start at index 0 and end at the number to the right. If you omit the number to the right, the slice will start from the number on the left and end at the number that is the length of the list (allowing the slice to include the last item in the list), e.g.:

    ```python
    spam = ['cat', 'bat', 'rat']

    spam[:2]   # ['cat', 'bat']
    ```

- To **Delete** items from a list, use the `del` statement, e.g.:

  ```python
  spam = ['cat', 'bat', 'elephant', 'rat']

  del spam[2]

  spam    # ['cat', 'bat', 'rat']
  ```

- To **Concatenate** lists, use the `+` or `*` operators, e.g.:

  ```python
  [1, 2, 3] + [4, 5, 6]   # [1, 2, 3, 4, 5, 6]

  [1, 2, 3] * 3           # [1, 2, 3, 1, 2, 3, 1, 2, 3]
  ```

- To **Convert** another iterable data type (e.g., a string) into a list, use the `list()` function, e.g.:

  ```python
  list('hello')   # ['h', 'e', 'l', 'l', 'o']
  ```

- To determine whether an item is **Contained** in a list, you can use the `in` and `not in` operators, e.g.:

  ```python
  'elephant' in ['cat', 'bat', 'rat']       # False

  'elephant' not in ['cat', 'bat', 'rat']   # True
  ```

[Back to ToC](#id-toc)
