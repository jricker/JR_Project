import binascii, re
import codecs
### THIS IS IMPORTING A REG FILE, READING IT, DECOND, AND YOU CAN THEN USE THE BELOW METHOD TO EXTRACT THE TEXT FROM THE HEX
def regHex2text(input_data):
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
#regHex2text("C:\\Users\\James\\Desktop\\test.reg")
#regHex2text('22,00,25,00,43,00,50,00,59,00,57,00,25,00,22,00,20,00,22,00,43,00,3a,00,5c,00,55,00,73,00,65,00,72,00,73,00,5c,00,6a,00,72,00,69,00,63,00,6b,00,65,00,72,00,5c,00,44,00,6f,00,63,00,75,00,6d,00,65,00,6e,00,74,00,73,00,5c,00,47,00,69,00,74,00,48,00,75,00,62,00,5c,00,4a,00,52,00,5f,00,50,00,72,00,6f,00,6a,00,65,00,63,00,74,00,5c,00,4a,00,52,00,5f,00,75,00,69,00,5f,00,78,00,6d,00,6c,00,2e,00,70,00,79,00,22,00')
def text2regHex(input_data):
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
  #print  regHex2text(REGHEX_from_txt) #REGHEX_from_txt


print text2regHex('"%CPYW%" "C:\Users\jricker\Documents\GitHub\JR_Project\JR_ui_xml.py"')
print regHex2text(text2regHex('"%CPYW%" "C:\Users\jricker\Documents\GitHub\JR_Project\JR_ui_xml.py"') )


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