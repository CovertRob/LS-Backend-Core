# Course Notes

## False values in Python

There are 12 in total

- False
- None
- 0
- 0.0
- 0j
- "" an emtpy string
- [] an empty list
- {} an empty dictionary
- () an empty tuple
- set() an empty set
- frozenset() an empty frozen set
- range(0) an empty range

## Pseudocode

Before we can take our pseudocode and translate it to program code, we must formalize the pseudocode a little more. We'll still use English, but we'll use some keywords to help us break down the program logic into concrete commands, which makes translating to code more natural.

We'll use the below keywords to assist us, along with their meaning.

Keyword Meaning
START start of the program
SET set a variable that we can use for later
GET retrieve input from user
PRINT display output to user
READ retrieve a value from a variable
IF/ELSE IF/ELSE show conditional branches in logic
WHILE show looping logic
END end of the program

## Flowchart Components

Used to determine logic flow in a program

-![alt text](image.png)

- oval: start/stop
- rectangle: processing step - define variables here
- rhombus: input/output
- Diamond: decision, only has two branches
  - If decision w/ > 3 branches, user seperate diamonds
- Circle: connector

## Pylint

- C: (Convention) for programming standard       violation
- R: (Refactor) for bad code smell
- W: (Warning) for Python specific problems
- E: (Error) for semantic errors that cause broken code
- F: (Fatal) for errors which prevented further processing

- Use a .pylintrc file for configurations to modify how strict it is on grading. Create this in your project directory

## Refactoring calcualtor program

- Use helper functions to wrap up repetetive code
- Use try and except statement and a while loop to evaluate if
something is true to validate waht the user inputs

## Precedance rules - top to bottom

Operators Meaning
() Parentheses
** Exponent
+x, -x, ~x Unary plus, Unary minus, Bitwise NOT
*, /, //, % Multiplication, Division, Floor division, Modulus
+, - Addition, Subtraction
<<, >> Bitwise shift operators
& Bitwise AND
^ Bitwise XOR
| Bitwise OR
==, !=, >, >=, <, <=, is, is not, in, not in Comparisons, Identity, Membership operators
not Logical NOT
and Logical AND
or Logical OR
![alt text](image-1.png)

## Important String methods

### Method         Description

- capitalize() Converts the first character to upper case
- casefold()     Converts string into lower case
- center()     Returns a centered string
- count()         Returns the number of times a specified value occurs in a string
- encode()     Returns an encoded version of the string
- endswith()     Returns true if the string ends with the specified value
- expandtabs() Sets the tab size of the string
- find()         Searches the string for a specified value and returns the position of where it was found
- format()     Formats specified values in a string
- format_map() Formats specified values in a string
- index()         Searches the string for a specified value and returns the position of where it was found
- isalnum()     Returns True if all characters in the string are alphanumeric
- isalpha()     Returns True if all characters in the string are in the alphabet
- isascii()     Returns True if all characters in the string are ascii characters
- isdecimal()     Returns True if all characters in the string are decimals
- isdigit()     Returns True if all characters in the string are digits
- isidentifier() Returns True if the string is an identifier
- islower()     Returns True if all characters in the string are lower case
- isnumeric()     Returns True if all characters in the string are numeric
- isprintable() Returns True if all characters in the string are printable
- isspace()     Returns True if all characters in the string are whitespaces
- istitle()     Returns True if the string follows the rules of a title
- isupper()     Returns True if all characters in the string are upper case
- join()         Converts the elements of an iterable into a string
- ljust()         Returns a left justified version of the string
- lower()         Converts a string into lower case
- lstrip()     Returns a left trim version of the string
- maketrans()     Returns a translation table to be used in translations
- partition()     Returns a tuple where the string is parted into three parts
- replace()     Returns a string where a specified value is replaced with a specified value
- rfind()         Searches the string for a specified value and returns the last position of where it was found
- rindex()     Searches the string for a specified value and returns the last position of where it was found
- rjust()         Returns a right justified version of the string
- rpartition() Returns a tuple where the string is parted into three parts
- rsplit()     Splits the string at the specified separator, and returns a list
- rstrip()     Returns a right trim version of the string
- split() S       plits the string at the specified separator, and returns a list
- splitlines() Splits the string at line breaks and returns a list
- startswith() Returns true if the string starts with the specified value
- strip()         Returns a trimmed version of the string
- swapcase()     Swaps cases, lower case becomes upper case and vice versa
- title()         Converts the first character of each word to upper case
- translate()     Returns a translated string
- upper()         Converts a string into upper case
- zfill()         Fills the string with a specified number of 0 values at the beginning

