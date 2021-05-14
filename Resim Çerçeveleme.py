import cv2
import numpy as np
from matplotlib import pyplot as plt


mavi = [0,0,255] ## mavi renk olması için

img = cv2.imread('opencv.png')

replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT101)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=mavi)# burda renk tonu kullanarak istediğimiz çerçeve rengi veriyoruz.
## çerçeve çeşitleri içerdeki 10 10 değerlerde yandan üstten felan ne kadar piksel olcağaı dışa doğru resmin devamına ekler

plt.subplot(231),plt.imshow(img,'gray'),plt.title('orjinal')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('replicate')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('reflect')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('reflect101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('wrap')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('constant')
## plt.subplot(231) burda 231 2 satır 3 stundan oluşcak şekilde resimleri koyması için
plt.show()# bu sayede hepsini toplu bi şekilde çıkarırız


#cv2.imshow('orjinal',img)
#cv2.imshow('constant',constant)
cv2.waitKey(0)
cv2.destroyAllWindows()
