import xml.etree.ElementTree as ET
import os
import re
import shutil # this module is used to copy files across to other directories
tree = ET.parse('xml_test_06.xml')
root = tree.getroot()
############################
fileList = []
edgeList = []
folderList = []
sharedFolderList = []
directoryList = []
projectName = 'E3'
sceneAmount = 2
shotAmount = 4
for child in root:
	if child.tag == 'section':
		x = child.keys()
		for i in range(len(x)):
			pass
	for a in child:
		item = ''
		label = ''
		identity = ''
		node = ''
		if a.tag == 'section':
			x = a.keys()
			for i in range(len(x)):
				ii = a.get(a.keys()[i])
				if ii == 'node':
					identity =  a[0].text
					for b in a:
						if b.tag == 'section':
							x = b.keys()
							for i in range(len(x)):
								iii =  b.get(b.keys()[i])
								if iii == 'graphics':
									item = b[5].text
									if item == '#FFCC00':
										node = 'folder'
									elif item == '#00CC00':
										node = 'file'
									elif item == '#0099FF':
										node = 'directory'
									elif item == '#FF99CC':
										node = 'sharedFolder'
									else:
										node == 'NA'
								elif iii == 'LabelGraphics':
									label = b[0].text
								add = [identity, item, label] # collection of all of the nodes added to the scene
					if node == 'folder':
						folderList.append(add)
					elif node == 'file':
						fileList.append(add)
					elif node == 'directory':
						directoryList.append(add)
					elif node == 'sharedFolder':
						sharedFolderList.append(add)
				elif ii == 'edge':
					for b in a:
						if b.tag == 'section':
							x = b.keys()
							for i in range(len(x)):
								iii =  b.get(b.keys()[i])
								one = a[0].text
								two = a[1].text
								add = [one, two]
								edgeList.append(add)
#print 'folders = ', folderList
#print 'shared = ', sharedFolderList
#print 'files = ', fileList
#print 'dir = ', directoryList
#print 'connections = ', edgeList
def getFileExtList (dirPath,uniq=True,sorted=True):
    extList=list()
    for dirpath,dirnames,filenames in os.walk(dirPath):
        for file in filenames:
            fileExt=os.path.splitext(file)[-1]
            extList.append(fileExt)
 
    if uniq:
        extList=list(set(extList))
    if sorted:
        extList.sort()
    return extList
defaultFileLocation = "C:\\Users\\jricker\\Copy\\GHOST\\CINEMATIC_SCRIPTS\\libraries\\files"
fileLibrary = getFileExtList(defaultFileLocation)
print fileLibrary
total = []
def createTotal():
	for i in folderList:
		total.append(i)
	for i in fileList:
		total.append(i)
	for i in sharedFolderList:
		total.append(i)
createTotal()

dirTemp = []
dirFinal = []
def again(source):
	x = [i for i in total if source in i] # folder list actually needs to be the total list with files and shared folders
	if x == []: # means that you've hit zero on the list and it is the 
		pass # break out of the loop and go to the next 'i' in the edgeList loop
	else:
		dirTemp.append(x[0])
		a = [i for i in edgeList if x[0][0] in i]
		for i in a:
			if i[1] == x[0][0]:
				again(i[0])
for i in edgeList:
	lastItem = [x for x in total if i[1] in x]
	#print lastItem, ' this is lastItem'
	dirTemp.append(lastItem[0])
	again(i[0])
	dirTemp.append(['C:\Users\jricker\Desktop'])
	dirFinal.append(dirTemp)
	dirTemp = []
a = ''
counter = 0
shotCounter = 0
sceneCounter = 0
sceneList = []
shotList = []
for i in dirFinal:
	for x in reversed(i):
		if counter != 0:
			a += '\\' +x[-1]
		else:
			a += x[-1]
		counter += 1
	#if not os.path.exists(a):
	#	os.makedirs(a)
	if a[:1] == '\\':
		d =  a[1:]
	else:
		d = a
	#print d
	if '*NAME*' in d:
		d = d.replace('*NAME*', projectName)
	s = re.compile(r'/*\\') # this finds the backslashes in the to be created directory
	f = s.finditer(d)
	g = [ x.span() for x in f ]
	h= d[g[-1][0] : ][1:] # this is a long winded way, we already ahve this information when we parse the first item. Just get it from there?
	p = [x for x in fileLibrary if h.endswith((x))]
	if 'sc##' in d:
		sceneList.append(d)
		#shotList.append(d)
	else:
		eee = d
	if p != []:
		#pass
		#print h
		#print p
		#print d
		fileDirectory = d[:(-1*(len(h)) )] # finds the directory from where to copy and past it
		oldFile = defaultFileLocation + '\\' + [each for each in os.listdir(defaultFileLocation) if each.endswith(p[0])][0]
		newFile = fileDirectory + h
		#print newFile
		#print oldFile
		#if not os.path.exists(fileDirectory):
		#	os.makedirs(fileDirectory)
		#shutil.copyfile(oldFile, newFile) 
	if p == []:
		pass
		#print d
		#if not os.path.exists(d):
		#	os.makedirs(d)
	if '.' in h:
		#print h
		k = h.find('.')
		#print h[k:]
	a = ''

while sceneAmount != sceneCounter:
	sceneCounter += 1
	for i in sceneList:
		temp = i.replace('sc##', ('sc' + str(sceneCounter)) )
		shotList.append(temp)

while shotAmount != shotCounter:
	shotCounter += 1
	for i in shotList:
		temp2 = i.replace('sh##', ('sh' + str(shotCounter)) )
		print temp2