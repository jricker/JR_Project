import xml.etree.ElementTree as ET
tree = ET.parse('xml_test_04.xml')
root = tree.getroot()
############################
fileList = []
edgeList = []
folderList = []
sharedFolderList = []
directoryList = []
for child in root:
	if child.tag == 'section':
		x = child.keys()
		for i in range(len(x)):
			pass
			#print '>', child.get(child.keys()[i])
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
					#print '    >>', ii
					#print '        >>> id =', a[0].text
					for b in a:
						if b.tag == 'section':
							x = b.keys()
							for i in range(len(x)):
								iii =  b.get(b.keys()[i])
								#print '        >>>', iii
								if iii == 'graphics':
									item = b[5].text
									#print '        >>> colour =', b[5].text
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
									#print '        >>> label =', b[0].text
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
					#print '    >>', ii
					for b in a:
						if b.tag == 'section':
							x = b.keys()
							for i in range(len(x)):
								iii =  b.get(b.keys()[i])
								one = a[0].text
								two = a[1].text
								add = [one, two]
								edgeList.append(add)
								#print '        >>> source = ', a[0].text
								#print '        >>> target = ', a[1].text
#print 'folders = ', folderList
#print 'shared = ', sharedFolderList
#print 'files = ', fileList
#print 'dir = ', directoryList
#print 'connections = ', edgeList
#iii = [directoryList[0][0], '#0099FF', 'C:\\Test']
#folderList.append(iii)

#for i in edgeList:
#	for x in folderList:
#		if i[1] == x[0]:
#			print x[2]

#path = []
#for i in edgeList:
#	temp = ''
#	if i[0] == directoryList[0][0]: # we've reached the last connection
#		temp += directoryList[0][2] + '\\'
#		temp += str([i for i in folderList if i[1] in i][0][2])
#		path.append(temp)
#print path
"""
def path(number):
	if int(number) != 0:
		x = [i for i in folderList if number in i]
		y = [i for i in edgeList if x[0][0] in i]
		#print y[0][0], ' this is y'
		#print x[0][0], ' this is x'
		path(y[0][0])
	else:
		print 'next'

for i in edgeList:
	print i
	path(i[0])
"""
dirTemp = []
dirFinal = []
def again(source):
	x = [i for i in folderList if source in i]
	if x == []:
		pass
		#print 'next'
	else:
		#print x[0][0], 'xxxxx'
		dirTemp.append(x[0])
		a = [i for i in edgeList if x[0][0] in i]
		#print a[0][0]
		again(a[0][0])

	#print x
for i in edgeList:
	#print i
	lastItem = [x for x in folderList if i[1] in x]
	dirTemp.append(lastItem[0])
	again(i[0])
	dirTemp.append(['C:'])
	dirFinal.append(dirTemp)

	dirTemp = []
a = ''
for i in dirFinal:
	for x in reversed(i):
		a += x[-1] + '\\'
	print a
	a = ''
	#print folderList
	#a = [x for x in folderList if i[0] in x]
	#print a
	#if i[0] == 'yes':
	#	print 'yes'
	#else:
	#	print 'no'
	#if i[0] in [x for x in folderList][0]


"""
end = directoryList[0][0]
pathList = []
def pp(sourceNumber):
	return [i for i in folderList if sourceNumber in i][0][2]
def pathFinder():
	a = ''
	#return [i for i in folderList if sourceNumber in i][0][2]
	for i in edgeList:
		print 'went through'
		source = i[0]
		print source, '   source #'
		if i[0] != end:
			if i[1] == source:
				pass
			else:
				print pp(i[1]), '  pathfinder', i
				a += pp(i[1])
			a += pp(i[0])
			a += '//'
		#pathList.append(a)
	print pathList
#
pathFinder()
"""


"""
we have the connections
go through each connections

now check in each one, the id # in the target

for i in edgeList:
	if i[0] == directoryList[0][0]: # we've reached the last connection
		path += [i for i in folderList if i[1] in i][0][2]
		path += folderList[0] + folderList[1]
		print path
		this is the directory so we can stop the filepath name
	else:
		run a function()


end = directoryList[0][0]
for i in edgeList:
	source = i[1]
	if i[0] != end:
		if i[0] == source:
			pass
		else:
			a += pathFinder(i[1])
		a += pathFinder(i[0])
print a
#
def pathFinder(sourceNumber):
	return [i for i in folderList if i[sourceNumber] in i][0][2]

	source = [i for i in edgeList if i[1] in i][0][2]
		path += 


"""
#xx = [i for i in folderList if '2' in i][0][2]
#print xx
#numbers = []
#print folderList
#for x in edgeList:
#	for y in x:
#		print y
#		numbers.append(y)
#numbers = set(numbers); numbers = list(numbers); numbers = sorted(numbers)
#print numbers
#for i in range( len(numbers) ):
#	if numbers[i] in folderList[0]:
#		print 'yes'
#		print folderList[0]

#for i in edgeList:
#	print i
#	for x in edgeList:
#		if i[1] in x:
#			print x[1], ' x1'
#			for y in folderList:
#				if x[1] == y[0]:
#					print y[2]
#temp = []
#temp.append(folderList); temp.append(sharedFolderList); temp.append(fileList)
#temp2 = [x for x in temp if x != []] 
#assets = temp2[0]
#print assets
#master = directoryList[0][0]
##print master
#for i in edgeList:
#	print i
#	if master in i[0]:
#		print 'yes'
#		for x in assets:
#			#print x
#			if x[0] == i[1]:
#				print ' doubel yes'
		#if i[1] in total:
		#	print 'yes'
#for i in edgeList:
#	#print i
#	x = i[0]
#	y = i[1]
#	print x, y
#	for a in total:
#		for b in a:
#			#print 
#			if b[0] == master:
#				print '........this is the dir'
#			elif b[0] == x:
#				print b[2], ' is the source'
#				#print a
#				if a == total[0]:
#					print 'its directory'
#				elif a == total[1]:
#					print 'its folder'
#				elif a == total[2]:
#					print 'its sharedFolder'
#				elif a == total[3]:
#					print 'its a file'
#			if b[0] == y:
#				print b[2], ' is the target'
			#print x
			#print b[0], 'this'
	#for a in folderList:
	#	if a[0] == x:
	#		print a[2], 'this is the main'
	#	if a[0] == y:
	#		print a[2], 'this is new'
	#print 'build ', folderList[int(y)][2],  'in',  folderList[int(x)][2]
