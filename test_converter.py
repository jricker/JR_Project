import os
# test to see if the folder for virtual dub actually exists. If it doesn't then tell the user they cannot procede until the folder and exe are located in the proper folder son teh C drive.
toAVI = "C:\\Users\\jricker\\Copy\\R2\\CINEMATIC_SCRIPTS\\programs\\vDub\\vdub64.exe"
toMOV = "C:\\Users\\jricker\\Copy\\R2\\CINEMATIC_SCRIPTS\\programs\\FFMPEG\\ffmpeg"
compression = "C:\\Users\\jricker\\Copy\\R2\\CINEMATIC_SCRIPTS\\settings\\vDub_compression\\vDub_avi_compression.vcf"
imageSequence = "E:\\batch_test\\Shot_04_0001.tga"
outputFile = "E:\\batch_test\\Shot_04"
final = ("C:\\Users\\jricker\\Documents\\GitHub\\JR_Project\\videoProcessing\\IMG_to_AVI.bat "+ imageSequence + ' ' + compression + ' ' +toAVI + ' ' + toMOV + ' ' + outputFile)
os.system(final)