# Function questions
# Author: Ricco
# Date Nov 27

# QUESTION ONE
def stars(num_stars: int) -> str:
    return "*" * num_stars

print(stars(5))

# QUESTION TWO

def biggest_of_three(num_one: float, num_two: float, num_three: float) -> float:
    """Returns the biggest of three given numbers.

    Params:
    num_one - the first number
    num_two - the second number
    num_three - the third number

    Returns:
    the biggest of the three numbers
    """
    if num_one > num_two and num_one > num_three:
        return num_one
    elif num_two > num_three:
        return num_two
    else:
        return num_three
    
# QUESTION 3

def pyramid(num_layers: int) -> None:
    """Prints out a pyramid of given number of layers.

    Params:
    num_layers - number of layers in the pyramid
    """

    for current_layer in range(1, num_layers + 1):
        print(stars(current_layer))


pyramid(2)
pyramid(3)
pyramid(20)

# QUESTION 4

def pyramid_mirror(num_layers: int) -> None:
    """Print a pyramid mirrored of given number
    of layers.

    Params:
    num_layers - number of layers in the pyramid
    """

    for current_layer in range(1, num_layers + 1):
        # Spaces is equal to total num of layers
        # minus the stars in the current layer
        spaces = " " * (num_layers - current_layer)

        print(spaces + stars(current_layer))


pyramid_mirror(2)
pyramid_mirror(3)
pyramid_mirror(20)