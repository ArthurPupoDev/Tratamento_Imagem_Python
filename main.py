import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
from matplotlib.pyplot import imshow

img = Image.open('stiloso.jpg')

img_arr = np.asanyarray(img)
plt.imshow(img_arr[:,:,2], cmap='gray')
#plt.show()

img_cinza = cv2.imread('stiloso.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow("img cinzinha",img_cinza)
cv2.waitKey()

img_color = cv2.imread('stiloso.jpg')

img_color_convert = cv2.cvtColor(img_color, cv2.COLOR_BGR2YCrCb)

img_color_convert[:,:,0]=cv2.equalizeHist(img_color_convert[:,:,0])

img_equalizada_color = cv2.cvtColor(img_color_convert, cv2.COLOR_YCrCb2BGR)


img_blur = cv2.GaussianBlur(img_cinza,(15,15),0)
cv2.imshow("blur cinza", img_blur)
cv2.waitKey()

img_equalizada = cv2.equalizeHist(img_blur)
cv2.imshow("Equalizada Cinza",img_equalizada)
cv2.waitKey()

cv2.imshow("Equalizada Color",img_equalizada_color)
cv2.waitKey()

img_concat = cv2.hconcat([img_cinza,img_blur,img_equalizada, img_equalizada_color])

cv2.imshow("teste",img_concat)
cv2.waitKey()

#cv2.waitKey()








