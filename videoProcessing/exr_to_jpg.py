import OpenEXR
import Imath
import datetime
from PIL import Image
import array
import sys
import os, os.path

def ConvertEXRToJPG(exrfile, jpgfile):
	File = OpenEXR.InputFile(exrfile)
	PixType = Imath.PixelType(Imath.PixelType.FLOAT)
	DW = File.header()['dataWindow']
	Size = (DW.max.x - DW.min.x + 1, DW.max.y - DW.min.y + 1)
	#
	jpgW = 1280
	jpgH = 720
	#
	RedStr = File.channel('R', PixType)
	GreenStr = File.channel('G', PixType)
	BlueStr = File.channel('B', PixType)

	Red = array.array('f', RedStr)
	Green = array.array('f', GreenStr)
	Blue = array.array('f', BlueStr)

	for I in range(len(Red)):
		Red[I] = EncodeToSRGB(Red[I])

	for I in range(len(Green)):
		Green[I] = EncodeToSRGB(Green[I])

	for I in range(len(Blue)):
		Blue[I] = EncodeToSRGB(Blue[I])

	rgbf = [Image.fromstring("F", Size, Red.tostring())]
	rgbf.append(Image.fromstring("F", Size, Green.tostring()))
	rgbf.append(Image.fromstring("F", Size, Blue.tostring()))

	rgb8 = [im.convert("L") for im in rgbf]
	#Image.merge("RGB", rgb8).save(jpgfile, "JPEG", quality=50)
	Image.merge("RGB", rgb8).resize((jpgW, jpgH), Image.NEAREST).save(jpgfile, "JPEG", quality=100)

def EncodeToSRGB(v):
	if (v <= 0.0031308):
		return (v * 12.92) * 255.0
	else:
		return (1.055*(v**(1.0/2.4))-0.055) * 255.0
a = "C:\\EXR\\test_01.exr"
b = "C:\\EXR\\test_jpeg_01.jpg"
#
location = "C:\\EXR\\"
path = os.listdir(location)
jpgPath = location + 'JPG\\'
#
if not os.path.exists(jpgPath):
	os.makedirs(jpgPath)
print datetime.datetime.now()
for name in path:
	if name.endswith((".exr")):
		EXR = location + name
		JPG = jpgPath + name[:-4] +'.jpg'
		ConvertEXRToJPG(EXR, JPG)
	else:
		print name, 'these are not exr files'
#print len([name for name in os.listdir('.') if os.path.isfile(name)])
#ConvertEXRToJPG(a, b)
print datetime.datetime.now()