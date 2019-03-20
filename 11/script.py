from PIL import Image

im = Image.open("cave.jpg")
odd = Image.new("RGB", (im.width//2, im.height//2))
even = Image.new("RGB", (im.width//2, im.height//2))

for i in range(im.width):
	for j in range(im.height):
		p = im.getpixel((i, j))
		if (i+j)%2 == 0:
			even.putpixel((i//2, j//2), p)
		else:
			odd.putpixel((i//2, j//2), p)

even.save("even.jpg")
odd.save("odd.jpg")