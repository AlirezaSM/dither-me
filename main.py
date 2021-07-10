from PIL import Image

in_img = Image.open("input.jpg")
width, height = in_img.size

pixels = in_img.load()

for i in range(width):
    for j in range(height):
        c_list = list(pixels[i, j])
        y = int(0.2126 * c_list[0] + 0.7152 * c_list[1] + 0.0722 * c_list[2])
        pixels[i, j] = (y, y, y)

in_img.show()
in_img.save('output.jpg')
