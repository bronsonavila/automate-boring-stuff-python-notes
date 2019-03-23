# Notes on "Automate the Boring Stuff with Python Programming"

## About

This repository is derived from the lectures covered in [Automate the Boring Stuff with Python Programming](https://www.udemy.com/automate/) by Al Sweigart. This repository is intended to serve as a personal quick reference guide and not a full-fledged tutorial. For more in-depth coverage, please consult the cited Udemy course, or review the free e-book available [here](http://automatetheboringstuff.com/).

<div id='id-toc'/>

## Table of Contents

- Section 1: [Python Basics](#id-section1)
- Section 2: [Flow Control](#id-section2)
- Section 3: [Functions](#id-section3)
- Section 4: [Handling Errors with Try/Except](#id-section4)
- Section 6: [Lists](#id-section6)
- Section 7: [Dictionaries](#id-section7)
- Section 8: [More About Strings](#id-section8)
- Section 9: [Running Programs from the Command Line](#id-section9)
- Section 10: [Regular Expressions](#id-section10)
- Section 11: [Files](#id-section11)
- Section 12: [Debugging](#id-section12)
- Section 13: [Web Scraping](#id-section13)
- Section 14: [Excel, Word, and PDF Documents](#id-section14)
- Section 15: [Email](#id-section15)
- Section 16: [GUI Automation](#id-section16)

<div id='id-section1'/>

## Section 1: Python Basics

### 1.2 - Basic Terminology and Using IDLE

#### Expressions

- Expressions consist of values and operators that reduce down to a single value (including combinations of numbers and strings):

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

[Back to TOC](#id-toc)

<div id='id-section2'/>

## Section 2: Flow Control

### 2.4 - Flow Charts and Basic Flow Control Concepts

#### Booleans

- Booleans have two values: `True` and `False` (which **must** be capitalized).

#### Comparison Operators

- Overview:

  | Operator | Meaning                  |
  | :------: | ------------------------ |
  |    ==    | Equal to                 |
  |    !=    | Not equal to             |
  |    <     | Less than                |
  |    >     | Greater than             |
  |    <=    | Less than or equal to    |
  |    >=    | Greater than or equal to |

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

- Python allows for "truthy" and "falsey" evaluations:

  ```python
  print('Enter a name.')

  name = input()

  if name:
      print('Thank you for entering a name.')
  else:
      print('You did not enter a name.')
  ```

  - **TIP:** If you want to evaluate the truthiness of a value, execute the `bool()` function with the value passed in as an argument:

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

- The `break` statement is used to break out of a loop (including an infinite loop):

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

  - **NOTE:** If `range()` is given only **one** argument, then Python will generate a sequence of numbers starting at 0 (as a range object data type, which is a list-like value known as a "sequence"), and the stopping point will be the value of the argument (which must be an integer). However, `range()` can accept up to three arguments (all of which must be integers):

    ```python
    # range([start], stop[, step])
    ```

    - `start`: Starting number of the sequence.
    - `stop`: Generate numbers up to (but not including) this number.
    - `step`: Difference between each number in the sequence.

- For loops are able to use `break` and `continue` statements in the same manner as while loops.

[Back to TOC](#id-toc)

<div id='id-section3'/>

## Section 3: Functions

### 3.8 - Python's Built-In Functions

#### Standard Library

- Python comes with a set of modules called the **[Standard Library](https://docs.python.org/3/library/)**. Each module is a Python program that contains a related group of functions you can use in your programs (e.g., numeric and mathematical modules). Before you can use the functions in a module, you must **import** the module with an `import` statement:

  ```python
  # Returns a random integer from 1 to 10:

  import random

  random.randint(1, 10)
  ```

  - In the example above, `randint()` is a function within the `random` module. You specify which function you want to use in a module by using dot notation.

- You can specify **multiple** modules for import by separating their names with **commas**:

  ```python
  import random, sys, os, math
  ```

- It is generally considered best to use the syntax outlined above when using a function in a Standard Library module. However, if you want to import and call a function **directly** without needing to reference the module name each time, use the `from` form of an import statement:

  ```python
  # Imports all functions from the "random" module, not the module itself:

  from random import *

  randint(1, 10)
  ```

- **TIP:** To terminate a program early, use the `exit()` function of the `sys` module:

  ```python
  # Terminates after printing "Hello":

  import sys

  print('Hello')
  sys.exit()
  print('Goodbye')
  ```

#### Third-Party Modules

- Modules can be installed by using the `pip` (or `pip3`) tool from the terminal:

  ```
  $ pip install ${MODULE_NAME}
  ```

  - **NOTE:** See [here](http://automatetheboringstuff.com/appendixa/) for more information on installing third-party modules.

- One noteworthy module is **[pyperclip](https://pypi.org/project/pyperclip/)** which allows you to copy and paste text to and from the clipboard:

  ```python
  import pyperclip

  pyperclip.copy('The text to be copied to the clipboard.')
  pyperclip.paste()   # 'The text to be copied to the clipboard.'
  ```

### 3.9 - Writing Your Own Functions

- Define a function by using the `def` keyword:

  ```python
  # Define a function called "hello()" that accepts a "name" parameter:

  def hello(name):
      print('Hello, ' + name)

  hello('Alice')      # "Hello, Alice"
  ```

- All function calls return a value. You can specify what value should be returned by the function by using a `return` statement:

  ```python
  def plusOne(number):
      return number + 1

  newNumber = plusOne(5)

  print(newNumber)    # 6
  ```

  - **NOTE:** If the value returned is considered "empty" (or if the return statement is omitted entirely), Python still returns a value called `None` (i.e., a value that represents a lack of a value). The `None` value will not be visibly displayed in the console.

- Some functions accept **keyword arguments**, which are used as optional arguments to pass to a function call. For example, the `print()` function adds a newline character by default to the end of the string it prints. However, this behavior can be modified by changing the value of `end` keyword argument:

  ```python
  # Prints "Hello" and "World" on two separate lines:

  print('Hello')
  print('World')

  # Prints "Hello World" on one line:

  print('Hello', end=' ')
  print('World')
  ```

  - **NOTE:** The `print()` function also contains a `sep` keyword argument that specifies what character should be used to separate multiple arguments (an empty space by default):

    ```python
    # Prints 'cat dog mouse':

    print('cat', 'dog', 'mouse')

    # Prints 'cat, dog, mouse':

    print('cat', 'dog', 'mouse', sep=', ')
    ```

### 3.10 - Global and Local Scopes

- Variables inside of a function can have the same name as variables outside of the function, but they are considered two separate variables due to scope. Variables defined in a function belong to that function's **local scope**, whereas all variables defined outside of functions belong to the application's **global scope**:

  ```python
  spam = 42       # Global variable

  def eggs():
      spam = 42   # Local variable
  ```

- Key Points:

  **1**\.  Code in the global scope cannot use any local variables.

  **2**\.  Code in a local scope can access global variables.

  **3**\.  Code in one function's local scope cannot use variables in another local scope.

  **4**\.  You can use the same name for different variables if they are in different scopes.

- If you want to reassign the value of a global variable (e.g. `eggs = 42`) from within a local scope, you cannot simply say `eggs = 'Hello'`, as this will merely create a local variable named "eggs" within the local scope. Rather, you must use a `global` statement:

  ```python
  eggs = 42

  def spam():
      global eggs
      eggs = 'Hello'    # Overwrites 42 in global "eggs" variable
      print(eggs)       # Prints 'Hello'

  spam()

  print(eggs)           # Prints 'Hello'
  ```

[Back to TOC](#id-toc)

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

  - **NOTE:** `ZeroDivisionError` is one of Python's [Built-in Exceptions](https://docs.python.org/2/library/exceptions.html). You can omit the exception type if you want Python to handle all errors via the code in the `except` block.

[Back to TOC](#id-toc)

<div id='id-section6'/>

## Section 6: Lists

### 6.13 - The List Data Type

- A **list** is a value containing sequential, comma-delimited items within square brackets. To access items in a list, use an integer index for the item's position in the list (starting with 0):

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

- To view the **length** of a list, use the `len()` function:

  ```python
  spam = ['cat', 'bat', 'rat']

  len(spam)   # 3
  ```

- A **slice** can access (not mutate) multiple items in a list by specifying the index at which the slice begins and the index at which the slice ends (non-inclusive):

  ```python
  spam = ['cat', 'bat', 'rat']

  spam[0:2]   # ['cat', 'bat']

  # You can redefine multiple items in a list by using a slice:

  spam[1:3] = ['dog', 'fish']

  spam        # ['cat', 'dog', 'fish']
  ```

  - **TIP:** You can omit either number on each side of the colon. If you omit the number to the left of the colon, the slice will start at index 0 and end at the number to the right. If you omit the number to the right, the slice will start from the number on the left and end at the number that is the length of the list (allowing the slice to include the last item in the list):

    ```python
    spam = ['cat', 'bat', 'rat']

    spam[:2]   # ['cat', 'bat']
    ```

- To **delete** items from a list, use the `del` statement:

  ```python
  spam = ['cat', 'bat', 'elephant', 'rat']

  del spam[2]

  spam    # ['cat', 'bat', 'rat']
  ```

- To **concatenate** lists, use the `+` or `*` operators:

  ```python
  [1, 2, 3] + [4, 5, 6]   # [1, 2, 3, 4, 5, 6]

  [1, 2, 3] * 3           # [1, 2, 3, 1, 2, 3, 1, 2, 3]
  ```

- To **convert** another iterable data type (e.g., a string) into a list, use the `list()` function:

  ```python
  list('hello')   # ['h', 'e', 'l', 'l', 'o']
  ```

- To determine whether an item is **contained** in a list, you can use the `in` and `not in` operators:

  ```python
  'elephant' in ['cat', 'bat', 'rat']       # False

  'elephant' not in ['cat', 'bat', 'rat']   # True
  ```

### 6.14 - For Loops with Lists, Multiple Assignment, and Augmented Operators

- A list can be iterated over in a for loop in the same manner as a `range` object:

  ```python
  # Both loops produce the same output:

  for i in range(4):
      print(i)

  for i in [0, 1, 2, 3]:
      print(i)
  ```

  - **TIP:** The ability to transform a `range` object into a list allows for you to take advantage of the `range()` function's step parameter:

    ```python
    # Prints all even numbers from 0 to 98:

    list(range(0, 100, 2))
    ```

  - **TIP:** You can access both the index and value of each item while iterating over a list by using the `range()` and `len()` functions:

    ```python
    supplies = ['pens', 'staplers', 'binders']

    for i in range(len(supplies)):
        print ('Index ' + str(i) + ' in supplies is: ' + supplies[i])

    # Index 0 in supplies is: pens
    # Index 1 in supplies is: staplers
    # Index 2 in supplies is: binders
    ```

- You can use Python's **multiple assignments** feature to iterate over a list and assign each item's value to a variable:

  ```python
  cat = ['fat', 'orange', 'loud']

  size, color, disposition = cat

  size          # 'fat'
  color         # 'orange'
  disposition   # 'loud'
  ```

  - **NOTE:** Multiple assignments work not only with lists, but also comma-delineated values outside of a list:

    ```python
    size, color, disposition = 'slim', 'gray', 'quiet'
    ```

  - **TIP:** Multiple assignments are also useful for quick variable swapping:

    ```python
    a = 'AAA'
    b = 'BBB'

    a, b = b, a

    a   # 'BBB'
    b   # 'AAA'
    ```

- **Augmented Operators** (`+=`, `-=`, `*=`, `/=`, `%=`):

  ```python
  spam  = 42

  spam = spam + 1

  spam += 1

  spam    # 44
  ```

### 6.15 - List Methods

- The `index()` method returns the index of the first occurrence of the specified value:

  ```python
  spam = ['hello', 'hi', 'howdy', 'hi']

  spam.index('hi')    # 1

  spam.index('hey')   # (Raises an exception if value not found)
  ```

- The `append()` method appends an item to the end of the list:

  ```python
  spam = ['cat', 'dog', 'bat']

  spam.append('moose')

  spam[3]   # 'moose'
  ```

- The `insert()` method inserts the specified value at the specified position:

  ```python
  spam = ['cat', 'dog', 'bat']

  spam.insert(1, 'chicken')

  spam    # ['cat', 'chicken', 'dog', 'bat']
  ```

- The `remove()` method removes the first occurrence of the item with the specified value:

  ```python
  spam = ['cat', 'bat', 'elephant', 'rat']

  spam.remove('elephant')

  spam                  # ['cat', 'bat', 'rat']

  spam.remove('oat')    # (Throws an error)
  ```

- The `sort()` method sorts a list in ascending order by default. The sorting direction can be reversed by using the `reverse` keyword argument:

  ```python
  spam = [2, 5, 3.14, 1, -7]

  spam.sort()

  spam    # [-7, 1, 2, 3.14, 5]

  spam = ['ants', 'cats', 'badgers']

  spam.sort()

  spam    # ['ants', 'badgers', 'cats']

  spam.sort(reverse=True)

  spam    # ['cats', 'badgers', 'ants']
  ```

  - **NOTE:** You cannot sort an array that contains both number and string types.

  - **ALSO:** When working with strings, `sort()` actually sorts by "**ASCII-betical**" order rather than alphabetical order (resulting in uppercase letters being sorted before lowercase letters, because uppercase letters appears before lowercase letters in ASCII code). However, you can sort by true alphabetical order by using the `key` keyword argument:

    ```python
    spam = ['a', 'z', 'A', 'Z']

    spam.sort()

    spam    # ['A', 'Z', 'a', 'z']

    # str.lower is a string method that converts a string input to lowercase:

    spam.sort(key=str.lower)

    spam    # ['A', 'a', 'Z', 'z']
    ```

### 6.16 - Similarities Between Lists and Strings

- A string is essentially a list of single character strings (which is why `list()` can accept a string as an argument). However, they are significantly different in the sense that a list is a **mutable** data type (i.e., it can have values added, moved, or changed), whereas a string is an **immutable** data type (i.e., its value cannot be changed). Because strings are immutable, the proper way to create a new string derived from an existing variable is by using **slices**:

  ```python
  name = 'Zophie a cat'

  newName = name[0:7] + 'the' + name[8:12]

  newName   # 'Zophie the cat'
  ```

- When a list is assigned to a variable, Python actually stores a **reference** to the list in memory, not the actual list itself. Thus, if a list is referenced in two separate variables, a modification to one variable will affect the value stored in the other variable as well:

  ```python
  spam = [0, 1, 2, 3, 4, 5]

  cheese = spam

  cheese[1] = 'Hello'

  cheese    # [0, 'Hello', 2, 3, 4, 5]

  spam      # [0, 'Hello', 2, 3, 4, 5]
  ```

- If you want to make a true copy of a list (rather than having two or more variables point to the same list by reference), use the `copy` module's `deepcopy()` function:

  ```python
  import copy

  spam = ['A', 'B', 'C', 'D']

  # Creates a list with items identical to (but separate from) those in "spam":

  cheese = copy.deepcopy(spam)
  ```

- When working within lists, Python is aware that instances of **line continuation** should not be considered a new block:

  ```python
  spam = ['apples',
          'oranges',
          'bananas']
  ```

  - **TIP:** You can take advantage of line continuation even without a list by using the line continuation character (`\`):

    ```python
    print('Four score and seven ' + \
          'years ago...')

    # 'Four score and seven years ago...'
    ```

[Back to TOC](#id-toc)

<div id='id-section7'/>

## Section 7: Dictionaries

### 7.17 - The Dictionary Data Type

- A dictionary is a mutable collection of key-value pairs:

  ```python
  myCat = {'size': 'large', 'color': 'gray', 'disposition': 'loud'}

  myCat['size']         # 'large'

  myCat['age']          # (Results in a KeyError message)

  # Check if a key exists with the "in" and "not in" operators:

  'name' in myCat       # False

  'name' not in myCat   # True
  ```

- Two dictionaries with identical key-value pairs will be considered equivalent regardless of the order in which those key-value pairs are arranged:

  ```python
  eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
  ham = {'species': 'cat', 'age': 8, 'name': 'Zophie'}

  eggs == ham   # True
  ```

- Three major dictionary iteration methods (`keys()`, `values()`, `items()`):

  ```python
  eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}

  # Each method returns a list-like data type, so you must convert each result
  # with the "list()" function if you want to receive a true list value:

  list(eggs.keys())     # ['name', 'species', 'age']

  list(eggs.values())   # ['Zophie', 'cat', 8]

  # Tuples are the same as lists, expect they use parentheses (not brackets):

  list(eggs.items())    # [('name, 'Zophie'), ('species', 'cat'), ('age', 8)]
  ```

- You can iterate over a dictionary's keys/values with a for loop:

  ```python
  eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}

  # Prints 'name', 'species', and 'age':

  for k in eggs.keys():
      print(k)

  # Prints 'name: Zophie', 'species: cat', and 'age: 8'

  for k, v in eggs.items():
      print(k + ': ' + str(v))
  ```

- If you attempt to retrieve a value from a key that does not exist in a dictionary, you will normally receive an error. However, you can avoid such problems by using the `get()` method to specify a default value if the key does not exist:

  ```python
  eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}

  eggs.get('age', 0)       # 8

  eggs.get('color', '')    # ''
  ```

- If you want to set a value for a key that does not yet exist in a dictionary, use the `setdefault()` method:

  ```python
  eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}

  eggs.setdefault('color', 'black')     # 'black'

  # No change if the key already exists:

  eggs.setdefault('color', 'orange')    # 'black'
  ```

- To obtain a **pretty print** of a dictionary (or list), use the `pprint` module:

  ```python
  import pprint

  message = 'All cows eat grass'

  count = {}

  for character in message:
      count.setdefault(character.lower(), 0)
      count[character.lower()] += 1

  pprint.pprint(count)

  # {' ': 3,
  #  'a': 3,
  #  'c': 1,
  #  'e': 1,
  #  'g': 1,
  #  'l': 2,
  #  'o': 1,
  #  'r': 1,
  #  's': 3,
  #  't': 1,
  #  'w': 1}
  ```

  - **TIP:** If you want to store your `pprint` object as a **string** (rather than merely print it to the screen), use the `pprint` module's `pformat()` method instead.

### 7.18 - Data Structures

- You can use the `type()` function to determine the data type of any value:

  ```python
  type(42)                    # <class 'int'>

  type('hello')               # <class 'str'>

  type({'name': 'Zophie'})    # <class 'dict'>
  ```

[Back to TOC](#id-toc)

<div id='id-section8'/>

## Section 8: More About Strings

### 8.19 - Advanced String Syntax

- There are multiple ways to type strings, including via double quotes and escape characters:

  ```python
  "That is Alice's cat."

  # Prints 'Say hello to Bob's mother.':

  print('Say hello to Bob\'s mother.')

  # Prints each statement on a new line:

  print('Hello.\nHow are you?\nI\'m fine.')
  ```

- Types of escape characters:

  | Escape character | Prints as            |
  | :--------------: | -------------------- |
  | \\'               | Single quote         |
  | \\"               | Double quote         |
  | \t               | Tab                  |
  | \n               | Newline (line break) |
  | \\\              | Backslash            |

- If you have text that contains many backslashes that you do not want to be treated as escape characters, you can use a **raw string**, which is a string that begins with a lowercase "r":

  ```python
  # Prints without the letters "t" and "n", and inserts tab and newline characters instead:

  print('C:\temp\new')

  # Prints text as written:

  print(r'C:\temp\new')
  ```

- Although you can use `\n` to add newlines to a string, it is often easier to use **multiline strings** with triple quotes (either single or double quotes). Any quotes, tabs, or newlines within the triple quotes are considered part of the string:

  ```python
  spam = """Dear Alice,
  Eve's cat is orange.
  Sincerely,
  Bob"""

  print(spam)     # (Prints each line on a new line)

  spam            # "Dear Alice,\nEve's cat is orange.\nSincerely,\nBob"
  ```

### 8.20 - String Methods

- The `upper()` and `lower()` methods return a string where all characters are in uppercase or lowercase, respectively:

  ```python
  spam = 'Hello, world!'

  spam.upper()    # 'HELLO, WORLD!'

  spam.lower()    # 'hello, world!'
  ```

  - **NOTE:** Because strings are immutable, string methods do not modify the original string. If you want to actually modify the string value stored to a variable, you must say, e.g.: `spam = spam.lower()`

- The `isupper()` and `islower()` methods return a Boolean value indicating whether all letters in the string are uppercase or lowercase, respectively:

  ```python
  spam = 'hello, world!'

  spam.isupper()    # False

  spam.islower()    # True
  ```

  - Other noteworthy string methods beginning with the word `is`:

    ```python
    isalpha()     # (Letters only)

    isalnum()     # (Letters and numbers only)

    isdecimal()   # (Numbers only)

    isspace()     # (Whitespace only)

    istitle()     # (Titlecase only)
    ```

  - **NOTE:** Because string methods return a new string, you are able to **chain** method calls:

    ```python
    'hello'.upper().isupper()   # True
    ```

- The `startswith()` and `endswith()` methods return a Boolean value indicating whether the string starts with or ends with (respectively) the specified value:

  ```python
  spam = 'Hello, world!'

  spam.startswith('Hello')   # True

  spam.endswith('!')         # True

  spam.endswith('world')     # False

- The `join()` method takes all items in an iterable and joins them into one string using a specified separator:

  ```python
  spam = ['cats', 'rats', 'bats']

  ', '.join(spam)   # 'cats, rats, bats'

  '\n'.join(spam)   # (Inserts newline character after each item)
  ```

- The `split()` method splits a string into a list. The method splits a string according to whitespace separation by default; however, you can specify the string to be used as the separator (first parameter) and the number of splits to perform (second parameter):

  ```python
  spam = 'My name is Simon'

  spam.split()          # ['My', 'name', 'is', 'Simon']

  spam.split('m')       # ['My na', 'e is Si', 'on']

  spam.split(None, 1)   # ['My', 'name is Simon']
  ```

- The `ljust()` and `rjust()` methods return a "padded" version of a string with a number of spaces (first parameter) inserted to left or right justify (respectively) the specified text. An optional second parameter can be used to specify a padding character other than a space. There is also a `center()` method that operates similarly to `ljust()` and `rjust()` but uses padding to center the text, rather than justify left or right:

  ```python
  'Hello'.ljust(10)         # 'Hello     '

  'Hello'.rjust(10)         # '     Hello'

  'Hello'.ljust(10, '.')    # 'Hello.....'

  'Hello'.center(15, '-')   # '-----Hello-----'
  ```
- Use the `strip()`, `rstrip()`, and `lstrip()` methods to trim whitespace characters off of a string. You can insert a string as an argument, and any contiguous set of characters in that argument (regardless of order) will be stripped from the end(s) of the string:

  ```python
  '  -x-  '.strip()                       # 'x'

  '  -x-  '.lstrip()                      # 'x   '

  '  -x-  '.rstrip()                      # '   x'

  'SpamBaconSpamEggsSpam'.strip('ampS')   # 'BaconSpamEggs'
  ```

- The `replace()` methods replaces a specified phrase with another specified phrase:

  ```python
  'Hello there!'.replace('e', '3')    # 'H3llo th3r3!'
  ```

### 8.21 - String Formatting

- Rather than concatenating numerous strings with the `+` operator, you can use Python's **string formatting** (a.k.a., string interpolation) by using the `%` operator and the `%s` symbol (one of several types of conversion specifiers):

  ```python
  name = 'Alice'
  place = 'Main Street'
  time = '6:00 PM'
  food = 'turnips'

  'Hello, %s. You are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food)

  # 'Hello, Alice. You are invited to a party at Main Street at 6:00 PM. Please bring turnips.'
  ```

[Back to TOC](#id-toc)

<div id='id-section9'/>

## Section 9: Running Programs from the Command Line

- See [Appendix B](https://automatetheboringstuff.com/appendixb/) re: shebang line (`#! /usr/bin/env python3`) and changing file permissions (`chmod +x pythonScript.py`)

- To use arguments from the command line in your Python script, use the `sys.argv` list:

  ```python
  #! /usr/bin/env python3

  import sys

  print(sys.argv)
  ```

[Back to TOC](#id-toc)

<div id='id-section10'/>

## Section 10: Regular Expressions

### 10.23 - Regular Expression Basics

- Example of using regular expressions with the `re` module:

  ```python
  import re

  message = 'Call me tomorrow at 415-555-1011, or at 415-555-9999.'

  # "compile()" compiles a regex pattern into a regex object that can be used
  # for matching via "match()", "search()", and other methods.  "\d" is the
  # regex for a numeric digit character:

  phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

  # The regex data type has a "search()" method that can be used to search a
  # string for the regex pattern and return a match object containing the first
  # matching string:

  matchObject = phoneNumRegex.search(message)

  # Match objects have a method called "group()" that will return the text
  # of the matching string:

  print(matchObject.group())    # 415-555-1011
  ```

  - **NOTE:** If the `search()` method does not find a match, it will return a value of `None`, which will cause an error to result if you call the `group()` method on a nonexistent match object.

### 10.24 - Regex Groups and the Pipe Character

- Use **parentheses** to mark out groups within a regex, and access groups via the `group()` method:

  ```python
  import re

  phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

  matchObject = phoneNumRegex.search('My number is 415-555-4242.')

  matchObject.group(1)    # '415'

  matchObject.group(2)    # '555-4242'
  ```

  - **NOTE:** If you want to find literal parentheses (or any other regex special characters) within your text, then you must escape the opening and closing parentheses with a backslash (`\`):

    ```python
    phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
    ```

- Use the **pipe** (`|`) character to match one of many possible groups (based on, e.g., prefix/suffix):

  ```python
  batRegex = re.compile(r'Bat(man|mobile|copter)')

  matchObject = batRegex.search('Batmobile lost a wheel')

  matchObject.group()     # 'Batmobile'

  matchObject.group(1)    # 'mobile'
  ```

### 10.25 - Repetition in Regex Patterns and Greedy/Nongreedy Matching

- The `?` character matches the preceding expression **0 or 1** time (i.e., the expression can either appear once or not at all for a match to occur):

  ```python
  import re

  # Matches 'Batman' or 'Batwoman':

  batRegex = re.compile(r'Bat(wo)?man')
  ```

- The `*` character matches the preceding expression **0 or more** times:

  ```python
  batRegex = re.compile(r'Bat(wo)*man')

  matchObject = batRegex.search('The Adventures of Batwowowoman')

  matchObject.group()   # 'Batwowowoman'
  ```

- The `+` character matches the preceding expression **1 or more** times:

  ```python
  # Matches 'Batwoman' or 'Batwowowoman', etc., but not 'Batman':

  batRegex = re.compile(r'Bat(wo)+man')
  ```

- The `{`*`n`*`}` character matches **exactly** *n* occurrences of the preceding expression:

  ```python
  haRegex = re.compile(r'(ha){3}')

  matchObject = haRegex.search('He said, "hahaha"')

  matchObject.group()   # 'hahaha'
  ```

- The `{`*`n,m`*`}` character matches at least *n* and at most *m* occurrences of the preceding expression (if *n* is omitted, it is treated as 0; if *m* is omitted, it is treated as ∞):

  ```python
  haRegex = re.compile(r'(ha){3,5}')

  haMatchObject = haRegex.search('He said, "hahahaha"')

  haMatchObject.group()       # 'hahahaha'

  # By default, Python will perform a "greedy" match and return the longest
  # possible match that it finds (in this case, 5 digits rather than 3):

  digitRegex = re.compile(r'(\d){3,5}')

  digitMatchObject = digitRegex.search('1234567890')

  digitMatchObject.group()    # '12345'

  # To perform a "nongreedy" match, use the "?" character after the curly brace:

  digitRegex = re.compile(r'(\d){3,5}?')

  digitMatchObject = digitRegex.search('1234567890')

  digitMatchObject.group()    # '123'
  ```

### 10.26 - Regex Character Classes and the findall() Method

#### findall() Method

- If you want to return **every** occurrence of a regex pattern (rather than only the first), then use the `findall()` method (instead of `search()`) to return a list containing all matches:

  ```python
  import re

  message = 'Call me tomorrow at 415-555-1011, or at 415-555-9999.'

  phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

  print(phoneNumRegex.findall(message))   # ['415-555-1011', '415-555-9999']
  ```

- Be mindful of how **groups** affect the value returned by the `findall()` method:

  ```python
  message = 'Call me tomorrow at 415-555-1011, or at 415-555-9999.'

  # One group:

  single = re.compile(r'(\d\d\d)-\d\d\d-\d\d\d\d')

  single.findall(message)   # ['415', '415']

  # Two groups:

  tuples = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

  tuples.findall(message)   # [('415', '555-1011'), ('415', '555-9999')]

  # Two groups nested within one group:

  nested = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')

  nested.findall(message)   # [('415-555-1011', '415', '555-1011'),
                            # ('415-555-9999', '415', '555-9999')]
  ```

#### Character Classes

- Common Character Classes:

  | Shorthand character class | Represents                                                          |
  | :-----------------------: | ------------------------------------------------------------------- |
  | \d                        | Any numeric digit from 0 to 9                                       |
  | \D                        | Any character that is *not* a numeric digit from 0 to 9             |
  | \w                        | Any letter, numeric digit, or underscore (i.e., "word" characters)  |
  | \W                        | Any character that is *not* a letter, numeric digit, or underscore  |
  | \s                        | Any space, tab, or newline character (i.e., "space" characters)     |
  | \S                        | Any character that is *not* a space, tab, or newline                |

- Example:

  ```python
  lyrics = """12 drummers drumming, 11 pipers piping, 10 lords a leaping,
              9 ladies dancing, 8 maids a milking, 7 swans a swimming,
              6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens,
              2 turtle doves, 1 partridge in a pear tree"""

  xmasRegex = re.compile(r'\d+\s\w+')

  xmasRegex.findall(lyrics)   # ['12 drummers', '11 pipers', '10 lords',
                              # '9 ladies', '8 maids', '7 swans',
                              # '6 geese', '5 golden', '4 calling',
                              # '3 french', '2 turtle', '1 partridge']
  ```

- You can create your own regex **character sets** (e.g., `[xyz]`) and **negated or complemented character sets** (e.g., `[^xyz]`):

  ```python
  message = 'Robocop eats baby food.'

  # Matches all letters:

  alphaRegex = re.compile(r'[a-zA-Z]')

  alphaRegex.findall(message)         # ['R', 'o', 'b', 'o', 'c', 'o', 'p',
                                      # 'e', 'a', 't', 's', 'b', 'a', 'b', 'y',
                                      # 'f', 'o', 'o', 'd']

  # Matches all vowels:

  vowelRegex = re.compile(r'[aeiouAEIOU]')

  vowelRegex.findall(message)         # ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']

  # Matches all vowels appearing in sets of 2:

  doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')

  doubleVowelRegex.findall(message)   # ['ea', 'oo']

  # Matches anything that is NOT enclosed in the brackets:

  nonVowelRegex = re.compile(r'[^aeiouAEIOU]')

  nonVowelRegex.findall(message)      # ['R', 'b', 'c', 'p', ' ', 't', 's', ' ',
                                      # 'b', 'b', 'y', ' ', 'f', 'd', '.']
  ```

### 10.27 - Regex Dot-Star and the Caret/Dollar Characters

- Use the `^` character (not as a first character in a character set) to find a match at the **beginning** of an input, and use the `$` character to find a match at the **end** of an input:

  ```python
  import re

  # Begins with 'Hello':

  beginsWithHelloRegex = re.compile(r'^Hello')

  beginsWithHelloRegex.findall('Hello there!')        # ['Hello']

  beginsWithHelloRegex.findall('He said, "Hello".')   # []

  # Ends with 'world':

  endsWithWorldRegex = re.compile(r'world$')

  endsWithWorldRegex.findall('Hello, world')          # ['world!']

  endsWithWorldRegex.findall('Hello, world!')         # []

  # Only contains one or more numeric digits:

  allDigitsRegex = re.compile(r'^\d+$')

  allDigitsRegex.findall('1234567890')                # ['1234567890']

  allDigitsRegex.findall('12345x7890')                # []
  ```

- The `.` (dot) character matches **any** character except the newline character:

  ```python
  message = 'The cat in the hat sat on the flat mat.'

  # Matches a phrase that ends in 'at' preceded by 1-2 non-newline characters:

  atRegex = re.compile(r'.{1,2}at')

  # Includes spaces:

  atRegex.findall(message)    # [' cat', ' hat', ' sat', 'flat', ' mat']
  ```

  - **NOTE:** To make `.` truly match **every** character (even newlines), pass the `re.DOTALL` variable as the second argument in the `compile()` function:

    ```python
    primeDirectives = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'

    dotStar = re.compile(r'.*', re.DOTALL)

    matchObject = dotStar.search(primeDirectives)

    print(matchObject.group())    # Serve the public trust.
                                  # Protect the innocent.
                                  # Uphold the law.
    ```

  - **ALSO:** If you want to have a **case-insensitive** regex match, use the `re.IGNORECASE` variable:

    ```python
    # TIP: You can also use "re.I" as a shorthand for "re.IGNORECASE':

    vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE)

    vowelRegex.findall('All cows eat grass.')    # ['A', 'o', 'e', 'a', 'a']
    ```

- Common way to match anything is the **Dot-Star** pattern:

  ```python
  text = 'First Name: Al Last Name: Sweigart'

  nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')

  nameRegex.findall(text)   # [('Al', 'Sweigart')]
  ```

  - **NOTE:** Dot-Star uses greedy mode by default, so you must use `(.*?)` for nongreedy matching:

    ```python
    serve = '<To serve humans> for dinner.>'

    # Nongreedy matching:

    nongreedy = re.compile(r'<(.*?)>')

    nongreedy.findall(serve)    # ['To serve humans']

    # Greedy matching:

    greedy = re.compile(r'<(.*)>')

    greedy.findall(serve)       # ['To serve humans> for dinner.']
    ```

### 10.28 - Regex sub() Method and Verbose Mode

#### sub() Method

- The `sub()` method allows you to find matching text and replace it with new text:

  ```python
  import re

  message = 'Agent Alice gave documents to Agent Bob.'

  namesRegex = re.compile(r'Agent \w+')

  # The first argument is the replacement string, and
  # the second argument is the string to be searched:

  namesRegex.sub('REDACTED', message)   # 'REDACTED gave documents to REDACTED.'
  ```

- You can retain portions of the original text by using the **Slash-Number** syntax (e.g., `\1`, `\2`, etc.), in which the number represents a group in the regex pattern:

  ```python
  message = 'Agent Alice gave documents to Agent Bob.'

  # The group will contain the first letter of an agent's name:

  namesRegex = re.compile(r'Agent (\w)\w*')

  namesRegex.findall(message)   # ['A', 'B']

  # Use the text from "Group 1" for the substituted match:

  namesRegex.sub(r'Agent \1', message)   # 'Agent A gave documents to Agent B.'
  ```

#### Verbose Mode

- The `re.VERBOSE` flag allows you to write regular expressions that look nicer and are more readable by allowing you to visually separate logical sections of the pattern and add comments. Whitespace within the pattern is generally ignored:

  ```python
  message = 'Call me tomorrow at 415-555-1011, or at (415) 555-9999.'

  # TIP: You can combine "compile()" options by using the bitwise "|" operator:

  phoneRegex = re.compile(r'''
  (((\d\d\d-)|      # Area code (without parentheses; with dash)
  (\(\d\d\d\)\s))   # -OR- Area code (with parentheses; without dash)
  \d\d\d            # First 3 digits
  -                 # Second dash
  \d\d\d\d)         # Last 4 digits
  ''', re.VERBOSE | re.I | re.DOTALL)   # Added extra options for demonstration

  phoneRegex.findall(message)[0][0]     # '415-555-1011'

  phoneRegex.findall(message)[1][0]     # '(415) 555-9999'
  ```

[Back to TOC](#id-toc)

<div id='id-section11'/>

## Section 11: Files

### 11.30 - Filenames and Absolute/Relative File Paths

- File paths are handled differently with regard to slashes/backslashes on Windows (e.g., `C:\temp\new`) and Mac/Linux (e.g., `C:/temp/new`). To enforce consistency when creating a file path string in Python, use the `os` module's `path.join()` method:

  ```python
  import os

  # Returns 'folder1\\folder2\\file.png' if run on Windows, and
  # returns 'folder1/folder2/file.png' if run on Mac/Linux:

  os.path.join('folder1', 'folder2', 'file.png')
  ```

- To retrieve the string value of the file's **current working directory** (CWD), use the `os.getcwd()` method. You can manually change what Python considers the CWD to be by using `os.chdir()`:

  ```python
  os.getcwd()   # '/Users/Guest/Desktop'

  oc.chdir('/Users/Guest/Documents')

  os.getcwd()   # '/Users/Guest/Documents'
  ```

- Being able to modify the CWD is important for handling **relative file paths**. A file referenced by name only (e.g., `file.png`) will be considered to be within the CWD, whereas a file name that is part of an **absolute file path** (e.g., `/Users/Guest/Documents/file.png`) is known to be within the path specified.

  - **NOTE:** Relative file paths can also contain references to folders, not just file names.

- To return an absolute file path derived from a non-absolute pathname, use `os.path.abspath()`:

  ```python
  # Essentially calls "os.getcwd()" and appends the string argument:

  os.path.abspath('spam.png')       # '/Users/Guest/Documents/spam.png'

  # You can use the ".." symbol to move to a higher folder in the CWD:

  os.path.abspath('../spam.png')    # '/Users/Guest/spam.png'
  ```

  - **TIP:** You can determine whether a path is relative or absolute by using the `os.path.isabs()`, which returns a Boolean value:

    ```python
    os.path.isabs('../spam.png')              # False

    os.path.isabs('/Users/Guest/Documents')   # True
    ```

- To find the relative path between two paths, use `os.path.relpath()`. The first argument is the destination path, and the second (optional) argument is the starting path (which defaults to the current directory if not specified):

  ```python
  os.path.relpath('/Users/Guest/spam.png', '/Users')    # '/Guest/spam.png'
  ```

- Use `os.path.dirname()` to retrieve only the directory in which a file is located, and use `os.path.basename()` to retrieve only the endpoint of a path:

  ```python
  os.path.dirname('/Users/Guest/spam.png')    # '/Users/Guest'

  os.path.basename('/Users/Guest/spam.png')   # 'spam.png'

  os.path.basename('/Users/Guest')            # 'Guest'
  ```

- To determine whether a file or path exists, use `os.path.exists()`, which returns a Boolean value:

  ```python
  os.path.exists('/Users/Guest')    # True
  ```

  - **ALSO:** Use `os.path.isfile()` and `os.path.isdir()` to determine whether a path is referencing a file or directory, respectively (returns a Boolean value).

- Other useful functions for **examining/modifying** directories include `os.path.getsize()`, `os.listdir()`, and `os.makedirs()`:

  ```python
  # Returns a directory's or file's size in bytes (as an integer):

  os.path.getsize('/Users/Guest')   # 384

  # Returns the contents of a directory:

  os.listdir('/Users/Guest')

  # Creates a new folder (accepts either absolute or relative file paths):

  os.makedirs('/Users/Guest/Delicious/Waffles')
  ```

### 11.31 - Reading and Writing Plaintext Files

- Three steps to **reading** plaintext files:

  ```python
  # The `open()` function opens a plaintext file in "read mode" (default)
  # and returns a file object:

  helloFile = open('/Users/Guest/hello.txt')

  # The file object includes the "read()" method that returns a string
  # containing the file's contents:

  content = helloFile.read()

  # Close the file:

  helloFile.close()
  ```

  - **NOTE:** Instead of `read()`, you can use the `readlines()` method to return all lines as strings inside of a list. For example, if the file `hello.txt` contained the following text...

    ```
    Hello, world!
    How are you?
    ```

    ...then `read()` and `readlines()` will process the text accordingly:

    ```python
    helloFile.read()        # 'Hello, world!\nHow are you?'

    helloFile.readlines()   # ['Hello, world!\n', 'How are you?']
    ```

- To **write** to a plaintext file (i.e., overwrite its contents), pass the string `'w'` as the second argument to the `open()` function. To **append** new text to a file (i.e., add to the end of the file, rather than overwrite its contents), pass the `'a'` string. In either case, if the file does not already exist, then Python will create a new `txt` file for you to write to:

  ```python
  helloFile = open('/Users/Guest/hello2.txt', 'w')

  # Use the "write()" method to write:

  helloFile.write('Hello!!!\n')   # NOTE: Will return the number of bytes written

  helloFile.close()
  ```

  - **NOTE:** Python will *not* automatically add newline characters when writing/appending text content. So newlines must be added manually if desired.

- If you need to store **complex data** such as lists/dictionaries (rather than just plaintext) to your storage device, use the `shelve` module to create a **binary shelf file**:

  ```python
  import shelve

  # Returns a "shelf" data object that will be saved to your storage device
  # as a shelf file named "mydata" in the current working directory:

  shelfFile = shelve.open('mydata')

  # Make changes to the shelf file in the same manner as a dictionary:

  shelfFile['cats'] = ['Kiwi', 'Penny', 'Clover']

  shelfFile['dogs'] = ['Bambi', 'Buzz', 'Elway']

  # Close the file:

  shelfFile.close()
  ```

  - **NOTE:** On Mac OS X, the shelf file will be saved with the `.db` extension. Its contents can be accessed from a Python program as follows:

    ```python
    # NOTE: The "shelve.open()" method opens a shelf file in read-write mode:

    shelfFile = shelve.open('mydata')

    shelfFile['cats']           # ['Kiwi', 'Penny', 'Clover']

    # List all keys in a shelf file:

    list(shelfFile.keys())      # ['cats', 'dogs']

    # List all values in a shelf file:

    list(shelfFile.values())    # [['Kiwi', 'Penny', 'Clover'],
                                # ['Bambi', 'Buzz', 'Elway']]
    ```

### 11.32 - Copying and Moving Files and Folders

- The `shutil` (Shell Utilities) module allows you to copy and move files and folders:

  ```python
  import shutil

  # COPY a file (first argument) to a new folder (second argument):

  shutil.copy('/Users/Guest/hello.txt', '/Users/Guest/Delicious')

  # COPY and RENAME a file to a new folder ('/Delicious.txt'):

  shutil.copy('/Users/Guest/hello.txt', '/Users/Guest/Delicious/spam.txt')

  # COPY an entire FOLDER:

  shutil.copytree('/Users/Guest/Delicious', '/Users/Guest/Delicious_Backup')

  # MOVE a file to a new location:

  shutil.move('/Users/Guest/Delicious/spam.txt', '/Users/Guest/Waffles')

  # MOVE and RENAME a file to a new location:

  shutil.move('/Users/Guest/Delicious/spam.txt', '/Users/Guest/hello.txt')
  ```

  - **NOTE:** `shutil` does not have a method dedicated to renaming a file without copying/moving the file; however, you can accomplish the same result by using the `move()` method and setting the destination path to be the same as the original filepath:

    ```python
    shutil.move('/Users/Guest/hello.txt', '/Users/Guest/eggs.txt')
    ```

### 11.33 - Deleting Files

- The `os` module has an `unlink()` method that can be used for permanently deleting a **single file**, and a `rmdir()` for permanently deleting an **empty folder**:

  ```python
  import os

  # Deletes a file:

  os.unlink('/Users/Guest/Delicious/eggs.txt')

  # Deletes an empty folder:

  os.unlink('/Users/Guest/Delicious')
  ```

- To permanently remove a folder and all of its contents, use the `shutil.rmtree()` method:

  ```python
  import shutil

  shutil.rmtree('/Users/Guest/Waffles')
  ```

- A better practice is to send a file/folder to your OS's **trash** or **recycling bin** (rather than permanently deleting the file/folder) by using the [send2trash](https://pypi.org/project/Send2Trash/) third-party module:

  ```python
  import send2trash

  send2trash.send2trash('/Users/Guest/Delicious/eggs.txt')
  ```

### 11.34 - Walking a Directory Tree

- The `os.walk()` method allows you to iterate through and execute code upon all of the files or folders within a specified folder:

  ```python
  import os

  for folderName, subfolders, filenames in os.walk('/Users/Guest'):
      # Delete subfolders containing the string 'fish' in the subfolder name:
      for subfolder in subfolders:
          if 'fish' in subfolder:
              os.rmdir(subfolder)

      # Copy all ".py" files to ".backup" files:
      for file in filenames:
          if file.endswith('.py'):
              shutil.copy(
                  os.path.join(folderName, file),
                  os.path.join(folderName, file + '.backup')
              )
  ```

[Back to TOC](#id-toc)

<div id='id-section12'/>

## Section 12: Debugging

### 12.35 - The raise and assert Statements

- Python automatically raises one of its built-in **exceptions** whenever it tries to run invalid code; however, you can also raise your own exceptions with a `raise` statement. A **traceback** will be logged upon raising the exception, which allows you to see the specific line of code that triggered the exception:

  ```python
  raise Exception('This is the error message.)
  ```

  - **TIP:** To save a running log of cleanly formatted error messages (as strings), use the `traceback.format_exc()` module:

    ```python
    import traceback

    try:
        raise Exception('This is the error message.')
    except:
        errorFile = open('error-log.txt', 'a')
        errorFile.write(traceback.format_exc())
        efforFile.close()
        print('The traceback info was written to error-log.txt')
    ```

- An **assertion** can be used to perform a "sanity check". They are intended to address programmer errors rather than user errors. See the following example of a traffic light simulator:

  ```python
  mainStreet = {'ns': 'green', 'ew': 'red'}


  def switchLights(intersection):
      for key in intersection.keys():
          if intersection[key] == 'green':
              intersection[key] == 'yellow'
          elif intersection[key] == 'yellow':
              intersection[key] == 'red'
          elif intersection[key] == 'red':
              intersection[key] == 'green'
      # This program will raise an exception when the assertion fails by returning
      # 'False' on the second run, in which the N/S light will be 'yellow' and the
      # E/W light will be 'green'. As traffic should only be flowing when one
      # light on the intersection is 'red', the assert statement allows you to
      # immediately detect the problem and take corrective action:
      assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)


  switchLights(mainStreet)
  ```

### 12.36 - Logging

- Python's `logging` module allows you to create a record of custom messages. Use the `logging.basicConfig()` method to display log messages on your screen while the program runs:

  ```python
  import logging

  # The following line should appear at or near the top of your program:

  logging.basicConfig(
      level=logging.DEBUG,
      format='%(asctime)s - %(levelname)s - %(message)s'
  )

  # Each of the following "debug()" function calls work like "print()" but
  # provide additional information (i.e., timestamp, log level, and custom message):

  logging.debug('Start of program')

  def factorial(n):
      logging.debug('Start of factorial(%s)' % (n))
      total = 1
      for i in range(n + 1):
          total *= i
          logging.debug('i is %s, total is %s' % (i, total))
      logging.debug('Return value is %s' % (total))
      return total

  print(factorial(5))   # (Returns 0, which is incorrect)

  logging.debug('End of program')

  # In this example, the running log will show that "i" is set to 0 on the first
  # iteration, which results in "total" being set to 0 because any amount
  # times 0 is always equal to 0. Therefore, by reviewing the log, it becomes
  # apparent that the "range()" value should be set to start at 1 rather than 0.
  ```

- To **disable** logging messages that are present in your code, use the `logging.disable()` method at the top of your code:

  ```python
  # Disables logging calls of the given severity level (or lower):

  logging.disable(logging.CRITICAL)
  ```

  - **NOTE:** Python recognizes the following 5 [logging levels](https://docs.python.org/3/library/logging.html#levels) (in descending order of severity). Log messages can be created at a specific log level by using the corresponding logging method:

    | Log level | Logging method       |
    | --------- | -------------------- |
    | CRITICAL  | `logging.critical()` |
    | ERROR     | `logging.error()`    |
    | WARNING   | `logging.warning()`  |
    | INFO      | `logging.info()`     |
    | DEBUG     | `logging.debug()`    |

- To log messages to a **plaintext file** rather than the screen, use the `filename` keyword argument in the `logging.basicConfig()` method:

  ```python
  logging.basicConfig(
      filename='myProgramLog.txt'   # (Relative pathname)
      level=logging.DEBUG,
      format='%(asctime)s - %(levelname)s - %(message)s'
  )
  ```

### 12.37 - Using the Debugger

- The debugger is a feature in IDLE that allows you to run your program one line at a time. To activate the deubgger:

  **1**\.  Go to `Debug > Debugger` in the IDLE menu bar.

  **2**\.  Ensure that the `Stack`, `Source`, `Locals`, and `Globals` checkboxes are all checked (to show the most information).

  **3**\.  Run your program with the debugger enabled. The execution should pause on the first line.

- Use the following controls to navigate through your code with the dugger:

  - `Over` ("Step Over") executes the line of code that appears highlighted in the shell, and then proceeds to execute the next line (basically allows you to execute a single line of code at a time).

    - **NOTE:** During this process, any variables that are set or modified will be displayed in the `Locals` and `Globals` boxes.

  - `Go` runs the program normally and disables the debugger until reaching (1) the end of the program or (2) a **breakpoint**.

    - To set a breakpoint in IDLE's file editor, right click the line at which you want to set a breakpoint and click `Set Breakpoint`.

  - `Step` ("Step Into") moves the debugger inside of a function call (if a function is about to be executed).

  - `Out` ("Step Out") will keep executing lines within the current function until the function returns.

[Back to TOC](#id-toc)

<div id='id-section13'/>

## Section 13: Web Scraping

### 13.38 - The webbrowser Module

- The `webbrowser` module's `open()` function launches a new browser to a specified URL:

  ```python
  import webbrowser

  webbrowser.open('https://automatetheboringstuff.com')
  ```

### 13.39 - Downloading from the Web with the requests Module

- The [requests](https://requests.readthedocs.io/en/master/) module is a third-party module that allows you to send HTTP/1.1 requests.

  ```python
  import requests

  # "get()" returns a response object received from the server:

  res = requests.get('http://nunit.org/nuget/nunit3-license.txt')

  res.status_code   # (Displays the response status code, e.g., 200)

  res.text          # (Displays the body of the text content)

  # "raise_for_status()" will raise an exception if a download error occurred:

  res.raise_for_status()

  # To save the file to your storage device, use then "open()" function in
  # Write-Binary mode by passing "wb" as the second argument. (NOTE: Even if the
  # downloaded page is in plaintext, you must still write binary data--rather
  # than plaintext data--in order to maintain the Unicode encoding of the text):

  licenseFile = open('license.txt', 'wb')

  # Write the file by using a for loop with the "iter_content()" method. Files
  # are written in "chunks" (of the "bytes" data type), and you can specify the
  # size of each chunk via the "chunk_size" keyword argument (first parameter).
  # (NOTE: Per the "requests" documentation, 128 is the recommended size when
  # streaming a download; however, this value may be modified as necessary):

  for chunk in res.iter_content(128):
      licenseFile.write(chunk)    # (Will return an integer of bytes written)

  licenseFile.close()
  ```

    - **NOTE:** See [here](https://nedbatchelder.com/text/unipain.html) for more information on Python and Unicode.

### 13.40 - Parsing HTML with the Beautiful Soup Module

- To locate specific HTML elements within an HTML file, you can parse the HTML by using the Beautiful Soup ([beautifulsoup4](https://pypi.org/project/beautifulsoup4/)) third-party module:

  ```python
  import bs4
  import requests

  # Request an HTML page:

  res = requests.get('https://www.amazon.com/dp/1593275994/')

  # "BeautifulSoup()" will return a "beautifulsoup" object. The first argument
  # is the content to be parsed, and the second argument is the type of parser
  # you want to use (in this case, HTML):

  soup = bs4.BeautifulSoup(res.text, 'html.parser')

  # "select()" takes in a string containing the CSS selector you are seeking,
  # and it will return a list of all matching elements. In this case, there
  # will be only one matching element, so it will return a list containing a
  # single <span> tag for the "header-price" from the requested Amazon page:

  elements = soup.select(
      """#newOfferAccordionRow > div > div.a-accordion-row-a11y > a > h5 >
      div > div.a-column.a-span4.a-text-right.a-span-last >
      span.a-size-medium.a-color-price.header-price"""
  )

  # Access a matching element's internal text content (e.g., just the contents
  # of a <span>, not the opening/closing tags) via the "text" variable:

  elements[0].text    # (Includes the price and newline/whitespace characters)

  elements[0].text.strip()    # (Includes only the price)
  ```

### 13.41 - Controlling the Browser with the Selenium Module

- If you need to parse information from a website that requires you to log in or requires some user interaction with JavaScript, then using Beautiful Soup alone will not be sufficient (as you will have to do more than just download an HTML page). To solve such problems, the [Selenium](https://www.seleniumhq.org/) third-party module can be used to launch a browser that can be programmatically controlled by Python:

  ```python
  # Unique way to import Selenium:

  from selenium import webdriver

  # Set the path of your Chrome driver (http://chromedriver.chromium.org/):

  chromeDriverPath = '/Users/bronson/Selenium Drivers/chromedriver'

  # Open a new Chrome browser that will be controlled by the automated process:

  browser = webdriver.Chrome(chromeDriverPath)

  # Direct the automated browser to fetch the requested URL:

  browser.get('https://automatetheboringstuff.com')

  # Target a SINGLE element containing a hyperlink to be clicked:

  element = browser.find_element_by_css_selector(
      """body > div.main > div:nth-child(1) >
      ul:nth-child(18) > li:nth-child(1) > a"""
  )

  # "click()" method automates the process of a clicking a hyperlink:

  element.click()
  ```

    - **NOTE:** Use `find_elements_by_css_selector()` (plural) to fetch a list of **all** matching elements. Other elements that can be targeted with the `find_element_by_` syntax include: `class_name`, `id`, `link_text` (complete match), `partial_link_text` (partial match), `name`, and `tag_name`.

    - **ALSO:** Other browser **nagivation** methods include: `back()`, `forward()`, `refresh()`, and `quit()`.

- Use the `send_keys()` and `submit()` methods to enter text and **submit input**, and use an element's `text` variable to **read** the content of an HTML element:

  ```python
  browser.get('https://www.google.com/')

  # Target Google's search bar:

  searchInput = browser.find_element_by_css_selector(
      '#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input'
  )

  # Enter the given string argument into the search input:

  searchInput.send_keys('python')

  # Fire the submit action associated with the search input:

  searchInput.submit()

  # Target a specific <span> element on the web page (i.e., the first result):

  snippet = browser.find_element_by_css_selector(
      '#rso > div:nth-child(1) > div > div > div > div > div.s > div > span'
  )

  # Display the targeted element's inner text content:

  snippet.text    # 'The official home of the Python Programming Language.'
  ```

[Back to TOC](#id-toc)

<div id='id-section14'/>

## Section 14: Excel, Word, and PDF Documents

### 14.42 - Reading Excel Spreadsheets

- Python can read and write Excel files via the [openpyxl](https://openpyxl.readthedocs.io/en/stable/) third-party module:

  ```python
  # NOTE: Ensure that the CWD is the directory containing your Excel file.

  import openpyxl

  # Open the Excel file (stored as a 'Workbook' object):

  workbook = openpyxl.load_workbook('example.xlsx')   # (Located in: ./14-42)

  # List the names of all sheets in the workbook:

  workbook.sheetnames                 # ['Sheet1', 'Sheet2', 'Sheet3']

  # Access a specific sheet in the workbook (stored as a 'Worksheet' object):

  sheet = workbook['Sheet1']

  # Access the value of a specific cell within a sheet by row/column NAME:

  sheet['A1'].value                   # datetime.datetime(2015, 4, 5, 13, 34, 2)
  str(sheet['A1'].value)              # '2015-04-05 13:34:02'

  # Access a cell by row/column NUMBER (useful when iterating with a loop):

  sheet.cell(row=1, column=2).value   # 'Apples'
  ```

### 14.43 - Editing Excel Spreadsheets

- Example:

  ```python
  import openpyxl

  # Create a new 'Workbook' object:

  workbook = openpyxl.Workbook()

  # Access the workbook's 'Sheet' object

  workbook.sheetnames       # ['Sheet']
  sheet = workbook['Sheet']

  # Assign values to sheet cells:

  sheet['A1'] = 42
  sheet['A2'] = 'Hello'

  # Add a new worksheet to the workbook:

  newSheet = workbook.create_sheet()
  workbook.sheetnames       # ['Sheet', 'Sheet1']

  # Change the worksheet's title:

  newSheet.title = 'My New Sheet'
  workbook.sheetnames       # ['Sheet', 'Sheet1']

  # Specify a new worksheet's order and title upon creation:

  otherSheet = workbook.create_sheet(index=0, title='My Other Sheet')
  workbook.sheetnames       # ['My Other Sheet', 'Sheet', 'My New Sheet']

  # Save the workbook to your storage device:

  workbook.save('test.xlsx')
  ```

### 14.44 - Reading and Editing PDFs

- The [PyPDF2](https://pythonhosted.org/PyPDF2/) third-party module can extract data from PDF files, or manipulate existing PDFs to produce a new file. Note, however, that there may be some PDF files that PyPDF2 will be unable to process. PyPDF2 cannot extract images, charts, or other media, but it can extract text and return it as a string:

  ```python
  import PyPDF2
  import os

  os.chdir('/Users/bronson/Udemy/automate-the-boring-stuff-with-python/14-44')

  # Open in Read-Binary ('rb') mode because PDFs are binary files:

  pdfFile = open('meetingminutes1.pdf', 'rb')

  # Pass the 'File' object to PyPDF2's "PdfFileReader()",
  # which will return a 'PDF Reader' object:

  reader = PyPDF2.PdfFileReader(pdfFile)

  # View the number of pages within the PDF file:

  reader.numPages   # 19

  # "getPage()" returns a 'Page' object (numbering starts at 0):

  page = reader.getPage(0)

  # "extractText()" returns a string of all text extracted from the page:

  page.extractText()

  # Print out the text of each page in the PDF file:

  for pageNum in range(reader.numPages):
      print(reader.getPage(pageNum).extractText())
  ```

- PyPDF2 cannot edit the text of a PDF file, but it can modify a PDF on the **page level** (i.e., you can add, remove, and reorder pages, but you cannot change a specific line of text on a particular page):

  ```python
  # Open two PDF files to be combined into a single file:

  pdf1File = open('meetingminutes1.pdf', 'rb')
  pdf2File = open('meetingminutes2.pdf', 'rb')

  reader1 = PyPDF2.PdfFileReader(pdf1File)
  reader2 = PyPDF2.PdfFileReader(pdf2File)

  # Create a new 'Writer' object that will create a new PDF file:

  writer = PyPDF2.PdfFileWriter()

  # "addPage()" allows you to append pages to a 'Writer' object:

  for pageNum in range(reader1.numPages):
      page = reader1.getPage(pageNum)
      writer.addPage(page)

  for pageNum in range(reader2.numPages):
      page = reader2.getPage(pageNum)
      writer.addPage(page)

  # Open a new 'File' object in Write-Binary mode (will become the new PDF):

  outputFile = open('combinedminutes.pdf', 'wb')

  # Save the PDF with the 'Writer' object's "write()" method:

  writer.write(outputFile)

  # Close all files:

  outputFile.close()
  pdf1File.close()
  pdf2File.close()
  ```

### 14.45 - Reading and Editing Word Documents

- Use the [python-docx](https://python-docx.readthedocs.io/en/latest/) third-party module to create and modify Word documents. `python-docx` divides a Word document into three different data structures: a 'Document' object, which contains a list of 'Paragraph' objects, which each contain a list of one or more 'Run' objects (a new run occurs in a paragraph whenever there is a change to the style, e.g., bold, italics, etc.):

  ```python
  # Import with 'docx' despite the fact that the module is named 'python-docx':

  import docx

  filePath = '/Users/bronson/Udemy/automate-the-boring-stuff-with-python/14-45/'

  # Create a 'Document' object from the Word document file:

  documentObject = docx.Document(filePath + 'demo.docx')

  # View the text of a 'Paragraph' object:

  documentObject.paragraphs       # (Returns a list of all 'Paragraph' objects)

  paragraph = documentObject.paragraphs[1]

  paragraph.text       # 'A plain paragraph having some bold and some italic.'

  # Modify a paragraph's "style", as defined within Word:

  paragraph.style                 # 'Normal'

  paragraph.style = 'Title'

  # View the text of a 'Run' object (split up based on changes to text style):

  paragraph.runs                  # (Returns a list of all 'Run' objects)

  run = paragraph.runs[1]

  run.text                        # 'bold'

  # Check if a 'Run' is bold, italic, or underline (returns a Boolean):

  run.bold                        # True

  run.italic                      # False

  run.underline                   # False

  # Modify a 'Run' object's bold, italic, or underline status:

  run.underline = True

  # Modify a 'Run' object's text:

  run.text = 'bold and underline'

  # Add a new paragraph to the end of the document:

  newParagraph = documentObject.add_paragraph('New paragraph. ')

  # Add additional text content to the new paragraph via "add_run()":

  newParagraph.add_run('New run.')

  # Save the Word document:

  documentObject.save('demo2.docx')
  ```

  - **NOTE:** The `add_paragraph()` and `add_run()` methods can only add content to the end of a file. If you want to insert additional content in the middle of a file, then you will have to create a new 'Document' object that will have its contents be copied from the source document, and you can add new content in the midst of this copying process.

[Back to TOC](#id-toc)

<div id='id-section15'/>

## Section 15: Email

### 15.46 - Sending Emails

- Simple Mail Transfer Protocol (SMTP) is an Internet standard for email transmission. Python implements SMTP via its built-in `smtplib` module:

  ```python
  import smtplib

  # Create a "Connection" object that will be used to connect to the specified
  # SMTP server (i.e., the domain name of your email server). The port number
  # for an SMTP server is 587 (via TLS) or 465 (via SSL):

  conn = smtplib.SMTP('smtp.gmail.com', 587)

  # Establish the connection with the SMTP server (allowing Internet traffic
  # from your Python program). If the connection is successful, you should
  # receive a 2XX HTTP response code:

  conn.ehlo()

  # Start TLS encryption to encrypt your email login password:

  conn.starttls()

  # Log in to your account (first argument is username; second is password).
  # For Gmail, you must generate an "App password":

  conn.login('sender@gmail.com', 'yourAppPassword')

  # Send email. The first argument is the "From" address, and the second is
  # the "To" address. The third argument is the email content, including
  # header information and the body of the email's message. You must include
  # two newline characters to separate the header and body. "sendmail()" will
  # return a dictionary object containing any emails that it FAILED to send:

  conn.sendmail(
      'sender@gmail.com',
      'recipient@example.com',
      'Subject: Straw Dogs\n\nToday the good life means making full use of science and technology...it means seeking peace...it means cherishing freedom.'
  )

  # Close the SMTP connection:

  conn.quit()
  ```

### 15.47 - Checking Your Email Inbox

- The Internet Message Access Protocol (IMAP) is an Internet standard protocol used by email clients to retrieve email messages from a mail server over TCP/IP. Python implements IMAP via its built-in `imaplib` module. However, [imapclient](https://imapclient.readthedocs.io/en/2.1.0/) and [pyzmail](http://www.magiksys.net/pyzmail/) are two third-party modules that may make using IMAP more user-friendly:

  ```python
  import imapclient
  import pyzmail

  # Create a "Connection" object to be used with the specified host:

  conn = imapclient.IMAPClient('imap.gmail.com', port=993, ssl=True)

  # Log in:

  conn.login('doe@gmail.com', 'yourAppPassword')

  # View all email folders:

  conn.list_folders()

  # Select an email folder (e.g., inbox) as the first argument. The second
  # argument can be used to toggle "Read Only" mode (if you want to prevent
  # emails from being deleted):

  conn.select_folder('INBOX', readonly=True)

  # Find an email via the "search()" method. The first argument is a list
  # containing strings formatted according to the imapclient syntax. The
  # method will return a string of unique IDs referencing a particular email:

  UIDs = conn.search(['SINCE 20-Aug-2018'])

  # Translate a UID into an actual email via the "fetch()" method. The first
  # argument is a list containing the desired UID, and the second argument
  # specifies which parts of an email to retrieve:

  rawMessage = conn.fetch([29068], ['BODY[]', 'FLAGS'])

  # Parse the body of the raw email message and store it as a "Message" object:

  message = pyzmail.PyzMessage.factory(rawMessage[29068][b'BODY[]'])

  # View subject line:

  message.get_subject()

  # View sender/recipient:

  message.get_addresses('from')
  message.get_addresses('to')
  message.get_addresses('bcc')

  # The body of a message can be plaintext, HTML, or a combination of the two.
  # The following can be used to view the length of plaintext and HTML portions.
  # If the specified content does not exist, then "None" will be the value:

  message.text_part
  message.html_part

  # Retrieve and decode the text content of the email message (usually UTF-8):

  message.text_part.get_payload().decode('UTF-8')

  # If you have "Read Only" mode disabled, you can delete messages via the
  # "delete_messages()" method that accepts a list of all UIDs to be deleted.
  # (NOTE: This is a PERMANENT deletion. The email is NOT moved to "Trash"):

  conn.delete_messages([29068])

  # Log out:

  conn.logout()
  ```

  - **IMPORTANT:** If you are receiving an SSLCertVerificationError while using `imapclient`, you may need to [downgrade to version 0.13](https://stackoverflow.com/questions/34714342/imapclient-error-on-windows). If you are unable to install `pyzmail`, you may need to install [pyzmail36](https://stackoverflow.com/questions/40924672/pip-install-pyzmail-error-message) instead.

[Back to TOC](#id-toc)

<div id='id-section16'/>

## Section 16: GUI Automation

### 16.48 - Controlling the Mouse from Python

- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) is a third-party Python module for programmatically controlling the mouse and keyboard:

  ```python
  import pyautogui

  # Obtain the resolution of your screen (width, height):

  width, height = pyautogui.size()

  # Obtain the current coordinates of the mouse cursor (width, height).
  # The "width" value indicates the number of pixels from the LEFT of the
  # screen, and the "height" value indicates the number from the TOP.
  # (NOTE: Because the starting position is (0, 0), that means the max position
  # will be one pixel less than the max screen width/height):

  pyautogui.position()

  # Move the mouse cursor to an ABSOLUTE position by specifying the width
  # coordinate (first argument), the height coordinate (second argument),
  # and the duration in seconds for the movement to occur (third argument):

  pyautogui.moveTo(840, 525, duration=0.5)

  # Move to the mouse cursor to a RELATIVE position (in relation to the current
  # position of the mouse) via the "moveRel()" method following the same
  # procedure explained above:

  pyautogui.moveRel(-10, 0, duration=0.25)

  # Left click  on an element at the specified position. If no coordinates are
  # given, then the mouse will simply be clicked at its current position:

  pyautogui.click(450, 10)
  ```

  - **NOTE:** The "click" functionality also includes the following methods: `doubleClick()`, `rightClick()`, and `middleClick()`. Additionally, you can perform **click-and-drag** operations in the same manner as `moveTo()` and `moveRel()` but with the left mouse button treated as being held down by using `dragTo()` and `dragRel()`

  - **TIP:** If your program ever results in the loss of control over your mouse cursor, force the cursor to the top left corner of the screen (0, 0) to kill the process by triggering PyAutoGUI's **failsafe exception**.

- Run the following code from the terminal (note IDLE) to see your current mouse cursor position in real-time. This is useful for planning out all of the locations that you want your program to click:

  ```python
  import pyautogui, sys

  print('Press Ctrl-C to quit.')

  try:
      while True:
          x, y = pyautogui.position()
          positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
          print(positionStr, end='')
          print('\b' * len(positionStr), end='', flush=True)
  except KeyboardInterrupt:
      print('\n')
  ```

  - Alternatively, PyAutoGUI has a method called `displayMousePosition()` that operates in a similar manner.

### 16.49 - Controlling the Keyboard from Python

- Example:

  ```python
  # "typewrite()" sends virtual keypresses to the computer. It can be used
  # in conjunction with "click()" to first click on a text input field. You
  # can specify an "interval" to add a delay (in seconds) between each keypress:

  pyautogui.click(1200, 400)    # ( Also accepts tuple: click((1200, 400)) )

  pyautogui.typewrite('Hello, world!', interval=0.2)

  # To use non-character keys (e.g., left arrow), you must specify the input
  # as strings in a list:

  pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])   # 'XYab'

  # Press a single key:

  pyautogui.press('F1')

  # Trigger a keyboard shortcut:

  pyautogui.hotkey('command', 'f')    # (Opens search dialog)
  ```

  - **NOTE:** You can view a list of all possible keys that can be accessed by `typewrite()` by accessing `pyautogui.KEYBOARD_KEYS`

### 16.50 - Screenshots and Image Recognition

- With PyAutoGUI, you can save a screenshot to an absolute or relative path:

  ```python
  pyautogui.screenshot('example.png')
  ```

- If you have a cropped image of an element that is presently displayed on your screen, you can locate the coordinates of the element by using `locateOnScreen()` or `locateCenterOnScreen()`, which is useful for targeting a specific element for to be clicked:

  ```python
  # Displays the coordinates of the element's top left corner, along with
  # width and height of the found element:

  pyautogui.locateOnScreen('crop.png')          # (1690, 516, 64, 64)

  # Displays the coordinates of the element's center point on screen:

  pyautogui.locateCenterOnScreen('crop.png')    # (1722, 548)
  ```

  - **NOTE:** These image recognition methods are computationally expensive and take time to complete (and therefore will not work on moving content). Additionally, the element on screen must be a **pixel perfect** match of the reference image.

[Back to TOC](#id-toc)
