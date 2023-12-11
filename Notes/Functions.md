# Function

A function is a block of code that can be reused over and over again

We can input data to the function. We can refer to the data as parameters

We use the term **arguments** to describe the ACTUAL data that we put into the function.

```python
def area_of_a_square(sidelength: float): float means the input can be a decimal number
	"""Calculates the area of a square.
	Results are in units squared.
	Params:
	
	sidelength - length of one side of the square"""
	
	print(f"The area of a square with side length = {sidelength}) is: {area} square units")
	area = sidelength ** 2

area_of_a_square(12.2) # 12.2 is the argument
```

## Functions with return values

We can call functions with return values, "fruitful functions" (not a term in industries) that teach the main idea of functions that return a value

```python
def adder(x: int, y: int) -> int:
"""Returns the sum of two given numbers"""
sume = x + y

return sum

adder(10, 2) # returns 12
print(adder(10, 2)) # will print value
```


The return keyword does two things in a function, it 

1) stops the function
2) if there a value, after the return keyword, it sends the value back to where the function is called

```python
def linear_search(l: list, item: Any) -> int:
"""Search through a list and if found, 
returns the index of the item occurence

Params: 
l - list we are searching through
item - thing being searched for
"""

counter = 0

# search an algorithm
for thing in it:
if thing == item:
return counter
counter += 1

return -1
```

## Recursion

is a way to repeat a pattern

Fractals are examples of patterns that can be described recursively

a recursive function must have 3 parts:

1) a function
2) somewhere in the body code block, the function should call itself
3) a base case - this is where the function stops calling itself

### Factorials and Recursion

```
0! = 1
1! = 1

2! = 1 x 2
2! = 1! x 2

3! = 1 x 2 x 3
3! = 2! x 3
```