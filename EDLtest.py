# EDL TEST
import os
##
EDL = []
EDL_file= 'C:\Users\jricker\Desktop\ghost_temp2.edl'
MOV_dir = 'D:\MOV'
EDIT_dir = 'D:\MOV\EDIT'
MOV_file = []
MOV_list = []
MOV_in = []
MOV_out = []
MOV_newName = []
counter = 0
## CREATE NEW EDIT FOLDER IF IT DOESN'T EXIST ALREADY
if not os.path.exists(EDIT_dir):
	os.makedirs(EDIT_dir)
## COLLECT FILES IN FOLDER
for dirpath,dirnames,filenames in os.walk( MOV_dir ):
	for i in filenames:
		MOV_file.append(i)
## READ THE EDL LINE BY LINE
with open(EDL_file) as fp:
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
	#
	MOV_in[i] = MOV_in[i][:-4] + '.' + str(in_frames)[:-2]
	MOV_out[i] = MOV_out[i][:-4] + '.' + str(out_frames)[:-2]
	MOV_newName[i] = ''.join(EDIT_dir + '\\' + MOV_newName[i])
	MOV_list[i] = ''.join(MOV_dir + '\\' + MOV_list[i])
	#print MOV_newName[i], ' new name'
	#print MOV_list[i], ' old name'
	print MOV_in[i], ' in point'
	print MOV_out[i], ' out point'
	# CALL THE ENCODING OF ALL EDIT FILES
	FFmpeg = "C:\\Users\\jricker\\Copy\\GHOST\\CINEMATIC_SCRIPTS\\programs\\FFMPEG\\ffmpeg"
	Action = ("C:\\Users\\jricker\\Documents\\GitHub\\JR_Project\\videoProcessing\\EDL_to_MOV.bat "  +FFmpeg+ ' ' +MOV_list[i]+ ' ' +MOV_newName[i]+  ' ' +MOV_in[i]+ ' ' +MOV_out[i] )
	os.system(Action)
## WRITE NEW NAMES OUT TO TXT FILE
with open(( EDIT_dir + '\\' + 'EDL.txt'),'w') as file:
    for item in MOV_newName:
        print>>file, ('file ' + "'" + item + "'")
##
def stitchEdit():
	FFmpeg = "C:\\Users\\jricker\\Copy\\GHOST\\CINEMATIC_SCRIPTS\\programs\\FFMPEG\\ffmpeg"
	Action = ("C:\\Users\\jricker\\Documents\\GitHub\\JR_Project\\videoProcessing\\CREATE_EDIT.bat "  +FFmpeg+ ' ' + ( EDIT_dir + '\\' + 'EDL.txt') + ' ' + ( EDIT_dir + '\\' + 'EDIT.mov' ) )
	os.system(Action)
stitchEdit()