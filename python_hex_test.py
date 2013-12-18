import binascii, re
import codecs
def asciirepl(match):
  # replace the hexadecimal characters with ascii characters
  s = match.group()  
  return binascii.unhexlify(s)  

def reformat_content(data):
  p = re.compile(r'\\x(\w{2})')
  return p.sub(asciirepl, data)
hex_string = "220025004300500059005700250022002000220043003a005c00550073006500720073005c006a007200690063006b00650072005c0044006f00630075006d0065006e00740073005c004700690074004800750062005c004a0052005f00500072006f006a006500630074005c004a0052005f00750069005f006d00610069006e002e007000790022000000"
ascii_string = reformat_content(hex_string)
b = "22,00,25,00,43,00,50,00,59,00,57,00,25,00,22,00,20,00,22,00,43,00,3a,\
  00,5c,00,55,00,73,00,65,00,72,00,73,00,5c,00,6a,00,72,00,69,00,63,00,6b,00,\
  65,00,72,00,5c,00,44,00,6f,00,63,00,75,00,6d,00,65,00,6e,00,74,00,73,00,5c,\
  00,47,00,69,00,74,00,48,00,75,00,62,00,5c,00,4a,00,52,00,5f,00,50,00,72,00,\
  6f,00,6a,00,65,00,63,00,74,00,5c,00,4a,00,52,00,5f,00,75,00,69,00,5f,00,6d,\
  00,61,00,69,00,6e,00,2e,00,70,00,79,00,22,00,00,00"
a = b.replace(',', '')
c = a.replace('\\', '')#.decode('hex')
d = c.replace('  ', '').decode('hex')
f = []
g = []
for i in d:
	if i == '\x00':
		pass
	else:
		f.append(i)
y = [''.join(x for x in f)]
print y[0]
text_file = codecs.open("C:\\Users\\jricker\\Desktop\\test.reg", encoding="utf_16")
ccc = text_file.readlines()
hexList = []
for i in range(len(ccc)):
	if ':' in ccc[i]:
		hexList.append(i)
final = ccc[hexList[0]:]
ff = ''
for i in final:
	print i
	#print i
	#ff = ff.join(str(i))
print ff
#a = hex_string.decode('utf-8')
#print ascii_string