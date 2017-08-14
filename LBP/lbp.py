#!/usr/bin/env python

#===========================================#
#                                           #
#   Aprendizado de Maquina - LBP filter     #
#   Nome:  Fernando Claudecir Erd           #
#   GRR20152936                             #
#                                           #
#===========================================#

import numpy as np
import cv2
import sys
from matplotlib import pyplot as plt

histogram = [0 for i in range (0,256)]

#Read Image
try:
    img = cv2.imread(sys.argv[1], 0)
    line = img.shape[0]
    column = img.shape[1]
except:
    print 'Faltou argumentos, use ./lbp.py <image>'
    exit()

#Generate matrix output
imgOut = []
for i in range (0, line):
    imgOut_vector = [0 for i in range (0,column)]
    imgOut.append(imgOut_vector)

#LBP algorithm 
for i in range (1, line - 1):
	sum = 0
	for j in range (1, column - 1):
		if (img[i][j] >= img[i-1][j-1]):
			sum += 1
		if (img[i][j] >= img[i-1][j]):
			sum += 2
		if (img[i][j] >= img[i-1][j+1]):
			sum += 4
		if (img[i][j] >= img[i][j-1]):
			sum += 8
		if (img[i][j] >= img[i][j+1]):
			sum += 16
		if (img[i][j] >= img[i+1][j-1]):
			sum += 32
		if (img[i][j] >= img[i+1][j]):
			sum += 64
		if (img[i][j] >= img[i+1][j+1]):
			sum += 128
		histogram[sum] = histogram[sum] + 1
		imgOut[i][j] = sum
		sum = 0

#Plot images
x = range(0,256)
y = histogram
fig = plt.figure()
ax1 = fig.add_subplot (2,2,1)
ax1.set_title('before LBP')
ax1.imshow(img, cmap = 'gray')
ax2 = fig.add_subplot (2,2,2)
ax2.set_title('after LBP')
ax2.imshow(imgOut, cmap = 'gray')
ax3 = fig.add_subplot(2,1,2)
ax3.set_title ('Histogram')
ax3.plot(x,y, 'r-')
plt.show()
