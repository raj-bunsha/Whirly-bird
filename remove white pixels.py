from PIL import Image

def convert_image(name):
	img=Image.open(f"./{name}.png").convert("RGBA")
	datas=img.getdata()
	newdata=[]
	for item in datas:
		if (item[0]>195) and (item[1]>195) and (item[2]>195):
			newdata.append((255,255,255,0))
		else:
			newdata.append((86,96,95,255))
	img.putdata(newdata)
	img.save(f"./{name}.png")
	print("successfull")

# convert_image("spring1")
# convert_image("spring2")
#convert_image("blink2")
convert_image("bird")