- and and or do not have precedence, in an expression it goes left to right. **All 8 comparison operations have same priority (but higher than boolean operations)** in and not in have same priorities as comparison operations
- For short circuting, or statements return the first truthy element or they return the last falsy element
- the and statement returns teh last truthy element and the first falsy one
**Note that neither and nor or restrict the value and type they return to False and True, but rather return the last evaluated argument. This is sometimes useful, e.g., if s is a string that should be replaced by a default value if it is empty, the expression s or 'foo' yields the desired value. Because not has to create a new value, it returns a boolean value regardless of the type of its argument (for example, not 'foo' produces False rather than ''.)**
- python will print the last element in an expression to the terminal
- remember [none] is actually

## Dict view objects

- the .keys() method returns a dictionary view object and not an actual list. If you print it it will print with ([]) which shows its not an actual list
- dict view objects are dynamic, so changes to the dict will show in all of them

# PY101 study guide - all topics

## Naming Conventions

Naming conventions: legal vs. idiomatic, illegal vs. non-idiomatic

- Closely related to the stylistic conventions discussed in the Using Python chapter are the Python naming conventions. Names that follow these conventions are idiomatic. In contrast, those that do not are non-idiomatic (valid but not idiomatic) or illegal (your code will either raise a syntax error or do something unexpected).

- Naming conventions for most identifiers (excluding constant and class names):

    Use snake_case formatting for these names.
    Names may contain lowercase letters (a-z), digits (0-9), and underscores (_).
    Names should begin with a letter.
    If the name has multiple words, separate the words with a single underscore (_).
    Names that begin or end with one or two underscores have special meaning under the naming conventions. Don't use them until you understand how they are used.
    Names may only use letters and digits from the standard ASCII character set.
- Idiomatic Names:
    foo
    answer_to_ultimate_question
    eighty_seven
    index_2
    index2
- Constant names (unchanging named values):

    Use SCREAMING_SNAKE_CASE formatting for these names.
    Names may contain uppercase letters (A-Z), digits (0-9), and underscores (_).
    Names should begin with a letter.
    If the name has multiple words, separate the words with a single underscore (_).
    Names that begin or end with one or two underscores have special meaning under the naming conventions. Don't use them until you understand how they are used.
    Names may only use letters and digits from the standard ASCII character set.
- Idiomatic Names:
    FOO
    ANSWER_TO_ULTIMATE_QUESTION
    EIGHTY_SEVEN
    INDEX_2
    INDEX2

- Class names:

    Use PascalCase formatting for these names. PascalCase is sometimes called CamelCase (with both Cs capitalized).
    Names may contain uppercase and lowercase letters (A-Z, a-z) and digits (0-9).
    Names should begin with an uppercase letter.
    If the name has multiple words, capitalize each word.

- Idiomatic Names
    Foo
    UltimateQuestion
    FourLeggedPets
    PythonVersion2Rules

- Note that many non-idiomatic names are still legal (valid) Python identifiers. Sometimes, it makes sense to break the rules. However, not all identifiers are legal; here are some things you must do:

    You can use letters, digits, and underscores in Python identifiers. Extended ASCII and Unicode letters and digits are allowed.
    You may not use punctuation characters, most special characters, or whitespace.
    You may not start identifiers with a digit.
    You may not use Python's reserved words such as if, def, while, return, and pass as names.

- Non-Idiomatic Names Explanation
    fourWayIntersection: camelCase
    Schön: Extended ASCII

    Illegal Names Explanation
    pass:         Reserved word
    3xy:         Starts with digit
    ultimate-question: Hyphen
    one two three: Whitespace
    is_lowercase?: Punctuation
    is+lowercase: Special character

- Most illegal names will raise an error. However, if the illegal name looks like valid Python, you won't get an error.

- Variable names are often referred to by the broader term identifiers. In Python, identifiers refer to several things:
  - Variable and constant names
  - Function and method names
  - Function and method parameter names
  - Class and module names

## type coercions: explicit (e.g., using int(), str()) and implicit

