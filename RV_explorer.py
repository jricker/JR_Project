# -*- coding: utf-8 -*-

"""
A script that figures out a file sequence from a single file name
and loads up the whole sequence in RV.

Version: 0.3, 27.11.2012
-- fixed an issue with reading sequences of different number of leading zeros denomination

Version: 0.2, 29.07.2012
-- added jump to frame feature

Version: 0.1, 27.06.2012
-- this script created, loocas

(c) 2012 Lukas Dubeda, duber studio, www.duber.cz, info@duber.cz
"""

import getopt
import glob
import os
import re
import sys
import subprocess

# this method searches the given file name and tries to find a match for the regular expression pattern.
# if it finds one, it replaces it with a wildcard character, if not, it leaves it as it was
def findSequence(selFile, rePattern, loadSingle):
	reRes = rePattern.search(selFile)
	
	if reRes != None:
		selFrame = int(reRes.group(0))
		wildcardFileName = re.sub(rePattern, '*', selFile)
		#firstFrame = int((rePattern.search((glob.glob(wildcardFileName))[0])).group(0))
		#lastFrame = int((rePattern.search((glob.glob(wildcardFileName))[-1])).group(0))
		#subString = r'{0}-{1}{2}'.format(firstFrame, lastFrame, ('@'*len(reRes.group(0))))
		subString = '@'*len(reRes.group(0))
		if len(glob.glob(wildcardFileName)) > 1 and loadSingle != True:
			return (re.sub(rePattern, subString, selFile), selFrame)
		else:
			return (selFile, None)
	else:
		return (selFile, None)

# this method takes the correctly formatted input file and fires up RV via RVPUSH passing it the selected file
# or file sequence
def callRV(seq, positionPlayer):
	print "args:", seq, "position player:", positionPlayer
	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	#rvpush mu-eval 'rvui.clearEverything(); addSource("myMovie.mov"); setFrame(50);'
	subprocess.call(['rvpush', 'set', seq[0]], startupinfo=startupinfo)

# just a usage method, mostly for remembering what the 
def usage():
	usageStr = """Pass in the file name and arguments. -p for positioning the player at the exact
	frame you selected and -s for ignoring file sequences and loading up only the one selected file.
	-h invokes this help explicitly"""
	
	print usageStr

# the main method that gets executed at the begining.
def main(args):
	#rvpush = r"path_to_executable" # you can specify your own rvpush executable here, if you want to.
	rePattern = re.compile(r'(([0-9]+)(?=(\.[a-zA-Z0-9]{1,3})$))') # a RE pattern used for figuring out the file sequence from a single file
	selFile = args[1]
	positionPlayer = False
	loadSingle = False
	
	try:
		opts, args = getopt.getopt(args[2:], 'psh', ['position', 'single', 'help'])
	except getopt.GetoptError:
		usage()
		sys.exit(2)

	for opt, arg in opts:
		if opt in ('-h', '--help'):
			usage()
			sys.exit()
		elif opt in ('-p', '--position'):
			positionPlayer = True
		elif opt in ('-s', '--single'):
			loadSingle = True
		else:
			assert False, 'unhandled option'

	callRV(findSequence(selFile, rePattern, loadSingle), positionPlayer)

if __name__ == '__main__':
	#main(['scriptName', r'D:\Mountfield_Benzin\SHOTS\MF_BE_M4\PLATE\MF_BE_M4_00.tif', '-p']) # for testing purposes only
	#main(['scriptName', r'D:\Mountfield_Benzin\SHOTS\MF_BE_PV\RENDERS\2D_OUT\MF_BE_PV_KROVINOREZ_0001.jpg', '-p'])
	
	main(sys.argv)