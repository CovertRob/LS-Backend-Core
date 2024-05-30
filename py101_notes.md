# False values in Python
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

# Pseudocode

Before we can take our pseudocode and translate it to program code, we must formalize the pseudocode a little more. We'll still use English, but we'll use some keywords to help us break down the program logic into concrete commands, which makes translating to code more natural.

We'll use the below keywords to assist us, along with their meaning.

Keyword	Meaning
START	start of the program
SET	set a variable that we can use for later
GET	retrieve input from user
PRINT	display output to user
READ	retrieve a value from a variable
IF/ELSE IF/ELSE	show conditional branches in logic
WHILE	show looping logic
END	end of the program

# Flowchart Components

Used to determine logic flow in a program

-![alt text](image.png)
- oval: start/stop
- rectangle: processing step - define variables here
- rhombus: input/output 
- Diamond: decision, only has two branches
    - If decision w/ > 3 branches, user seperate diamonds
- Circle: connector


# Pylint

- C: (Convention) for programming standard       violation
- R: (Refactor) for bad code smell
- W: (Warning) for Python specific problems
- E: (Error) for semantic errors that cause broken code
- F: (Fatal) for errors which prevented further processing

- Use a .pylintrc file for configurations to modify how strict it is on grading. Create this in your project directory

# Refactoring calcualtor program

- Use helper functions to wrap up repetetive code
- Use try and except statement and a while loop to evaluate if 
something is true to validate waht the user inputs

# Precedance rules - top to bottom

Operators	Meaning
()	Parentheses
**	Exponent
+x, -x, ~x	Unary plus, Unary minus, Bitwise NOT
*, /, //, %	Multiplication, Division, Floor division, Modulus
+, -	Addition, Subtraction
<<, >>	Bitwise shift operators
&	Bitwise AND
^	Bitwise XOR
|	Bitwise OR
==, !=, >, >=, <, <=, is, is not, in, not in	Comparisons, Identity, Membership operators
not	Logical NOT
and	Logical AND
or	Logical OR