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
        self.numLines = 0
    def setfilename(self,filename):
        self.filename = filename
    def setpno(self, pno):
    	self.pno = pno
    def setlines(self, editline):
    	self.editline = editline
    def addpresetCode(self, code):
    	self.presetCode.append(code)
    	self.numLines = self.numLines + 1
    def setPrev(self, prevPreset):
    	self.prev = prevPreset
    def getNumLines(self):
    	return self.numLines
    def getStartLine(self):
    	return self.editline


def checkFile(filename):
	# check if the file exists, if it does, then load
	# its presets. If it doesn't, create a preset
	# file with the filename
    if not os.path.exists('presets/%s.preset'%(filename)):
		print "Existing preset file does not exist"
		print "Creating a new preset file.."
		print 'step2'
		f = open('presets/%s.preset'%(filename),'w+')
		f.write('#PRESETS\n')
		f.write('#PREV=-1\n')
		f.close()
		print "Would you like to add a new preset?"
		choice = raw_input("Enter y or n:")
		if choice == 'y':
			print 'step3'
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
			#print fp.readlines()
			print 'step5'
			global previousPreset

		#		print fp.readlines()
			presetInfo = fp.readlines()
			print presetInfo
			presetInfo = [x[1:len(x)-1] for x in presetInfo]
			# print presetInfo

			# # iterate through the presetInfo list and
			# # add each preset
			presetList = []
			print presetInfo

			# try:
			if presetInfo[0] == 'PRESETS':
				for info in presetInfo[1:]:
					# print 'Once'
					# print info
					if info[0:3] == 'PNO':
						p = presets()
						p.setfilename(filename)
						p.setpno(int(info.split('=')[-1]))
						presetList.append(p)
					elif info[0:4] == 'LINE':
						p.setlines(int(info.split('=')	[-1]))
					elif info[0:4] == 'PREV':
						print info.split('=')
						previousPreset = int(info.split('=')[-1])
					elif info[0:1] == '+':
						print 'Im here'
						p.addpresetCode(info[1:])
						
		# except:
			# 	print "Quit tampering with the preset file, child."

			print previousPreset
			print presetList
			return presetList	


def setPreset(filename, presets):
	f = open('%s'%(filename))
	codeLines = f.readlines()
	codeLines = removePreviousPreset(codeLines,presets,previousPreset)
	print codeLines[0:100]
#	print codeLines
	# codeLines = [code[:len(code)-1] for code in codeLines]
	# print codeLines
	print "Enter preset number : "
	presetNumber = int(raw_input(">>>"))
	# print [p.pno for p in presets]
	if not presetNumber in [p.pno for p in presets]:
		print "Preset Number Not Found"
	else:
		for pos in range(presets[presetNumber-1].editline, presets[presetNumber-1].editline + len(presets[presetNumber-1].presetCode),1):
			#codeLines[pos] = presets[presetNumber].presetCode[pos] + '\n'
			# print pos
			codeLines[pos-1] = presets[presetNumber-1].presetCode[pos - presets[presetNumber-1].editline] + '\n'

		fp = open(filename,'w')
		for c in codeLines:
			fp.write(c)
		fp.close()
		print "Code has been swapped"

		# Changing the preset number
		f = open('presets/%s.preset'%(filename),'r')
		presetCodeLines = f.readlines()
		presetCodeLines[1] = '#PREV='+str(presetNumber)+'\n'
		f.close()

		f = open('presets/%s.preset'%(filename),'w')
		for c in presetCodeLines:
			f.write(c)
		f.close()

		print presetCodeLines

		# print presets[presetNumber].editline
		# print codeLines


def addPreset(filename):
    
    # get the list of presets for the filename
    print 'step4'
    presetList = checkFile(filename)

    if len(presetList) == 0:
    	pno = 1
    else:
    	pno = len(presetList)+1

    # Getting the line and code from the user
    print "Enter line to begin edit"
    lineNo = int(raw_input(">>"))

    print "Enter/Paste code to swap (to finish input, press CTRL+D for linux/mac or CTRL+Z for windows)"
    code = sys.stdin.readlines()

    # Add new data into the preset file
    print "Adding new data into preset file..."
    f = open('presets/%s.preset'%(filename),'a')
    f.write('#PNO=%d\n'%pno)
    f.write('#LINE=%d\n'%lineNo)
    for c in code:
    	f.write('++%s\n'%c)
    print "Done!"


def removePreviousPreset(code,presets,previousPreset):
	""" This function removes the code swapped in by the previous function"""
	print previousPreset
	if previousPreset > 0:
		p = presets[previousPreset-1]
		length = p.getNumLines()
		print 'length = ',length	
		line = p.getStartLine()
		code[line-1:line] = '\n'
		code[line:line+length] = '\n'
		print 'i came here'
		print code

	return code





  #Copyright Adithya Murali	


	

