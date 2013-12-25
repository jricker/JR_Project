from JR_project_class import *
from JR_system_class import *
import binascii, re
import codecs
import os
class Convert(System, Project): # CREATE A MASTER BAT FILE WHICH HOLDS ALL OF THE CONVERSION SCRIPTS
  def __init__(self):
    pass
    # init system and projects shared variables
  def img2mov(self, input_data, output_data):
    if input_data.endswith('.exr'):
      pass
    else:
      pass
  def mov2prores(self, input_data):
    pass
  def edl2mov(self, edl):
    pass
  def gxml2dir(self, xml, dir):
    pass
  def exr2img(self, format, size):
    pass
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

#print text2regHex('"%CPYW%" "C:\Users\jricker\Documents\GitHub\JR_Project\JR_ui_xml.py"')
#print regHex2text(text2regHex('"%CPYW%" "C:\Users\jricker\Documents\GitHub\JR_Project\JR_ui_xml.py"') )
# these were the old test functions
"""
reg_file = codecs.open("C:\\Users\\James\\Desktop\\test.reg", encoding="utf_16")
readText = reg_file.readlines()
hexList = []
for i in range(len(readText)):
	if ':' in readText[i]:
		hexList.append(i)
hexLine = readText[hexList[0]:]
hexJoin = [''.join(x for x in hexLine)]
HEX = hexJoin[0]
#print HEX
###
text_data = '"%CPYW%" "C:\Users\jricker\Documents\GitHub\JR_Project\JR_ui_xml.py"'
text_as_hex = text_data.encode('hex')
digit_counter = 0
regHEX_list = []
for i in range(len(text_as_hex)/2 ): # JUMPING TWO SPOTS, ADDING 00 AND , TO EACH
  if digit_counter > len(text_as_hex)-2 or digit_counter == len(text_as_hex):
    pass
  else:
    o = text_as_hex[digit_counter] + text_as_hex[digit_counter+1] +','+'00' + ','
  regHEX_list.append(o)
  digit_counter +=2
regHexJoin = [''.join(x for x in regHEX_list)]
REGHEX = regHexJoin[0][:-1]
###
#print 'this is hex:', REGHEX
remove_comma = REGHEX.replace(',', '')
remove_backspace = remove_comma.replace('\\', '')#.decode('hex')
regHex_to_text = remove_backspace.replace('  ', '').decode('hex')
textList = []
for i in regHex_to_text:
  if i == '\x00':
    pass
  else:
    textList.append(i)
FINAL = [''.join(x for x in textList)]
#print 'this is txt:', FINAL[0]
"""