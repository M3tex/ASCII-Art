from PIL import Image
import numpy as np


# Opening the image and converting it to a 2D array containing triplets of RGB values
image_name = input("Which image would you like to open? ")
with Image.open(image_name) as im:
    print("Before: ", im.size, im.mode)
    im = im.convert('RGB')

    maxW = int(input("Max width: "))
    mode = int(input("Mode (1 for normal, 0 for reverse): "))
    k =  maxW / im.size[0]

    # Resizing the image to a given max width so it can fit in the terminal
    im = im.resize((int(k * im.width), int(k * im.height)))
    width, height = im.size
    print("After: ", im.size)
    im_arr = np.array(im)

# Converting the triplets of RGB values to a brightness number
# We'll use this formula: B = (0.2126*R + 0.7152*G + 0.0722*B) (found on StackOverflow)
result = []
for i, row in enumerate(im_arr):
    result.append([])
    for j, col in enumerate(row):
        B = (0.2126*col[0] + 0.7152*col[1] + 0.0722*col[2])
        result[i].append(B)

result = np.array(result)

# These are sorted from brightest to darkest
chars = ' `^\\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

# We write the result to a text file
with open("result.txt", "w") as f:
    for i in range(height):
        for j in range(width):
            if not mode:
                idx = int(result[i][j] / np.around(255 / len(chars), 15))
            else:
                idx = -int(result[i][j] / np.around(255 / len(chars), 15)) - 1
            f.write(2 * chars[idx])
        f.write('\n')
        

