import os
# test to see if the folder for virtual dub actually exists. If it doesn't then tell the user they cannot procede until the folder and exe are located in the proper folder son teh C drive.
toAVI = "C:\\Users\\jricker\\Copy\\GHOST\\CINEMATIC_SCRIPTS\\programs\\vDub\\vdub64.exe"
toMOV = "C:\\Users\\jricker\\Copy\\GHOST\\CINEMATIC_SCRIPTS\\programs\\FFMPEG\\ffmpeg"
compression = "C:\\Users\\jricker\\Copy\\GHOST\\CINEMATIC_SCRIPTS\\settings\\vDub_compression\\vDub_avi_compression.vcf"
imageSequence = "D:\\EXR\\test_01.jpg" #"E:\\batch_test\\Shot_04_0001.tga"
outputFile = "D:\\EXR\\test"#E:\\batch_test\\Shot_04"
#EDL READING
## When reading EDL use 33.3 as a mutiplyer for frame values.
editIN = "00:00:00.266" 
editOUT = "00:00:01.133"
final = ("C:\\Users\\jricker\\Documents\\GitHub\\JR_Project\\videoProcessing\\IMG_to_AVI.bat "+ imageSequence + ' ' + compression + ' ' +toAVI + ' ' + toMOV + ' ' + outputFile + ' ' + editIN + ' ' + editOUT )
os.system(final)
#"%~4" -i "%~5.avi" -c:v libx264 -preset slow -s hd1080 -crf 20 -c:a libvo_aacenc -b:a 128k "%~5_H264.mp4" - THESE ARE THE DEFAULT ENCODING COMMANDS
#"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe" "%~5_H264.mov" - PUT THIS BACK IN AT THE END AFTER DELETING THE AVI
# "%~4" -i "%~5.avi" -vcodec prores -s hd1080 -bits_per_mb 4000 "%~5_ProRes.mov"   THIS IS FOR A PRORES VERSION


