import cv2
import numpy as np

def create_img(width, height):
     return np.zeros((width, height, 3), dtype = np.uint8)


def polarization(img):
    new_img = create_img(np.shape(img)[0], np.shape(img)[1])
    lenY, lenX = img.shape[ :-1]
    for line in range(lenY):
        for stolb in range(lenX):
            if img[line][stolb][0] > 150:
                s = [255, 255, 255]
            else:
                s = [0, 0, 0]
            new_img[line][stolb] = np.array(s)
    return new_img

image = cv2.imread('variant-10.jpg')
new_img = polarization(image)
cv2.imshow('new_img', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()