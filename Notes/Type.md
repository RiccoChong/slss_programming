In Python, data can be grouped in categories called **Types**.

| Name      | Example          |
| ---           | ---                   |
| string or `str`  | `"hello world!"`        |
| `list`     | [1, 2, 3, 4, 5] |
| boolean or `bool` | `True False` |
|integer or `int` | `1 -10 1205` |
| float | `1.2 -432.21 1.0` |
An example showing the use of these names:
```python
favourite_food = "bibimbap"
my_age = 16
my_age_float = 16.0
# my_age_float is of type float
```

## converting types

there are some special functions build in to python that helps to convert data from one type to another

```python
intro_string = "My age is"
my_age = 15

# Recall
"My name is" + "Ricco"  # My name isRicco
"My name is" +" "+ "Dulneth"
intro_string = my_age    # This is going to break
```

We can use the following *built in* functions to convert into different types:

```python
int()
float()
str()

list()
```

We can fix the example above in this way:

```python
intro_string = "My age is"
my_age = 16

print(intro_string + str(my_age))        # "My age is16"
print(intro_string + " " + str(my_age))  # "My age is 16"
print(f"{intro_string}{my_age}")        # "My age is 16"
```