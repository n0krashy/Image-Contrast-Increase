from skimage import io
import numpy as np

img = io.imread('Ocean.bmp')


def inc_contrast(o_img, A, B, C, D):
    slope1 = B/float(A)
    # slope1 = B / A
    slope2 = (D-B)/float(C-A)
    slope3 = (255-D)/float(255-C)
    r = o_img.shape[0]
    k = o_img.shape[1]
    contrasty_img = np.zeros((r, k), dtype=np.uint8)
    for i in range(r):
        for j in range(k):
            # check on which line the pixel lies
            if o_img[i, j] <= A:
                m = slope1
                c = B - m * A
                c = 0
            elif o_img[i, j] <= C:
                m = slope2
                c = B - m * A
            else:
                m = slope3
                c = D - m * C
            # apply contrast for the pixel
            contrasty_img[i, j] = m * o_img[i, j] + c
    # return the result image
    return contrasty_img


def show_img(im):
    io.imshow(im)
    io.show()


def save_img(im, name):
    io.imsave(name, im)


# question 2 tests
manipulated_img = inc_contrast(img, 30, 20, 180, 230)
show_img(manipulated_img)
save_img(manipulated_img, 'Ocean_1.bmp')

manipulated_img = inc_contrast(img, 70, 20, 140, 240)
show_img(manipulated_img)
save_img(manipulated_img, 'Ocean_2.bmp')
