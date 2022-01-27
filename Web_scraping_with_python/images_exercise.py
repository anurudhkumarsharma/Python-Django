from re import I
from PIL import Image
a=Image.open('word_matrix.png')
b=Image.open('mask.png')
c=b.resize((1015, 559))
c.putalpha(170)
a.paste(c,(0,0),c)
a.show()




