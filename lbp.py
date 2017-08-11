#!/usr/bin/env python
import numpy as np
import cv2
from matplotlib import pyplot as plt

####################################
histograma = [0 for i in range (0,256)]

print ('I AM READING THE IMAGE')
img = cv2.imread('Lenna.png', 0)
line = img.shape[0]
column = img.shape[1]
print line
print column
print ('IMAGE READED')
print histograma
imgOut = []
for i in range (0, line):
    imgOut_vector = [0 for i in range (0,column)]
    imgOut.append(imgOut_vector)

for i in range (1, line - 1):
	sum = 0
	for j in range (1, column - 1):
		if (img[i][j] < img[i-1][j-1]):
			sum += 1
		if (img[i][j] < img[i-1][j]):
			sum += 2
		if (img[i][j] < img[i-1][j+1]):
			sum += 4
		if (img[i][j] < img[i][j-1]):
			sum += 8
		if (img[i][j] < img[i][j+1]):
			sum += 16
		if (img[i][j] < img[i+1][j-1]):
			sum += 32
		if (img[i][j] < img[i+1][j]):
			sum += 64
		if (img[i][j] < img[i+1][j+1]):
			sum += 128
		histograma[sum] = histograma[sum] + 1
		imgOut[i][j] = sum
		sum = 0
plt.imshow(imgOut, cmap='gray')
plt.show()
x = range(0,256)
y = histograma

plt.figure(figsize=(16, 8))
plt.subplot(121),plt.imshow(imgOut, cmap = 'gray')
plt.title('LBP')
plt.subplot(122),plt.plot(x,y)
plt.title('Histogram')

plt.show()
