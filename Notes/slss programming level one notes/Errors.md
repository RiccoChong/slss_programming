# Syntax Errors

syntax = errors
- These types of errors are ones that occur when you run your code and then it breaks
- Syntax Errors are relatively easy to spot and fix
- Syntax errors occur when we don't follow the rules of the language completely
# Semantic Errors

- Semantic errors occur when our code doesn't ***MEAN*** what we intend it to ***MEAN***.
- These errors, in Mr. Ubial's opinion are ***FAR MORE*** challenging to spot and fix.

```python
user_response = input("Do you like to eat foor? ")

if user_response.lower() == "yes":
	print("You are a human. ")
else:
	print("You must be some sort of robot. ")
```

- The problem with the code above is subtle. What i (Ricco) mean is that EVERY ENSWER OF YES should go into the YES block.
one wat to solve this problem is to user [[Strings#String Methods]]

