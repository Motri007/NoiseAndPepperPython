import cv2
import numpy as np


image_original = cv2.imread("C:\\Users\\Motri\\Documents\\GitHub\\NoiseAndPepperPython\\original.jpg")
imageBW = cv2.imread("C:\\Users\\Motri\\Documents\\GitHub\\NoiseAndPepperPython\\original.jpg",0)
imageBW = imageBW/255

cv2.imshow("original", image_original)
cv2.imshow("original black white", imageBW)
cv2.waitKey(0)
cv2.destroyAllWindows()


x,y = imageBW.shape
g = np.zeros((x,y) , dtype= np.float32)

pepper = 0.25
salt = 1 - pepper

for i in range(x):
    for j in range(y):
        rnd=np.random.random()
        if rnd < pepper:
            g[i][j] = 0
        elif rnd > salt:
            g[i][j] = 1
        else:
            g[i][j] = imageBW[i][j]

image_noisy = g
cv2.imshow('image noisy', image_noisy)
cv2.waitKey(0)
cv2.destroyAllWindows()

output_path = "C:\\Users\\Motri\\Documents\\GitHub\\NoiseAndPepperPython\\tasvir_noisy.jpg"
cv2.imwrite(output_path, image_noisy)