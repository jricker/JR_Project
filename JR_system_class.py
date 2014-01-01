import os
class System():
    def __init__(self):
        ## MASTER PATHS 
        self.userName = os.path.expanduser("~")
        self.systemLocation = self.userName + '\\Copy\\GHOST\\CINEMATIC_SCRIPTS\\'
        ## PROGRAMS
        self.vlc = '"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"'
        self.djv = '"C:\\Program Files (x86)\\djv 0.8.3\\bin\\djv_convert"'
        self.ffmpeg = self.systemLocation + "programs\\FFMPEG\\ffmpeg"
        self.vdub = self.systemLocation + "programs\\vDub\\vdub64.exe"
        self.mencoder = self.systemLocation + "programs\\MPlayer\\mencoder"
        ## FOLDER LOCATIONS
        self.images = self.systemLocation + "images"
        self.files = self.systemLocation + "files"
        self.scripts = self.systemLocation + "scripts"
        self.settings = self.systemLocation + "settings"
        self.sequences = self.systemLocation + "test\\sequences"
        ## SETTINGS
        self.prores = {'ProRes422_Proxy': 0, 'ProRes422_LT':1, 'ProRes422_Normal':2, 'ProRes422_HQ':3 }
    def systemStart(self, app):
        os.system('"''start '+app+'"')
    def findFolder(self, input_data, folderName):
        if folderName in input_data:
            ii = input_data.find(folderName)
            pp = [i for i, letter in enumerate(input_data) if letter == '\\']
            high = [x for x in pp if x > ii]
            low = [x for x in pp if x < ii]
            return input_data[:high[0]], input_data[low[-1]+1:high[0]]
    def rename(self, input_data):
        #print input_data
        file_path = input_data[:[i for i, letter in enumerate(input_data) if letter == '\\'][-1]+1]
        # find folder to isolate first _sh folder
        try:
            if self.findFolder(file_path, '_sh')[1] != None:
                new_name = self.findFolder(file_path, '_sh')[1]
        except TypeError:
            # for now we'll keep with the initial name of the frames, just in case someone has already labeled these nicely and watns to keep them.
            # IN THE FUTURE, let's create a rename dialogue box
            temp = input_data[: [i for i, letter in enumerate(input_data) if letter == '.'][-1] ] # +1
            new_name = temp[[i for i, letter in enumerate(temp) if letter == '\\'][-1]+1 :]
            new_name = new_name[:[i for i, letter in enumerate(new_name) if letter == '_'][-1]]
        # if '1K' in file_path:
        #     new_name = new_name + '_1K'
        # elif '2K' in file_path:
        #     new_name = new_name + '_2K'
        # elif '4K' in file_path:
        #     new_name = new_name + '_4K'
        if file_path[[i for i, letter in enumerate(file_path) if letter == '\\'][-2]:][1] == 'v': # find out if this is in a version folder or not
            # if it is attach it to the new name var
            new_name = new_name + '_' + file_path[[i for i, letter in enumerate(file_path) if letter == '\\'][-2]:][1:-1]
        shot_path = input_data[:[i for i, letter in enumerate(input_data) if letter == '\\'][-3]+1]
        file_name_full = input_data[[i for i, letter in enumerate(input_data) if letter == '\\'][-1]+1 :] # +1
        file_extension = input_data[[i for i, letter in enumerate(input_data) if letter == '.'][-1] :] # +1
        # find iterator placement
        if '_' in file_name_full:
            file_name = file_name_full[:[i for i, letter in enumerate(file_name_full) if letter == '_'][-1] ]
    	else:
            file_name = file_name_full
        fileList = []
        os.chdir(file_path)
        for files in os.listdir("."):
            if file_name in files:
                fileList.append(files)
        iterator = -1
        new_return = [] # this is for the return so the mov converters know what it is now
        for x in sorted(fileList):
            iterator +=1
            if len(str(iterator)) == 1:
                padding = '000'
            elif len(str(iterator)) == 2:
                padding = '00'
            elif len(str(iterator)) == 3:
                padding = '0'
            else:
                padding = ''
            y = new_name + '_' + padding + str(iterator) + file_extension
            old = file_path + x
            new = file_path + y
            #print x, 'to .. ', y
            new_return.append(new)
            os.rename(old, new)
        return new_return[0]