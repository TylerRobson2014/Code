import cv2
from pygame import mixer

def diffImg(t0, t1, t2):
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

mixer.init()
alert=mixer.Sound('/home/steve/Downloads/beep-01a.wav')

cam = cv2.VideoCapture(0)

winName = "Movement Indicator"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

# Read three images first:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
alarm_count = 0
while True:
  cv2.imshow( winName, diffImg(t_minus, t, t_plus) )
 
  # Set threshold and maxValue
  thresh = 55
  maxValue = 255
  # Basic threshold example
  th, dst = cv2.threshold(diffImg(t_minus, t, t_plus), thresh, maxValue, cv2.THRESH_BINARY);

  if (cv2.countNonZero(dst) > 0):
	  alert.play()
	  alarm_count += 1

  # Read next image
  t_minus = t
  t = t_plus
  t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

  key = cv2.waitKey(10)
  if key == 27:
    cv2.destroyWindow(winName)
    break

print "Goodbye"
