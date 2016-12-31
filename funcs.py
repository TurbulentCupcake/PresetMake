# This is the accompanying functions file where
# we declare and define all necessary fucntions
# required by the exec.py program
import os


# the presets class gets data from the checkFile function
# and reads the data of the textfile into 
# the correct variables
# filename :  contains the name of the file
# editlines : has the lines we need to edit
# contains the presets 
# code : contains the code we need to edit

class presets:
    def __init__(self):
        self.filename = None
        self.pno = None
        self.editline = None
        self.presetCode = []
    def setfilename(self,filename):
        self.filename = filename
    def setpno(self, pno):
    	self.pno = pno
    def setlines(self, editline):
    	self.editline = editline
    def addpresetCode(self, code):
    	self.presetCode.append(code)


def checkFile(filename):
	# check if the file exists, if it does, then load
	# its presets. If it doesn't, create a preset
	# file with the filename
    if not os.path.exists('presets/%s.preset'%(filename)):
		print "Existing preset does not exist\n"
		print "Creating a new preset\n"
		open('presets/%s.preset'%(filename),'w+')
		return False
    else:
		with open('presets/%s.preset'%(filename),'r') as fp:
			# presetInfo holds the preset information
			# about a file if it is found.
			presetInfo = fp.readlines()
			presetInfo = [x[1:len(x)-1] for x in presetInfo]
			print presetInfo

			# # iterate through the presetInfo list and
			# # add each preset
			presetList = []

			if presetInfo[0] == 'PRESETS':
				for info in presetInfo[1:]:
					if info[0:3] == 'PNO':
						p = presets()
						p.setfilename(filename)
						p.setpno(int(info[-1]))
						presetList.append(p)
					elif info[0:4] == 'LINE':
						p.setlines(int(info[-1]))
					else:
						p.addpresetCode(info)

			return presetList


def setPreset(filename, presets):
	f = open('%s'%(filename))
	codeLines = f.readlines()
	# codeLines = [code[:len(code)-1] for code in codeLines]
	print codeLines
	print "Enter preset number : "
	presetNumber = int(raw_input(">>>"))
	if not presetNumber in [p.pno for p in presets]:
		print "Preset Number Not Found"
	else:
		for pos in range(presets[presetNumber].editline, presets[presetNumber].editline + len(presets[presetNumber].presetCode),1):
			#codeLines[pos] = presets[presetNumber].presetCode[pos] + '\n'
			print pos
			codeLines[pos] = presets[presetNumber].presetCode[pos - presets[presetNumber].editline + 1]

		# fp = open(filename,'w')
		# fp.write(codeLines)
		# print presets[presetNumber].editline
		print codeLines



	

	

