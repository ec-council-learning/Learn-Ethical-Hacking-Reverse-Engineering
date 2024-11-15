# trims left, right, top, bottom
from PIL import Image
import math

WHITE = (255, 255, 255)
filename = 'captcha3.png'
image = Image.open(filename)
image = image.convert('RGB')
img2 = image.copy()
croparray = []
w, h = img2.size

def cropimg(left, right, top_and_bottom, image_to_crop):
  top, bottom = top_and_bottom
  croparray.append(image_to_crop.crop((left,top,right,bottom)))
  

def showimages():
  img2.show()
  for i in croparray:
    i.show()

def saveImages():
  t = 0
  for i in croparray:
    t += 1
    i.save('c' + str(t) + '.png')

def getTopAndBottom(imgCenter, img):
    for y in range(h-1, 0, -1):
        px = img.getpixel((math.floor(imgCenter), y))
        if px != WHITE:
            break
    bottom = y
    for y in range(0, h):
        px = img.getpixel((math.floor(imgCenter), y))
        if px != WHITE:
            break
    top = y
    return top, bottom

def startcrop():
  print('w: {} h: {}'.format(w, h))

  x_left = 5
  x_right = 0

  isdrawn = False
  for x in range(0, w):
    for y in range(0, h):
      px = img2.getpixel((x, y))
      if px != WHITE:
        isdrawn = False
        break
      elif isdrawn == False and x > 27 and y > 20:
        if y == 39: 
          isdrawn = True
          x_right = x
          x_left = x_right - 17
          imgCenter = (x_right - x_left)/2 + x_left
          cropimg(x_left, x_right, getTopAndBottom(imgCenter, img2), img2)
          x_left = x_right

startcrop()
# showimages()
saveImages()
