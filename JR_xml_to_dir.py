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
iii = [directoryList[0][0], '#0099FF', 'C:\\Test']
folderList.append(iii)
numbers = []
#print folderList
for x in edgeList:
	for y in x:
		print y
		numbers.append(y)
numbers = set(numbers); numbers = list(numbers); numbers = sorted(numbers)
print numbers
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