- Explicit type coercioin occurs when a programmer intentionally employs built in functions to convert a value of one type to another.
  - For example, using int() to convert a string from input() if we are asking for an int input
  - Trying to convert a non-numberic string to an integer using int() will raise a ValueError
  - int() will accept also a real number (floating point), bytes-like object, and also boolean values (because they can evaluate to 1 and 0)
  - any other data type passed to int(), for example a list, will raise a TypeError
  - floats have a special "Not-a-number" value
  - print() automatically will call the str() function. str() works with all buiilt in python data types and most non-built in types
  - Note: repr() will print a string representation of an object. For example, printing the list [1, 2, 3] with print() will print the values,
    however repr of that will print '[1, 2, 3]'. This can be used to recreate the object later on

- Implicit type conversion (automatic data type conversation), when python automatically transofmrs one dat typoe into another without the programers
direct instruction. Typically occurs when mixing distinct data types
  - For example: calculations between an int and a float, python will convert the int to a float
  - print() will implicitly convert any non-string arguments to a string

## numbers, including handling exceptions (ValueError, ZeroDivisionError)

- Numeric values represent numbers. Numbers can be added, subtracted, multiplied, and divided and can be used in a wide variety of mathematical operations.
- Int represents integers, aka whole numbers, to include negative whole numbers
- Python also supports other numeric types, such as complex, decimal, and fractional numbers.
- You can break up numbers with underscores: 123_456_789. Commas and decimals are not valid seperators
- Floats represent real numbers: includes integers and numbers with digits after the decimal point
- scientific notation is: 10**n, where n is positive, represents a 1 followed by n zeroes
- Python will print large and small floats w/ scientific notation
print(3.14 * (10**20))        # 3.14e+20
print(3.14 * (10**-20))       # 3.14e-20

- Can also do this:
print(3.14e+20 / 2.72e-15)    # 1.1544117647058823e+35

- Integers DO NOT get printed with scientific notation
- Must do this:
print(int(3e+20))             # 300000000000000000000

- If python interpreter cannot continue executing a program: creates an Exception Object that describes problem and stops the program
  - This is called "raising an exception"
  - Example, trying to cast a string to a float creates a **value error**
  - zero division error is when denom is zero

## strings

Examples:
'Hello!'
"He's pining for the fjords!"
'1969-07-20'
f'{greeting}! My name is {my_name}'
r'\w+\d+'

- Also includes byte string sequences
- text sequence vs ordinary sequence: text sequence (string) does not contain any objects, only the characters (bytes) that make up the text. These are not objects, simply part of the value
- Escaping quotations:
    print("""My nickname is "Wolfy". What's yours?""")
    print('My nickname is "Wolfy". What\'s yours?')
    print("My nickname is \"Wolfy\". What's yours?")
- Both of these print C:\Users\Xyzzy
print("C:\\Users\\Xyzzy")  # Each \\ produces a literal \
print(r"C:\Users\Xyzzy")  # raw string literal

## f-strings

- primarily used for string interpolation
- can be used instead of the format method
- can also escape {} by doing {{}} in f strings
- f strings for numbers:
    print(f'{123456789:_}')       # 123_456_789
    print(f'{123456789:,}')       # 123,456,789
- f strings for floats:
    print(f'{123456.7890123:_}')  # 123_456.7890123
    print(f'{123456.7890123:,}')  # 123,456.7890123

### string methods

1. capitalize - return a copy of the string w/ first character capitalized and the rest lowercased
    str.capitalize()
2. swapcase - return a copy of string w/ uppercase characters to lowercase and vice versa. Note not necessarily true that
str.swapcase().swapcase() == str (because of non ASCII chars)
str.swapcase()
3. upper - return copy of string w/ all cased chars converted to uppercase. Note str.upper().isupper() might be flase if str
contains uncased characters or if the unicode catergory of the resulting char is not "Lu" (letter, uppercase) but "Lt" (letter, titlecase)
    \p{Lu} or \p{Uppercase_Letter}: an uppercase letter that has a lowercase variant.
    \p{Lt} or \p{Titlecase_Letter}: a letter that appears at the start of a word when only the first letter of the word is capitalized.
