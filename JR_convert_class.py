from JR_project_class import *
from JR_system_class import *
import binascii, re
import codecs
import shutil
import sys
import os
class Convert(System, Project): # CREATE A MASTER BAT FILE WHICH HOLDS ALL OF THE CONVERSION SCRIPTS
	def __init__(self):
		# System is already initialized in the Projects class 
		Project.__init__(self)
	def regWriter(self):
		template_reg = self.settings + '\\registry\\default_reg.reg'
		user_reg = self.settings + '\\registry\\custom_reg.reg'
		user_reg_data = codecs.open(template_reg) # type of data it needs "C:\\Users\\James\\Desktop\\test.reg"
		user_reg_lines = user_reg_data.readlines()
		new_list = []
		for i in user_reg_lines:
			x = i.strip()
			if 'USERNAME' in x:
				new_line = x.replace('USERNAME', self.userName[9:])
			else:
				new_line = x
			if '@=hex(2):' in new_line:
				new_line = new_line[:9] + self.text2regHex(new_line[9:])
			new_list.append(new_line)
		with open(user_reg,'w') as file:
		    for i in new_list:
		    	print>>file, (i)
		os.system('"''start '+user_reg+'"')
		# find a way to delete the created custom_reg file after it's used.
	def img2mov(self, input_data):
		compression = self.settings + '\\vDub_compression\\vDub_avi_compression.vcf'
		input_data = self.rename(input_data) #renames the files in case they are incorrect
		# !!
		# use an if statement instead of seperate parent name and output names. If _ in string use this, else use . for name
		output_data = input_data[:[i for i, letter in enumerate(input_data) if letter == '.'][-1] ] # find the last . in the string to create the name of the file for avi and mov output.
		parent_name = input_data[:[i for i, letter in enumerate(input_data) if letter == '_'][-1] ]
		iteration_length =  input_data[[i for i, letter in enumerate(input_data) if letter == '_'][-1] : ]
		##
		try:
			if self.findFolder(input_data, "RENDER")[0] != None:
				parent_folder = self.findFolder(input_data, "RENDER")[0]
		except TypeError:
			parent_folder = input_data[:[i for i, letter in enumerate(input_data) if letter == '\\'][-1] ]
		JPG_folder = input_data[:[i for i, letter in enumerate(input_data) if letter == '\\'][-1] ]+ '\\JPG_temp' # find the last . in the string to create the name of the file for avi and mov output.		
		if parent_folder.endswith("RENDER"): # Find the render folder, should be -5 up as the parent_folder VAR dictates
			parent_name = parent_folder + '\\01_MOV' + parent_name[[i for i, letter in enumerate(parent_name) if letter == '\\'][-1]: ]
		###
		if input_data.endswith('.exr'):
			batch_cmd = "EXR2IMG2MOV"
			iteration = '-9'
			for i in range(len(iteration_length[1:-5])):
				iteration += '0'
			JPG_output =  JPG_folder + output_data[[i for i, letter in enumerate(input_data) if letter == '\\'][-1] : ]+'.jpg'
			if not os.path.exists(JPG_folder):
				os.makedirs(JPG_folder)
			setup = (self.scripts + "\\JR_convert.bat " + batch_cmd + ' ' +  JPG_output[:-4]+'_temp_0000.jpg' + ' ' + compression + ' ' + self.vdub + ' ' + self.ffmpeg + ' ' + parent_name + ' ' + self.vlc + ' ' + self.djv + ' ' + output_data+iteration+'.exr' + ' ' + JPG_output[:-4] )
			#setup = (self.scripts + "\\JR_convert.bat " + batch_cmd + ' ' +  JPG_output[:-4]+'_reformat_00000.jpg' + ' ' + compression + ' ' + self.vdub + ' ' + self.ffmpeg + ' ' + parent_name + ' ' + self.vlc + ' ' + self.djv + ' ' + output_data+"-10000.exr" + ' ' + JPG_output[:-4] )
		else:
			batch_cmd = "IMG2MOV"
			setup = (self.scripts + "\\JR_convert.bat " + batch_cmd + ' ' +  input_data + ' ' + compression + ' ' + self.vdub + ' ' + self.ffmpeg + ' ' + parent_name + ' ' + self.vlc)
		os.system(setup)
		if os.path.exists(JPG_folder):
			shutil.rmtree(JPG_folder) # remove temp JPG folder
		# once the video is closed, open the window which houses the newly created MOV
		# check if MOV folder exists
		if os.path.exists( parent_folder+'\\01_MOV' ):
			os.system('"''start '+parent_folder+'\\01_MOV'+'"') # have to make a fix for this if it doesn't export to an MOV folder and just does it to the recent directory
	def mov2prores(self, input_data):
		batch_cmd = 'PRORES'
		output_data = input_data[:[i for i, letter in enumerate(input_data) if letter == '.'][-1] ]+'_prores.mov'
		action = (self.scripts + "\\JR_convert.bat "+ batch_cmd+ ' ' +self.ffmpeg+ ' ' +input_data+ ' ' + output_data + ' ' + str(self.prores['ProRes422_Normal']) )
		os.system(action)
	def edl2mov(self, input_data):
		batch_cmd = "MOV2CUTDOWN"
		EDL = []
		edit_folder = self.findFolder(input_data, 'EDIT')[0]
		project_folder = edit_folder[:[i for i, letter in enumerate(edit_folder) if letter == '\\'][-1] ]
		# find the MOV folder where all of the mov files are held
		for dirpath,dirnames,filenames in os.walk(project_folder):
			if dirpath.endswith('MOV'):
				if 'RENDER' in dirpath:
					mov_folder = dirpath
			if dirpath.endswith('CUTDOWNS'):
				if 'RENDER' in dirpath:
					cutdown_folder = dirpath
		MOV_file = []
		MOV_list = []
		MOV_in = []
		MOV_out = []
		MOV_newName = []
		counter = 0
		## CREATE NEW EDIT FOLDER IF IT DOESN'T EXIST ALREADY
		#if not os.path.exists(cutdown_folder):
		#	os.makedirs(cutdown_folder)
		## COLLECT FILES IN FOLDER
		for dirpath,dirnames,filenames in os.walk( mov_folder ):
			for i in filenames:
				MOV_file.append(i)
		## READ THE EDL LINE BY LINE
		with open(input_data) as fp:
		    for line in fp:
		        EDL.append(line.strip())
		## RUN THROUGH EDL AND FIND MATCHES WITH FILE LIST
		for i in range(len(EDL)):
			if [x for x in MOV_file if x in EDL[i] ]:
				counter += 1
				MOV_list.append( EDL[i][18:] )
				MOV_in.append( EDL[(i-1)][29:41] )
				MOV_out.append( EDL[(i-1)][41:53] )
				MOV_newName.append( str(counter) +'_'+ EDL[i][18:] ) 
		## RENAME ITEMS WITH DIRECTORY VALUES AND RE-CALCULATE THE FRAMES TO MILISECONDS
		for i in range( len(MOV_list) ):
			in_frames = int(MOV_in[i][9:])*33.3
			out_frames = int(MOV_out[i][9:])*33.3
			# ADD 0'S WHERE THERE ARE UNDER 3 VALUES FOR MILISECONDS
			if len(str(in_frames)[:-2]) == 2:
				in_frames = ''.join('0' + str(in_frames) )
			elif len(str(in_frames)[:-2]) == 1:
				in_frames = ''.join('00' + str(in_frames) )
			if len(str(out_frames)[:-2]) == 2:
				out_frames = ''.join('0' + str(out_frames) )
			##
			MOV_in[i] = '00' + MOV_in[i][2:-4] + '.' + str(in_frames)[:-2] # the added 00 at the start is to rule out hours added in by accident
			MOV_out[i] = '00' + MOV_out[i][2:-4] + '.' + str(out_frames)[:-2]
			MOV_newName[i] = ''.join(cutdown_folder + '\\' + MOV_newName[i])
			MOV_list[i] = ''.join(mov_folder + '\\' + MOV_list[i])
			## CALL THE ENCODING OF ALL EDIT FILES
			#Action = (self.userName + "\\Documents\\GitHub\\JR_Project\\videoProcessing\\EDL_to_MOV.bat "  +self.ffmpeg+ ' ' + MOV_list[i] + ' ' + MOV_newName[i] + ' ' + MOV_in[i] + ' ' +MOV_out[i] )
			Action = (self.scripts + "\\JR_convert.bat " + batch_cmd + ' ' +self.ffmpeg+ ' ' + MOV_list[i] + ' ' + MOV_newName[i] + ' ' + MOV_in[i] + ' ' +MOV_out[i] )
			os.system(Action)
		batch_cmd = "EDL2MOV"
		a = [' '.join(x for x in MOV_newName)]	
		b = ''.join(( edit_folder + '\\' + 'PREVIEW_EDIT.mov ' ) + a[0] )
		Action2 = (self.scripts + "\\JR_convert.bat "+ batch_cmd + ' ' +self.mencoder+ ' ' + '"'+b+'"' )
		#Action2 = (self.userName + "\\Documents\\GitHub\\JR_Project\\videoProcessing\\CREATE_EDIT.bat "  +self.mencoder+ ' ' + '"'+b+'"' )
		os.system(Action2)
		####
		"""
		ONLY NEED TO ACTIVATE IF USING FFMPEG WITH CONCAT - ISSUE IS IT DOESN't ACCURETLY STITCH FRAME BY FRAME
		
		## WRITE NEW NAMES OUT TO TXT FILE
		with open(( cutdown_folder + '\\' + 'EDL.txt'),'w') as file:
		    for item in MOV_newName:
		        print>>file, ('file ' + "'" + item + "'")
		"""
	def gxml2dir(self, xml, dir):
		pass
	def exr2img(self, input_data = 'NA', format = '.tga', size = '1920 1080'):
		batch_cmd = "EXR2IMG"
		input_data = self.rename(input_data) #renames the files in case they are incorrect
		iteration_length =  input_data[[i for i, letter in enumerate(input_data) if letter == '_'][-1] : ]
		iteration = '-9'
		for i in range(len(iteration_length[1:-5])):
			iteration+='0'
		output_data = input_data[:[i for i, letter in enumerate(input_data) if letter == '.'][-1] ]
		new_folder = input_data[:[i for i, letter in enumerate(input_data) if letter == '\\'][-1] ]+ '\\'+format[1:].upper()+'_version' # find the last . in the string to create the name of the file for avi and mov output.		
		if not os.path.exists(new_folder):
			os.makedirs(new_folder)
		new_output =  new_folder + output_data[[i for i, letter in enumerate(input_data) if letter == '\\'][-1] : ]+format
		setup = (self.scripts + "\\JR_convert.bat " + batch_cmd + ' ' + self.djv + ' ' +  output_data+iteration+'.exr' + ' ' + new_output+ ' '+ '"'+size+'"')
		os.system(setup)
	def regHex2text(self, input_data):
		if input_data.endswith('.reg'):
			reg_data = codecs.open(input_data, encoding="utf_16") # type of data it needs "C:\\Users\\James\\Desktop\\test.reg"
			reg_lines = reg_data.readlines()
			reg_list = []
			for i in range(len(reg_lines)):
				if ':' in reg_lines[i]:
					reg_list.append(i)
			reghex_read = reg_lines[reg_list[0]:]
			reghex_join = [''.join(x for x in reghex_read)]
			reghex = reghex_join[0] # the end just removes the @=hex(2) which needs to be put pack in later when writing to a .reg file
		else:
			reghex = input_data
		remove_comma = reghex.replace(',', '')
		remove_backspace = remove_comma.replace('\\', '')#.decode('hex')
		reghex_decoded = remove_backspace.replace('  ', '').decode('hex')
		regList = []
		for i in reghex_decoded:
			if i == '\x00':
				pass
			else:
				regList.append(i)
		reghex_clean = [''.join(x for x in regList)]
		text_from_hex = reghex_clean[0]
		return text_from_hex	
	def text2regHex(self, input_data):
		text_as_hex = input_data.encode('hex')
		digit_counter = 0
		hex_list = []
		for i in range(len(text_as_hex)/2 ): # JUMPING TWO SPOTS, ADDING 00 AND , TO EACH
			if digit_counter > len(text_as_hex)-2 or digit_counter == len(text_as_hex):
				pass
			else:
				o = text_as_hex[digit_counter] + text_as_hex[digit_counter+1] +','+'00' + ','
			hex_list.append(o)
			digit_counter +=2
		regHexJoin = [''.join(x for x in hex_list)]
		REGHEX_from_txt = regHexJoin[0][:-1]
		return REGHEX_from_txt
if __name__ == '__main__':
	converion = Convert()
	if sys.argv[2] == 'IMG2MOV':
		converion.img2mov(sys.argv[1])
	elif sys.argv[2] == 'RENAME':
		converion.rename(sys.argv[1])
	elif sys.argv[2] == 'PRORES':
		converion.mov2prores(sys.argv[1])
	elif sys.argv[2] == 'EXR2IMG':
		converion.exr2img(input_data = sys.argv[1])
	elif sys.argv[2] == 'MOV2CUTDOWN':
		pass
	elif sys.argv[2] == 'EDL2MOV':
		converion.edl2mov(sys.argv[1])
	else:
		pass
	#converion.regWriter()