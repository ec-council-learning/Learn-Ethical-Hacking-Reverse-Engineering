from PIL import Image

img = Image.open('captcha3.png')
img = img.convert('RGB')
img.show()

width, height = img.size
print('width: {}, height:{}'.format(width,height))

for x in range(0, width):
    px = img.getpixel((x,20))
    print('x: {}, px: {}'.format(x,px))