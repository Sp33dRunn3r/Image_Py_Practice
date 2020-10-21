# Images

from PIL import Image, ImageFilter
img = Image.open('./Pokedex/pikachu.jpg')

#Filters:
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", 'png')
filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("smooth.png", 'png')
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("sharpen.png", 'png')
#//////////////////////////////////////
filtered_img = img.convert('L')
filtered_img.save("grey.png", 'png')



# print(dir(img))

print(img.format)
print(img.size)
print(img.mode)

from PIL import Image, ImageFilter
img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.convert('L')

#filtered_img.show() - Show the image preview

crooked = filtered_img.rotate(180)
resize = filtered_img.resize((300, 300))
region = filtered_img.crop((100, 100, 400, 400))

region.save("grey.png", 'png')

from PIL import Image, ImageFilter
img = Image.open('./astro.jpg')
img.thumbnail((400, 400))
img.save('thumbnail.jpg')
