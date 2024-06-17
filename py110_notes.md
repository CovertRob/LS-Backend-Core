# PY110 Notes and Study Material

## Collections and Sequences

### Operations on Sequences

- Slicing: syntax for slicing is `sequence[start:stop:step]`
- stop index is not included in the slice
- If ommitted, start defaults to 0 for positive steps and -1 for negative step values

~~~Python
>>> lst = [0, 1, 2]

>>> # Omitting start with a positive step
>>> lst[::1]
[0, 1, 2]

>>> tup = (0, 1, 2)
>>> # Omitting start with a negative step
>>> tup[::-1]
(2, 1, 0)

>>> # For ranges, the start parameter works similarly:
>>> r = range(10)
>>> list(r[2:])
[2, 3, 4, 5, 6, 7, 8, 9]
~~~

- If stop index ommitted it will go up to the end of the sequence
- If start is greater than stop, the result is an empty sequence
- If step negative, empty sequence returned when stop is greater than start
- Note that my_list[::] is equivalent to my_list[:]. Both expressions yield a shallow copy of a list. This is considered pythonic or idiomatic code, so it's seen often.
- strings are sequences of characters so we iterate over them char by char:

~~~Python
>>> message = "bye"
>>> for char in message:
...    print(char)
...
b
y
e
~~~

- While loops are often used when you need the index of each item
- More idiomatic to use the enumerate function for this purpose

- You cannot concatenate ranges

- `sequence.count(value)` returns the number of occurrences of a value in the sequence
- `sequence.index(value)` returns the index of the first occurrence of a value in the sequence - if not present, raises ValueError
- count either returns 0 or 1 with ranges
- when using the list and tuple constructor on strings it breaks it up into chars

- Can use list comprehension to get around all elements needing to be strings with join:

~~~Python
>>> my_list = [1, 2, 3, 4]
>>> ', '.join([str(element) for element in my_list])
'1, 2, 3, 4'
~~~