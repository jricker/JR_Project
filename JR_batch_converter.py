import os
import JR_convert_class
import shutil
convert = JR_convert_class.Convert()
directory = "\\\\eucr-fs1.eu.ad.ea.com\\Studio\\HawaiiMarketing\\CINEMATICS\\JUPITER NFS14\\0022 DLC_Koenig\\03_RENDER"
#directory = "C:/Users/jricker/Documents/Ghost Games/Need for Speed(TM) Rivals/Screenshots"
screenshotDirectory = []
movList = []
newMovDir = []
finalSet = []
def getFileExtList (dirPath,uniq=True,sorted=True):
    for dirpath,dirnames,filenames in os.walk(dirPath):
        for file in filenames:
            #fileExt=os.path.splitext(file)[-1]
            if 'Screenshot' in file:
            	screenshotDirectory.append(dirpath)
def findScreenshots():
	getFileExtList(directory)
	a = set(screenshotDirectory)
	finalSet.append( sorted(a) )
def findMovies (dirPath,uniq=True,sorted=True):
    for dirpath,dirnames,filenames in os.walk(dirPath):
        for file in filenames:
            if file.endswith('.mov'):
            	movList.append(dirpath + '\\' + file)
            	newMovDir.append(directory + '\\' + file)
findScreenshots()
#for i in finalSet[0]:
#	print i
#findMovies(directory)
for i in movList:
	print i
def createMOV():
	for i in finalSet[0]:
		firstImage = ''
		for dirpath,dirnames,filename in os.walk(i):
			for file in filename:
				if 'Screenshot' in file:
					firstImage = file
					break
       		item = i+'\\'+firstImage
       	print item
       		#convert.img2mov(item)
def moveMovies():
	for i in range(len(movList)):
		shutil.move(movList[i], newMovDir[i])
#moveMovies()
createMOV()