str.upper()
4. lower - return copy of string w/ all cased chars converted to lowercase.  Used 'default case folding' from unicode standard
str.lower()
5. isalpha - return **True** if all chars in str are alphabetic and there is at least one char, **False** otherwise.
    Defined by uncode char database as "Letter": “Lm”, “Lt”, “Lu”, “Ll”, or “Lo”
str.isalpha()
6. isdigit - return **True** if all chars in str are digits and there is at least one char, **False** otherwise.
    Digits include: decimal chars and digits that need special handling such as compatability superscript digits
    Formally: digit has property value Numeric_Type=Digit or Numeric_Type =Decimal.
7. isalnum - return **True** if all char in str are alphanumeric and there is at least one char, **False** otherwise.
    Char 'c' is alphanumeric if one of the following returns **True**: c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric()
8. islower - return **True** if all cased chars in str are lowercase and there is at least one cased character, **False** otherwise
9. isupper - return **True** if all cased chars in str are uppercase and there is at least one cased character, **False** otherwise
10. isspace - Return **True** if there are only whitespace chars in str and there is at least one char, **False** otherwise
11. strip - str.strip([chars]) - return copy of str w/ leading and trailing characters removed. Chars argu ment is a string
    specifying set of chars to be removed. If ommitted or **None**, chars arg defualts to removing whitespace.
    Chars arg not a prefix or suffic, all combos are stripped.
    Exampe:
    `'   spacious   '.strip()`
               `'spacious'`
    `'www.example.com'.strip('cmowz.')`
           `'example'`
12. rstrip - str.rstrip([chars]) -return copy of str w/ trailing chars removed. Same specifications for argument as strip, not a suffix.
13. lstrip - str.lstrip([chars]) - return copy of string w/ leading chars removed. Same specifications for argument as strip, not a prefix.
14. replace - str.replace(old, new[, count]) - return copy of str w/ all occurrences of substring _old_ replaced by _new_.
    If optional argu ment _count_ is given, only the first _count_ occurrernces are replaced
15. split - `str.split(sep=None, maxsplit=-1)` - Return a list of the words in the string, using _sep_ as the delimiter string.
    If _maxsplit_ is given, at most _maxsplit_ splits are done (therefore will have at most maxsplit+1 elements).
    If _maxsplit_ not specified or -1, the no limit on number of splits (all possible are made)

16. find - `str.find(sub[, start[, end]])` - Return lowest index in str where substring _sub_ is found w/in slice s[start:end].
    Optional arguments start and end are interpreted as in slice notation
    **Return -1 if sub not found**
17. rfind - `str.rfind(sub[, start[, en]])` - Return highest index in str where substring _sub_ is found, such that _sub_ is contained
    w/in s[start:end]. Opt args interpreted in slice notation.
    **Return -1 on failure**

## boolean vs. truthiness

- True or false is not the same as saying something returns truthy or false ( aka evaluates as true or evaluates as false)
- True and False refer to the boolean values True and False - other phrases refer to truthiness, that is a truthy or false value
`num = 5`
`if num:`
    `print("valid number")`
`else:`
    `print("error!")`
- Above prints valid number because any non-zero number is truthy
- However, print(num == True) is False because num is still not equal to the boolean value of True

## None

- A literal value whole value is the lone representative of the _NoneType_ class
- Used to indicate missing, unset, or unavailable data and may sometimes be an error indication

** Side note: _Literals_ in python definition: literal types indicate that a var has a specific and concrete value.
    - Also m eans all methods from the parent type will be directly inherited by the literal type.
    - Lets you directly represent an object in source code
    - Literals: strings, numeric, booleans, collections (list, dict, tuple, set), special (None)

## ranges

- Sequence of integers between two endpoints
- Commonly used to iterate over an increasing or decreasing range of integers
- Range starts from 0 and ends just before argument
- W/ two arguments, first arg is starting point and second arg is one past the last number in range
- Third arg is step value : can use -1 to from highest to lowest value
- **Python optimizes ranges - won't create it before the program asks for it**
- Can  use indexing syntax to access specific numbers in range object:
`>>> my_range = range(5, 10)`
`>>> my_range[3]               # 8`
- Examples:
`>>> tuple(range(5))`
`(0, 1, 2, 3, 4)`

`>>> tuple(range(5, 10))`
`(5, 6, 7, 8, 9)`

`>>> list(range(1, 10, 2))`
`[1, 3, 5, 7, 9]`

