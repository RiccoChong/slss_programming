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
    num = num_stars * int
    return num

stars(2)   # **
stars(10)   # **********
print_area_of_a_square(12.2)
print_area_of_a_square(13)
# sum_areas = area_of_a_square(12.2) + area_of_a_square(13)
print(area_of_a_square(2))

print(print_area_of_a_square(2))