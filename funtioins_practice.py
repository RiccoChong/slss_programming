# Functions Practice
# Author: Ricco
# 24 November 2023


def print_area_of_a_square(sidelength: float) -> None:
    """Calculates the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square"""

    area = sidelength**2

    print(
        f"The area of a square with side length = {sidelength} is: {area} square units"
    )


def area_of_a_square(sidelength: float) -> float:
    """Returns the area of a square with given
    sidelength

    Params:

    sidelength - length of one side of a square
    """
    area = sidelength**2

    return area

def stars(num_stars: int) -> str:
    """"""
    num = num_stars 
    print(f"There are {num} amount of stars")
    return num

stars(1)
print_area_of_a_square(12.2)
print_area_of_a_square(13)
# sum_areas = area_of_a_square(12.2) + area_of_a_square(13)
print(area_of_a_square(2))

print(print_area_of_a_square(2))


def linear_search(l: list, item: any) -> int:
    """Search through a list and if found,
    returns the index of the first occurence
    of the item.

    Params:
            l - list we're search through
            item - item we're looking for

    Returns:
            index if found, -1 if not found
    """
    counter = 0

    # search algorithm
    for thing in l:
        if thing == item:
            return counter
        counter += 1

    return -1


pockets = ["coins", "lint", "paperclip", "keys", "wallet"]

results = linear_search(pockets, "keys")

if results == -1:
    print("Your keys are not in your pockets")
else:
    print(f"Found your keys! They're in the {results}th index.")


