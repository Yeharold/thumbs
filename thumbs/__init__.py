import time as t 
import os
from PIL import Image



def getPicture():

	os.system("adb shell screencap -p /sdcard/test.png")
	os.system("adb pull /sdcard/test.png ./test.png")


def getPostion():

	''' return y  --int-- is px Y axis position
	'''

	img = Image.open("./test.png")
	px = img.load()

	for i in range(1540,1900):
		up = px[1015,i]
		down = px[1015,i+1]

		if down[0]==133 and up[0]==255:

			y = i + 24
			return y

	return "none"



def clickLike(y):
	os.system("adb shell input tap {0} {1}".format(1015,y))
	os.system("adb shell input tap {0} {1}".format(480,y))



def upPage():
	os.system("adb shell input swipe 516 1910 516 1610")



def upPagelittle():	
	os.system("adb shell input swipe 516 1910 516 1800")



def run(setting = 2):
	'''setting--int--  is loop time
	'''

	for i in range(setting):
		getPicture()
		y = getPostion()

		if y !="none" and y<1850:
			clickLike(y)
			print("ok")

		if y !="none" and y>1850:
			upPagelittle()
			getPicture()
			retry= getPostion()
			clickLike(retry)
			print("ok")

		upPage()

