import sys
import os
from functools import partial
from Tkinter import *
from tkFileDialog import askopenfilename, askdirectory
class Directory():
	def __init__(self):
		self.tk = Tk()
		self.directoryValue = ''
		self.xmlValue = ''
		self.projectValue = ''
		self.sceneValue = ''
		self.shotValue = ''
	def Run(self):
		self.tk.geometry('200x160+600+300')
		#self.tk.iconbitmap(default='transparent.ico')
		#TITLE
		self.tk.title('XML>DIR')
		# COLOURS
		bgColour = '#2f2f2f'
		self.btnColour2 = '#098400'
		input_bgColour = '#cecece'
		input_fgColour = 'black'
		# LABELS
		labelOffset = 25
		project = Label(text = 'Project :', bg = bgColour, fg = 'white').place(x=8, y=5)
		scene = Label(text = 'Scene :', bg = bgColour, fg = 'white').place(x=14, y=5+labelOffset)
		shots = Label(text = 'Shots :', bg = bgColour, fg = 'white').place(x=15.5, y=30+labelOffset)
		## INPUT FIELDS
		self.project_field = Entry(bg = input_bgColour, fg=input_fgColour, bd = 0)
		self.scene_field = Entry(bg = input_bgColour, fg=input_fgColour, bd = 0)
		self.shot_field = Entry(bg = input_bgColour, fg=input_fgColour, bd = 0)
		self.project_field.configure(text = 'test')
		# INPUT FIELD POSITION
		self.project_field.place(x=60, y= 8)
		self.scene_field.place(x=60, y= 8+labelOffset )
		self.shot_field.place(x=60, y=33 + labelOffset )
		# BUTTONS
		self.directoryBtn = Button(text = 'DIR', bg = bgColour, fg = 'white', width = 200 , command = partial(self.assignValues, 'DIR') )
		self.XMLBtn = Button(text = 'XML', bg = bgColour, fg = 'white', width = 200 , command = partial(self.assignValues, 'XML') )
		self.buildBtn = Button(text = 'BUILD', bg = bgColour, fg = 'white', width = 200 , command = partial(self.buildDirectory) )
		# BUTTON POSITION
		self.buildBtn.pack(side = 'bottom' )
		self.XMLBtn.pack(side = 'bottom' )
		self.directoryBtn.pack(side = 'bottom' )
		# FILE OPTIONS
		self.file_opt = options = {}
		#options['defaultextension'] = '.txt'
		options['filetypes'] = [ ('XML Files', '.xml')]
		#print self.file_opt
		#options['initialdir'] = 'C:\\'
		#options['initialfile'] = 'myfile.txt'
		#options['parent'] = root
		#options['title'] = 'This is a title'
		# FINAL CONFIGURATIONS
		self.tk.configure(background= bgColour)
		self.tk.bind('<Escape>', quit) # BIND TO ESC KEY
		self.tk.mainloop()
	def assignValues(self, value):
		if value == 'XML':
			filename = askopenfilename(**self.file_opt)
			self.xmlValue = filename
			if filename == '':
				pass
				#self.warningMessage('Please Select an XML')
			else:
				self.XMLBtn.configure(bg = self.btnColour2 )
		elif value == 'DIR':
			directory = askdirectory()
			self.directoryValue = directory
			if self.directoryValue == '':
				pass
			else:
				self.directoryBtn.configure(bg = self.btnColour2 )
	def warningMessage(self, comment):
		w=Toplevel()
		w.iconify()
		var = StringVar()
		note = Message( w, textvariable=var, relief=RAISED )
		var.set(comment)
		note.pack()
	def buildDirectory(self):
		self.projectValue = self.project_field.get()
		self.sceneValue = self.scene_field.get()
		self.shotValue = self.shot_field.get()
		if self.projectValue == '':
			print 'Please type in project name'
		elif self.directoryValue == 'None':
			print 'Please select Directory'
		elif self.xmlValue == 'None':
			print 'Please select XML location'
		elif self.sceneValue == '' or self.sceneValue == '0':
			print 'Please enter a scene amount'
		elif self.shotValue == '' or self.shotValue == '0':
			print 'Please enter a shot amount'
		else:
			print ' starting '
		dirs = 'C:\Users\jricker\Desktop\hello'
		if not os.path.exists(dirs):
			os.makedirs(dirs)
		else:
			print 'already exists'
	def __call__(self):
		pass
if __name__ == '__main__':
	K = Directory()
	K.Run()
	#self.Run()
#main(['scriptName', r'D:\Mountfield_Benzin\SHOTS\MF_BE_M4\PLATE\MF_BE_M4_00.tif', '-p']) # for testing purposes only
#main(['scriptName', r'D:\Mountfield_Benzin\SHOTS\MF_BE_PV\RENDERS\2D_OUT\MF_BE_PV_KROVINOREZ_0001.jpg', '-p'])
	
	#main(sys.argv)
#K = Directory()
#K.Run()