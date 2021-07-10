from PIL import Image

in_img = Image.open("input.jpg")
width, height = in_img.size

pixels = in_img.load()

for i in range(width):
    for j in range(height):
        c_list = list(pixels[i, j])
        y = int(0.2126 * c_list[0] + 0.7152 * c_list[1] + 0.0722 * c_list[2])
        pixels[i, j] = (y, y, y)


clr_res = 256
n = 4
L = clr_res / ((n ** 2) + 1)
#d = [[0, 2], [3,1]]
d = [[0, 8, 2, 10], [12, 4, 14, 6], [3,  11, 1 ,9], [15, 7, 13, 5]]
for x in range(width):
    for y in range(height):
        c_list = list(pixels[x, y])
        i = x % n
        j = y % n
        z = int(c_list[0] / L)
        if z <= d[i][j]:
            pixels[x, y] = (255, 255, 255)
        else:
            pixels[x, y] = (0, 0, 0)






in_img.show()
#in_img.save('output.jpg')
