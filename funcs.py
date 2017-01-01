# This is the accompanying functions file where
# we declare and define all necessary fucntions
# required by the exec.py program
import os
import sys


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
		print "Existing preset file does not exist"
		print "Creating a new preset file.."
		open('presets/%s.preset'%(filename),'w+')
		print "Would you like to add a new preset?"
		choice = raw_input("Enter y or n:")
		if choice == 'y':
			addPreset(filename)
		elif choice == 'n':
			print "Exiting"
			exit(0)
		else:
			print "Invalid option, Exiting"
			exit(0)
		return None
    else:
		with open('presets/%s.preset'%(filename),'r') as fp:
			# presetInfo holds the preset information
			# about a file if it is found.
			presetInfo = fp.readlines()
			presetInfo = [x[1:len(x)-1] for x in presetInfo]
			# print presetInfo

			# # iterate through the presetInfo list and
			# # add each preset
			presetList = []

			if presetInfo[0] == 'PRESETS':
				for info in presetInfo[1:]:
					if info[0:3] == 'PNO':
						p = presets()
						p.setfilename(filename)
						p.setpno(int(info.split('=')[-1]))
						presetList.append(p)
					elif info[0:4] == 'LINE':
						p.setlines(int(info.split('=')	[-1]))
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
	print [p.pno for p in presets]
	if not presetNumber in [p.pno for p in presets]:
		print "Preset Number Not Found"
	else:
		for pos in range(presets[presetNumber-1].editline, presets[presetNumber-1].editline + len(presets[presetNumber-1].presetCode),1):
			#codeLines[pos] = presets[presetNumber].presetCode[pos] + '\n'
			print pos
			codeLines[pos-1] = presets[presetNumber-1].presetCode[pos - presets[presetNumber-1].editline] + '\n'

		fp = open('trial.txt','w')
		for c in codeLines:
			fp.write(c)
		# print presets[presetNumber].editline
		print codeLines


def addPreset(filename):
    
    # get the list of presets for the filename
    presetList = checkFile(filename)

    if len(presetList) == 0:
    	pno = 1
    else:
    	pno = len(presetList)+1

    # Getting the line and code from the user
    print "Enter line to begin edit"
    lineNo = int(raw_input(">>"))

    print "Enter/Paste code to swap (to finish input, press CTRL+D for linux/mac or CTRL+Z for windows"
    code = sys.stdin.readlines()

    # Add new data into the preset file
    print "Adding new data into preset file..."
    f = open('presets/%s.preset'%(filename),'a')
    f.write('\n#PNO=%d'%pno)
    f.write('\n#LINE=%d'%lineNo)
    for c in code:
    	f.write('\n+%s'%c)
    print "Done!"




  #Copyright Adithya Murali


	

