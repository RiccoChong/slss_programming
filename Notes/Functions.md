(***A function is a block of code that can be reused over and over again***)

We can input data to the function. We can refer to the data as --**parameters**--

We use the term **arguments** to describe the ACTUAL data that we put into the function.

```python
def area_of_a_square(sidelength: float):
	"""Callculates the area of a square.
	Results are in unit squared.
	
	params: 
	
	sidelength - legnth of one side of the square"""

	area = sidelegnth ** 2

	print(f"The area of a square with side legnth = {sidelegnth}
is: {area} square units.")

area_of_a_square(12.2)   # 12.2 is the argument 
```

# Functions with Return ValuesWe can call functions with return values, fruitful functions.  
```python  
def adder(x: int, y: int) -> int:  
"""Returns the sum of two given numbers."""  
sum = x + y  

return sum

adder(10, 2)
print(adder(10, 2)). # This will print the value
```

The return keyword does two things in a function

1. stops the function when it finds the variable
2. if there is a value after the keyword, it sends the value back to where the function is called
```python
def linear_search(l: list, item: Any) -> int
	"""search through a list and if found,
	retern the index of the first recurent of the item
	
	params: 1 - list we search through
	item - item we are looking for

	return:
		index if found
	"""
	counter = 0

	# Search item in list
	for item in l:
		if thing = item:
			return counter
		counter += 1

	return -1

```

## Recursion
recursion is an elegant way to repeat a pattern.
fractals are examples of patterns that can be described recursively.

A recursive function must have three parts

1. need to have a function
2. somewhere in the body code block, the function should call itself
3. A Base case. This is where a function stops calling itself

## Factorials and Recursion

```
0! = 1
1! = 1

2! = 1 * 2
2! = 1! * 2

3! = 1 * 2 * 3
3! = 2! * 3
```