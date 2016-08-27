#!/usr/bin/python
## This is an example of a simple sound capture script.
##
## The script opens an ALSA pcm for sound capture. Set
## various attributes of the capture, and reads in a loop,
## Then prints the volume.
##
## To test it out, run it and shout at your microphone:

import time, audioop
import matplotlib.pyplot as plt
import alsaaudio, struct
from aubio import *
import pygame.camera
import pygame.image
import numpy as np


# Open the device in nonblocking capture mode. The last argument could
# just as well have been zero for blocking mode. Then we could have
# left out the sleep call in the bottom of the loop
# constants
inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)

# Set attributes: Mono, 8000 Hz, 16 bit little endian samples
inp.setchannels(1)
inp.setrate(8000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(160)
# set up pitch detect
#detect = new_aubio_pitchdetection(FRAMESIZE,FRAMESIZE/2,CHANNELS,
#                                  RATE,PITCHALG,PITCHOUT)
#buf = new_fvec(FRAMESIZE,CHANNELS)

pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()


capture = []
count = 0
running = True
while running:
	# read data from audio input
	[l, data]=inp.read()
	count += 1
	if count > 10000: running = False
	if l:
		# Return the maximum of the absolute value of all samples in a fragment.
		capture.append( audioop.max(data, 2) )
		#if audioop.max(data, 2) > np.mean(capture)+np.std(capture):
			#img = cam.get_image()
			#filename = "photo"+str(count)+".bmp"
		#	print np.mean(capture),np.std(capture)
			#pygame.image.save(img, filename)

	time.sleep(.001)
	
pygame.camera.quit()
plt.plot(capture)
plt.show()
plt.plot(np.fft.rfft(capture))
plt.show()

    

