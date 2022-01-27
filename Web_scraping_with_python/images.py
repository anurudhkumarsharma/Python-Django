from PIL import Image
img=Image.open('pic.jpg')
r=img.crop((1400,1000,2500,2500))
r.show()
