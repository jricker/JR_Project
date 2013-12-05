import os
# test to see if the folder for virtual dub actually exists. If it doesn't then tell the user they cannot procede until the folder and exe are located in the proper folder son teh C drive.
location = "C:\\Users\\James\\Documents\\GitHub\\JR_Project\\videoProcessing\\goPro_compression.vcf"
b = 'D:\\projects\\gamescom\\jpgs\\00.jpg'
a= ("C:\\Users\\James\\Documents\\GitHub\\JR_Project\\videoProcessing\\sequence_to_avi.bat "+ b + ' ' + location)
print a
os.system(a)