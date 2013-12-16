# EDL TEST
####################### ADD IN SOMETHING THAT CHECKS FOR THE EDL CREATION DATE - CHECK THE ORIGINAL MOV THAT IS BEING REFERENCED AND IF IT'S NEWER THAN THE EDL THAN CREATE A CUTDOWN, IF NOT, THEN DON'T AND JUST USE WHAT'S THERE INSTEAD.
import os
## VARIABLES
userName = os.path.expanduser("~")
EDL = []
EDL_file= userName + '\\Desktop\\ghost_temp2.edl'
MOV_dir = 'D:\\MOV'
EDIT_dir = 'D:\\MOV\\EDIT'
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
	MOV_newName[i] = ''.join(EDIT_dir + '\\' + MOV_newName[i])
	MOV_list[i] = ''.join(MOV_dir + '\\' + MOV_list[i])
	## CALL THE ENCODING OF ALL EDIT FILES
	FFmpeg = userName + "\\Copy\\GHOST\\CINEMATIC_SCRIPTS\\programs\\FFMPEG\\ffmpeg"
	Action = (userName + "\\Documents\\GitHub\\JR_Project\\videoProcessing\\EDL_to_MOV.bat "  +FFmpeg+ ' ' + MOV_list[i] + ' ' + MOV_newName[i] + ' ' + MOV_in[i] + ' ' +MOV_out[i] )
	os.system(Action)
"""
ONLY NEED TO ACTIVATE IF USING FFMPEG WITH CONCAT - ISSUE IS IT DOESN't ACCURETLY STITCH FRAME BY FRAME

## WRITE NEW NAMES OUT TO TXT FILE
with open(( EDIT_dir + '\\' + 'EDL.txt'),'w') as file:
    for item in MOV_newName:
        print>>file, ('file ' + "'" + item + "'")
"""
def stitchEdit(): ## WITH MENCODER INSTEAD OF FFMPEG
	a = [' '.join(x for x in MOV_newName)]	
	b = ''.join(( EDIT_dir + '\\' + 'EDIT.mov ' ) + a[0] )
	Mencoder = userName + "\\Copy\\GHOST\\CINEMATIC_SCRIPTS\\programs\\MPlayer\\mencoder"
	Action = (userName + "\\Documents\\GitHub\\JR_Project\\videoProcessing\\CREATE_EDIT.bat "  +Mencoder+ ' ' + '"'+b+'"' )			
	os.system(Action)
## NOW STITCH THE FILES TOGETHER
stitchEdit()