`>>> list(range(0, -5, -1))`
`[0, -1, -2, -3, -4]`

## list and dictionary syntax

- List literals use square brackets [] surrounding a comma-delimited list of values, while tuples use parentheses ().
- The comma-delimited list values are known as elements.
`>>> my_list = [1, 'xyz', True, [2, 3, 4]]`
`>>> my_list`
`[1, 'xyz', True, [2, 3, 4]]`

`>>> tup = ('xyz', [2, 3, 4], 1, True)`
`>>> tup`
`('xyz', [2, 3, 4], 1, True)`

- Multi-line:

~~~Python
[ # Begin multi-line list literal`
    "Monty Python's Flying Circus",
    ( # Begin multi-line tuple literal
      'Eric Idle',
      'John Cleese',
      'Terry Gilliam',
      'Graham Chapman',
      'Michael Palin',
      'Terry Jones',
    ), # End multi-line tuple literal
] # End multi-line list literal
~~~

- The most important facts to remember about lists and tuples are:

    The order of the elements is significant.
    Lists are mutable; tuples are immutable.
    Use indexing syntax to retrieve specific elements.
    Use indexing syntax to reassign specific list elements.
    Index numbers are non-negative integers starting from 0 and ending at the sequence's length minus 1.
- Dictionary syntax(type of map):

~~~Python
>>> my_dict = {
...     'dog': 'barks',
...     'cat': 'meows',
...     'pig': 'oinks',
... }
{'dog': 'barks', 'cat': 'meows', 'pig': 'oinks'}
~~~

- Use [] key access syntax, value between the brackets must be one of the keys in the dict
- **Dictionairies are unordered collections in which insertion order is preserved**

## list/dict methods

- len(list) - return the length (number of items) of the list

- list.append() - add an item to the end of the list. Equivalent to `a[len(a):] = [x]` **RETURNS NONE**

Think back to how slices work: a[beginning:end]. If you do not supply one of them, then you get all the list from beginning or all the way to end.
What that means is if I ask for a[2:], I will get the list from the index 2 all the way to the end of the list and len(a) is an index right after the last element of the array...
so `a[len(a):]` is basically an empty array positioned right after the last element of the array
**Using slice notation in lists creates a shallow copy**

- list.pop() - remove the item at the given position in the list, and return it. If no index is specified, pop() removes and returns the
last item in the list. **Raises an IndexError if list is empty or index is outside the list range**

- list.reverse() - reverse the elements of the list in place. This mutates the original object. **RETURNS NONE**

## dictionary methods

- keys(), values(), and items() all **Return a dictionary view object** - provides a dynamic view on the dict's entries. When dict changes, the view reflects it
- dict.keys() - returns a new view of the dictionary's keys
- dict.values() - return a new view of the dictionary's values. **Equality comparisons between one dict.values() view and another will always return false, including comparing to itself**
- dict.items() - return a new view of the dictionary's keys
- dict.get() - `dict.get(key, default=None)` - return the value for _key_ if it is in the dictionary, else _default_.
If default not given, it defaults to **None**, so that this method never raises a KeyError.

## operators

~~~Python
    Arithmetic: +, -, *, /, //, %, **
    String operators: +
    List operators: +
    Comparison: ==, !=, <, >, <=, >=
    Logical: and, or, not
    Identity: is, is not
    operator precedence - use list below
~~~

- `==` operator compares the value or equality of two objects, whereas `is` operator checks two variables point to same object in memory

## mutability and immutability

- Mutable - refers to the capability of an object to be changed or modified after its creation
    1. lists
    2. dicts
    3. sets
    4. functions
- Immutable - cannot be changed after it is created
    1. int
    2. float
    3. boolean
    4. strings
    5. ranges
    6. tuples

## variables

naming conventions - covered above

- Function names should reflect whether side effects occur. Ex: display_total as name of function that displays a total on the console
- comput_total would imply it just returns the value of a computation. **AKA no side effect**

Initialization, assignment, and reassignment - self-explanatory
Scope - global, function scope aka local scope. Inner function scope
Global keyword

## Variables as pointers

- Pass by reference - means it is passing a pointer to the original object, allowing you to change the original object
- Pass by value - traditionally, it means the function has a copy of the original object. Operations performed on this object
    within the function have no effectg on the oriignal object outside the function.
