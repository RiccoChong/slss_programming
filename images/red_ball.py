# Red Ball
# Name: Ricco Chong
# Date: jan 12 2023

from PIL import Image
import colour_helper

red_ball_img = Image.open("./Images/Red Ball.jpeg")

red_pixels = []


# Visit every pixel
for y in range(red_ball_img.height):
    for x in range(red_ball_img.width):
        # get the pixels information
        current_pixel = red_ball_img.getpixel((x,y))
        # Find the red pixels
        if colour_helper.pixel_to_name(current_pixel) == "red":
            # Store its location somewhere
            red_pixels.append((x, y))

orig_image_width = jelly_bean_img.width
orig_image_height = jelly_bean_img.height

blue_pixel_map = Image.new("RGB", (orig_image_width, orig_image_height))

# For every pixel location in the red_pixels list
    # place a red pixel at that location
for pixel_loc in blue_pixels:
    blue_pixel_map.putpixel(pixel_loc, BLUE_PIXEL)

# save the image
blue_pixel_map.save("./images/blue_pixel_map.jpg")
blue_pixel_map.close()

# Count all the locations of red pixels
red_pixel_count = len(red_pixels)
green_pixel_count = len(green_pixels)
blue_pixel_count = len(blue_pixels)
total_pixels = jelly_bean_img.width * jelly_bean_img.height
