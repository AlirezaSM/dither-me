from PIL import Image
import numpy as np
import math


def main():

    in_img = Image.open(input("[INPUT] Enter the address of an image: "))
    convert_to_grayscale(in_img)
    ordered_dithering(in_img)

    in_img.show()
    in_img.save('output.jpg')


def ordered_dithering(img):
    width, height = img.size
    pixels = img.load()
    n = 0

    while True:
        n = int(input("[INPUT] Enter size of dithering matrix - must be power of two (enter 2 for 2X2 matrix): "))
        if math.log(n, 2).is_integer():
            break
        else:
            print("[ERROR]: Size of matrix must be power of two")

    clr_res = 256
    L = clr_res / ((n ** 2) + 1)
    d = build_dithering_matrix(n)

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


def convert_to_grayscale(img):
    width, height = img.size
    pixels = img.load()

    for i in range(width):
        for j in range(height):
            c_list = list(pixels[i, j])
            y = int(0.2126 * c_list[0] + 0.7152 * c_list[1] + 0.0722 * c_list[2])
            pixels[i, j] = (y, y, y)


def build_dithering_matrix(size):
    if size == 2:
        return np.array([[0, 2],
                         [3, 1]])
    m0 = np.multiply(build_dithering_matrix(size / 2), 4)
    m1 = np.add(np.multiply(build_dithering_matrix(size / 2), 4), 2)
    m2 = np.add(np.multiply(build_dithering_matrix(size / 2), 4), 3)
    m3 = np.add(np.multiply(build_dithering_matrix(size / 2), 4), 1)

    return np.concatenate((np.concatenate((m0, m1), axis=1), np.concatenate((m2, m3), axis=1)))


if __name__ == '__main__':
    main()