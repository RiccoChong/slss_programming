# Colour Helper
# Functions that help wither colours


def pixel_to_name(pixel: tuple) -> str:
    """Given a 3-tuple, return a string representing
    its colour

    Params:
        pixel = 3-tuple of values (red, green, blue)

    Returns:
        name of the colour
    """
    red, green, blue = pixel

    # TODO: detect jelly bean green
    if red < 200 and blue < 200 and green > 220:
        return "green"
    elif red > 170 and green < 60 and blue < 60:
        return "red"
    elif red < 60 and green > 80 and blue < 60:
        return"jelly bean green"
    elif red < 80 and green > 60 and blue > 150:
        return "jelly bean blue"
    else:
        return "colour unknown"


print(pixel_to_name((180, 3, 2)))
print(pixel_to_name((255, 255, 255)))


def is_light(pixel: tuple) -> bool:
    """Returns True if the pixel is a "light" pixel

    Params:
        pixel - 3-tuple of values r, g, b

    Returns:
        True if the pixel is a light pixel
        False if a dark pixel
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    average = (red + green + blue) / 3

    if average >= 128:
        return True
    else:
        return False


def pixel_to_grayscale(pixel: tuple) -> tuple:
    """Return a gray version of the given pixel"""
    red, green, blue = pixel

    gray = int(red * 0.3 + green * 0.59 + blue * 0.11)

    return (gray, gray, gray)


def pixel_to_random_effect(pixel: tuple) -> tuple:
    """Return a random pixel"""
    red, green, blue, red1 = pixel

    red += 30
    green += 50
    blue -= 10
    red1 += 240

    if red > 255:
        red = 255
    if green > 255:
        green = 255
    if blue < 0:
        blue = 0
    if 240 <= red1:
        red1<= 250

    return (red, green, blue, red1)