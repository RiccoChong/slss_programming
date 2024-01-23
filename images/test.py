from PIL import Image
def find_center():
    img = Image.open("./Images/Red Ball.jpeg")
    img_mtx = img.load()
    top = bottom = 0
    first_row = True
    # First we find the top and bottom border of the object
    for row in range(img.size[0]):
        for col in range(img.size[1]):
            if img_mtx[row, col][0:3] != (255, 255, 255):
                bottom = row
                if first_row:
                    top = row
                    first_row = False
    middle_row = (top + bottom) / 2  # Calculate the middle row of the object
    left = right = 0
    first_col = True
    # Scan through the middle row and find the left and right border
    for col in range(img.size[1]):
        if img_mtx[middle_row, col][0:3] != (255, 255, 255):
            left = col
            if first_col:
                right = col
                first_col = False
    middle_col = (left + right) / 2  # Calculate the middle col of the object
    return (middle_col, middle_row)
print(find_center())