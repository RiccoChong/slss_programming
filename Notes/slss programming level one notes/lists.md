In Python, lists are a collection of items  
We store values inside of lists  
The values of the items can be of different [[Type]]s  
**Order matters** in a list

# Creating a List
To make a list, we use brackets \[\] to surround our list  
We separate the individual items with commas

```python
some_list = ["Jimmy", "Sara", "Frederique"]
```

# Access Elements in the List
We can access the individual things from lists using **bracket notation**  
In the example below, we'll use bracket notation to access "Sara"  

```python
some_list[1]          # "Sara"
some_list[0]          # "Jimmy"
some_list[2]          # "Frederique"
some_list[-1]         # "Frederique"  counts from the end
some_list[-2]         # "Sara"
```

Inside the brackets, we give the *index* of the item we want  
Python uses **0-index** counting, which means we start counting at 0

## 2-Dimensional Lists

So far, all the lists we've used are one-dimensional.

```python
some_list = ["blue", "red", "green"]
```

We can create two-dimensional lists that in short, are 
multiple lists inside a bigger list.

```python
some_2d_list = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

#            r  c
some_2d_list[0][0]    # -> 1
some_2d_list[0][1]    # -> 2
```
## Tuples

Tuples (toopels or tuhpels) are like lists except for one
main thing.

Tuples are **immutable**. Immutable means that **you can't
change** the contents of a tuple. 

Because they are immutable they have some performance
benefits.

```python
some_tuple = (1, 2, 3, 4, 5)
```
To create a tuple, use parentheses instead of brackets.

### Images and Tuples

The basic unit of measurement in images is a pixel.
The pixel information is stored in a tuple of three-values
(3-tuple). 

The 3-tuple tells us for ONE PORTION of the image, what
the RED, GREEN, BLUE values are. `(red, green, blue)`

```
          r,   g,   b
RED -   (255,   0,   0)
BLUE -  (  0,   0, 255)
GREEN - (  0, 255,   0)
```