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
a = np.zeros((x,y) , dtype= np.float32)

# salt and pepper
# nose 10% pepper=0.5
# nose 25% pepper=0.125
# nose 50% pepper=0.25
pepper = 0.25
salt = 1 - pepper

# sakht salt and pepper
for i in range(x):
    for j in range(y):
        rnd=np.random.random()
        if rnd < pepper:
            a[i][j] = 0
        elif rnd > salt:
            a[i][j] = 1
        else:
            a[i][j] = imageBW[i][j]


image_noisy = a
cv2.imshow('image noisy', image_noisy)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save image
output_path = "C:\\Users\\Motri\\Documents\\GitHub\\NoiseAndPepperPython\\tasvir_noisy.jpg"
cv2.imwrite(output_path, image_noisy)