- **Python is described as a pass by object reference as you are actually passing a reference to the object (value) rather than a copy of the object itself**
- **Whether the function can modify the object depends on whether the object is mutable or immutable.

variable shadowing

## conditionals and loops

for
while

## print() and input()

## Functions

definitions and calls
return values
parameters vs. arguments

- Arguments are data you pass from outside the function's scope into the function so it can access that data **actual values**
- Names between parentheses in the function definition are called parameters - **placeholders for potential arguments**

nested functions - does variable scope apply to nested functions? - Yes

output vs. return values, side effects

- output is not the same thing as returning a value. Return values can be used elsewhere in the program and are not always written to output
- Side effects: these are when a function modifies something outside of the functions definition. Ex: modifying a list with the reverse() method
    1. Reassigns any non-local variable
    2. Modifies the value of any data structure passed as an argument, or acessed directly from the outer scope. Mutating an object, such as appending
    an element to a list argument.
    3. Reads from or writes to a file, network connection, browser, or system hardware. **Side effects like this include printing and reading from terminal**
    4. Raises an exception without handling it
    5. It calls another function that has side effects
**Functions should return a useful value or should have a side effect, NOT BOTH**

## expressions and statements

- Expression - combines values, variables, operators, and calls to functions to produce a new object. They must be evaluated to determine
    the expression's value. Ex's include:
    1. Literals: `5, 'Karl', 3.141592, True, None`
    2. Variable references: foo or name when these variables have been previously defined.
    3. Arithmetic operations: `x + y or a * b - 5.`
    4. Comparison operations: `'x' == 'x' or 'x' < 'y'.`
    5. String operations: `'x' + 'y' or 'x' * 32.`
    6. Function calls: `print('Hello') or len('Python').`
    7. Any valid combination of the above that evaluates to a single object.

- Statement - an instructionthat tells python to perform an action of some kind. **Unlike expressions, statements don't return values**. They do
    something but don't produce a value as expressions do. Ex's:
    1. Assignment: like x = 5. This doesn't evaluate as a value; it assigns a value to a variable.
    2. Control flow: such as if, else, while, for, and so on. These determine the flow of your program but don't evaluate as a value themselves.
    3. Function and class definitions: using def or class.
    4. Return statements: like return x, which tells a function to exit and return a value. return itself doesn't return a value; it informs the function what value it should return.
    5. Import statements: such as import math.
    6. stand-alone expression are considered both expressions and statements:

~~~Python
3 + 4            # Simple expression
print('Hello')   # Function call; returns None
my_list.sort()   # Method call; returns None
~~~

## discuss a function's use and purpose (a "user-level" description) instead of its implementation

![alt text](image-2.png)

# PY109 TA Session

## Questions for Antonina

1. How well should we know list comprehensions since they are in the book
2. Go over precedence for 'or' and 'and' operators

~~~Python
greeting = "Hello"
# initalize variable greeting

def greet(greeting): # define greet function w/ 1 parameter
    greeting += " world" # 
    print(greeting) # does not mutate global bc uses local var

greet(greeting) >>> Hello world
print(greeting) >>> Hello

# Overall concepts: variable shadowing, string immutability

greeting = "Hello"

def greet():
    global greeting
    greeting += " world"
    print(greeting)

greet() >>> Hello world
print(greeting) >>> Hello world
~~~

## Truthiness questions

~~~ Python
# print('a' and 2 < 3) # True
print(None or 1 > -2.5) # True
# print('' or []) # []
# print(2 < 3 and '' or 'c' > 'a')
        (True and Falsy) or True
~~~

~~~ Python
lst1 = [0, 1, 2, 3]
lst2 = lst1.pop(1)

if lst2:
    print(lst2) # returns 1 b/c pop method returns the element
else:
    print(lst1)

~~~

~~~Python
letters = ['b', 'a', 'c', 'f']

def reverse_list1(lst):
    return lst[::-1]

def reverse_list2(lst):
    return lst.reverse()

print(reverse_list1(letters)) # ? # makes copy, doesn't mutate original list
print(reverse_list2(letters)) # ? # returns none, reverse mutates original list
print(letters) # will print the reversed list due to mutation by reverse in above function call

#Concepts: mutate by object pass reference
#Note: the is operator uses the id() functions behind the scenes
~~~
