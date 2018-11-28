from PIL import Image
import urllib.request
# urllib.request.urlretrieve("http://www.pythonchallenge.com/pc/def/oxygen.png", 'level7.png')

im = Image.open('python challenge/level7.png')

pixel = [im.getpixel((x, im.height/2)) for x in range(im.width)]
# print(pixel)
pixel = pixel[::7]
print(pixel)
grey_pixel = [p for p in pixel if p[0]==p[1]==p[2]]
print(grey_pixel)
grey_pixel_num = [gp[0] for gp in grey_pixel]
print(grey_pixel_num)

print(''.join(list(map(chr, grey_pixel_num))))
#105, 110, 116, 101, 103, 114, 105, 116, 121
next_lvl = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join(list(map(chr, next_lvl))))
# integrity
