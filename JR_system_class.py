import os
class System():
	def __init__(self):
        ## MASTER PATHS 
    	self.userName = os.path.expanduser("~")
    	self.systemLocation = self.userName + '\\Copy\\GHOST\\CINEMATIC_SCRIPTS\\'
        ## PROGRAMS
    	self.VLC = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
    	self.DJV = "C:\\Program Files (x86)\\djv 0.8.3\\bin\\djv_convert"
        self.FFMPEG = self.systemLocation + "programs\\FFMPEG\\ffmpeg"
    	self.VDUB = self.systemLocation + "programs\\vDub\\vdub64.exe"
        ## FOLDER LOCATIONS
    	self.images = self.systemLocation + "images"
    	self.files = self.systemLocation + "files"
        self.scripts = self.systemLocation + "scripts"
    def rename(self):
    	pass