from PIL import Image

file = open("evil2.gfx", "rb").read()
# print(len(file.read()))
for i in range(5):
	f = open(str(i)+".jpg", "wb")
	f.write(file[i::5])
