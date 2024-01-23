# Format Strings
We can evaluate inside of strings using f-string.
To create an f-string, we put an f before the opening quote.

```python
fave_food = input("what's your favourite food?")
print (f"Ooooooo, {fave_food} sounds good.)
```

# String Methods

- [[Methods]] are functions that we can use on Objects.
- Sting methods allow us to modify and work with strings.

- Say for example, we want to make all characters of a string lowercase
```python
	mr_ubial_yelling = "PLEASE PUSH YOUR CHAIRS IN"
print(mr_ubial_yelling.lower()   #lowercases the letters
```

## `.lower()`

- The ``.lower()`` method takes a string and converts all UPPERCASE characters to lowercase.
- We can use .lower() to help with [[Errors#Semantic Errors]]

## `.upper()`
The `.upper()` method converts all lowercase characters to uppercase in a string

## `.strip(str)`
- The `.strip()` method removes characters from the beginning and end of the string

```python
user_feeling = input ("How are you feeling? ")

# "good" "Good" "GOOD" "GOOD!" "good." "good?"
if user_feeling.lower().strip("!.,?") == "good":
	print("that's great! ")
```

## `.split(str) -> List`
The `.split()` method splits a string into a [[List]], separating the string based on the characters you give it

```python
grocrey_str = "eggs milk cheese hotwheels"

grocery_str = grocery_str.split(" ")
```
