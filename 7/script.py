from PIL import Image

im = Image.open("oxygen.png")
# im.show()
# print(im.height, im.width)

for x in range(0, im.width, 7):
	r, g, b, a = im.getpixel((x, im.height//2))
	if(r == g and g == b):
		print(chr(r), end='')

print()

## After running the above script we get this list [105, 110, 116, 101, 103, 114, 105, 116, 121]
a = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join([chr(x) for x in a]))