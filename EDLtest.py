# EDL TEST
import os
##
userName = os.path.expanduser("~")
EDL = []
EDL_file= userName + '\\Desktop\\2013_REEL.edl'
MOV_dir = 'C:\\MOV'
EDIT_dir = 'C:\\MOV\\EDIT'
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
## RUN FFMPEG DEF
def runFFMPEG(inputName, outputName, ffmpegProcess):
	FFmpeg = userName + "\\Copy\\GHOST\\CINEMATIC_SCRIPTS\\programs\\FFMPEG\\ffmpeg"
	#encode = (userName + "\\Documents\\GitHub\\JR_Project\\videoProcessing\\ffmpeg.bat "  +FFmpeg+ ' ' + inputName + ' ' + ffmpegProcess + ' '+ outputName )
	encode = (userName + "\\Documents\\GitHub\\JR_Project\\videoProcessing\\ffmpeg.bat "  + FFmpeg + '' + ffmpegProcess )	
	os.system(encode)
for i in range( len(MOV_list) ):
	in_frames = int(MOV_in[i][9:])*33.3
	out_frames = int(MOV_out[i][9:])*33.3
	#print in_frames
	#print out_frames
	if len(str(in_frames)[:-2]) == 2:
		in_frames = ''.join('0' + str(in_frames) )
	if len(str(out_frames)[:-2]) == 2:
		out_frames = ''.join('0' + str(out_frames) )
	#
	MOV_in[i] = '00' + MOV_in[i][2:-4] + '.' + str(in_frames)[:-2] # the added 00 at the start is to rule out hours added in by accident
	MOV_out[i] = '00' + MOV_out[i][2:-4] + '.' + str(out_frames)[:-2]
	MOV_newName[i] = ''.join(EDIT_dir + '\\' + MOV_newName[i])
	MOV_list[i] = ''.join(MOV_dir + '\\' + MOV_list[i])
	#print MOV_newName[i], ' new name'
	#print MOV_list[i], ' old name'
	#print MOV_in[i], 'in point'
	#print MOV_out[i], 'out point'
	#print ('-y -ss ' + MOV_in[i]+' -to '+ MOV_out[i] +' -y -vcodec prores -profile:v 0 -s hd1080')
	# CALL THE ENCODING OF ALL EDIT FILES\
	#runFFMPEG(inputName, outputName, ffmpegProcess):
	FFmpeg = userName + "\\Copy\\GHOST\\CINEMATIC_SCRIPTS\\programs\\FFMPEG\\ffmpeg"
	Action = (userName + "\\Documents\\GitHub\\JR_Project\\videoProcessing\\EDL_to_MOV.bat "  +FFmpeg+ ' ' + MOV_list[i] + ' ' + MOV_newName[i] + ' ' + MOV_in[i] + ' ' +MOV_out[i] )
	#os.system(Action)
	#encoding = [MOV_list[i] + " -ss " + MOV_in[i] +' -vcodec prores -profile:v 0 -s hd1080'+' -to '+ MOV_out[i] + ' ' + MOV_newName[i] ]
	#print encoding[0]
	#"%~2" -y -ss %~4 -to %~5 -y -vcodec prores -profile:v 0 -s hd1080 "%~3"
	#runFFMPEG(inputName = MOV_list[i], outputName = MOV_newName[i], ffmpegProcess = encoding[0] )
## WRITE NEW NAMES OUT TO TXT FILE
with open(( EDIT_dir + '\\' + 'EDL.txt'),'w') as file:
    for item in MOV_newName:
        print>>file, ('file ' + "'" + item + "'")
def stitchEdit():
	a = [' '.join(x for x in MOV_newName)]
	b = ''.join(( EDIT_dir + '\\' + 'EDIT.mov ' ) + a[0] )
	print b
	Mencoder = userName + "\\Copy\\GHOST\\CINEMATIC_SCRIPTS\\programs\\MPlayer\\mencoder"
	FFmpeg = userName + "\\Copy\\GHOST\\CINEMATIC_SCRIPTS\\programs\\FFMPEG\\ffmpeg"
	#Action = (userName + "\\Documents\\GitHub\\JR_Project\\videoProcessing\\CREATE_EDIT.bat "  +FFmpeg+ ' ' + ( EDIT_dir + '\\' + 'EDL.txt') + ' ' + ( EDIT_dir + '\\' + 'EDIT.mov' ) )
	Action = (userName + "\\Documents\\GitHub\\JR_Project\\videoProcessing\\CREATE_EDIT.bat "  +Mencoder+ ' ' + '"'+b+'"' )			
	#Action = (userName + "\\Documents\\GitHub\\JR_Project\\videoProcessing\\CREATE_EDIT.bat "  +FFmpeg+ ' ' + b + ' ' + ( EDIT_dir + '\\' + 'EDIT.mov' ) )	
	#Action = (userName + "\\Documents\\GitHub\\JR_Project\\videoProcessing\\CREATE_EDIT.bat "  +FFmpeg+ ' ' + ( EDIT_dir + '\\' + 'EDIT.mov' ) )		
	#os.system(Action)
## NOW STITCH THE FILES TOGETHER
stitchEdit()
Mencoder = userName + "\\Copy\\GHOST\\CINEMATIC_SCRIPTS\\programs\\MPlayer\\mencoder"
Action = (userName + "\\Documents\\GitHub\\JR_Project\\videoProcessing\\prores_low.bat "  +Mencoder+ ' ' + ( EDIT_dir + '\\' + 'EDIT.mov' ) + ' ' + ( EDIT_dir + '\\' + 'EDIT_v2.mov' ) )			
#Action = (userName + "\\Documents\\GitHub\\JR_Project\\videoProcessing\\CREATE_EDIT.bat "  +FFmpeg+ ' ' + b + ' ' + ( EDIT_dir + '\\' + 'EDIT.mov' ) )	
#Action = (userName + "\\Documents\\GitHub\\JR_Project\\videoProcessing\\CREATE_EDIT.bat "  +FFmpeg+ ' ' + ( EDIT_dir + '\\' + 'EDIT.mov' ) )		
os.system(Action)
#FFmpeg = userName + "\\Copy\\GHOST\\CINEMATIC_SCRIPTS\\programs\\FFMPEG\\ffmpeg"
#Action = (userName + "\\Documents\\GitHub\\JR_Project\\videoProcessing\\prores_low.bat "  +FFmpeg+ ' ' + (EDIT_dir + '\\' + 'EDIT.mov ')  + ' ' + (EDIT_dir + '\\' + 'EDIT_low.mov ')   )
#os.system(Action)
#runFFMPEG(inputName = ( EDIT_dir + '\\' + 'EDL.txt'), outputName = ( EDIT_dir + '\\' + 'EDIT.mov' ) ,ffmpegProcess = '-f concat -y -vcodec prores')