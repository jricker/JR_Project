from JR_project_class import *
from JR_system_class import *
import binascii, re
import codecs
import os
class Convert(System, Project): # CREATE A MASTER BAT FILE WHICH HOLDS ALL OF THE CONVERSION SCRIPTS
	def __init__(self):
		pass
	def img2mov(self, input_data):
		if input_data.endswith('.exr'):
			batch_cmd = "IMG2MOV2EXR"
			output_data = input_data[:-3] + '.jpg'
			self.exr2img(input_data, output_data, 'jpg', ('1920x1080') )
			#setup = (self.scripts + "\\IMG_to_AVI.bat " + batch_cmd + ' ' + self.DJV + ' ' +  input_data + ' ' + compression + ' ' + self.VDUB + ' ' + self.FFMPEG + ' ' + output_data)
		else:
			batch_cmd = "IMG2MOV"
			setup = (self.scripts + "\\IMG_to_AVI.bat " + batch_cmd + ' ' + self.DJV + ' ' +  input_data + ' ' + compression + ' ' + self.VDUB + ' ' + self.FFMPEG + ' ' + output_data)
		os.system(setup)
	def mov2prores(self, input_data):
		pass
	def edl2mov(self, edl):
		pass
	def gxml2dir(self, xml, dir):
		pass
	def exr2img(self, input_data, output_data, format, size):
		batch_cmd = "EXR2IMG"
		setup = (self.scripts + "\\JR_convert.bat " + batch_cmd + ' ' + self.DJV + ' ' +  input_data + ' ' + compression + ' ' + self.VDUB + ' ' + self.FFMPEG + ' ' + output_data)
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