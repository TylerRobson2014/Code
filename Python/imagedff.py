from __future__ import division
import random as r
import numpy as np
import cv2
from matplotlib import pyplot as plt
import pygame.camera
import pygame.image

#pygame.camera.init()
#cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
#cam.start()
#img = cam.get_image()
#filename = "photo2.bmp"
#pygame.image.save(img, filename)
#cam.stop()
#pygame.camera.quit()

img = cv2.imread('photo2.bmp',0)
# fft to convert the image to freq domain 
f = np.fft.fft2(img)

# shift the center
fshift = np.fft.fftshift(f)

rows, cols = img.shape
crow,ccol = rows/2 , cols/2

# remove the low frequencies by masking with a rectangular window of size 60x60
# High Pass Filter (HPF)
win = 40
fshift[crow-win:crow+win, ccol-win:ccol+win] = 0

# shift back (we shifted the center before)
f_ishift = np.fft.ifftshift(fshift)

# inverse fft to get the image back 
img_back = np.fft.ifft2(f_ishift)

img_back = np.abs(img_back)

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Fianl Result'), plt.xticks([]), plt.yticks([])

plt.show()

