# This is a program to be able to swap replacable pieces
# of code in the same text file. 

import os
import sys
import funcs as fc

# Checking if a presets directory exists on boot.

if not os.path.isdir('./presets'):
	print "presets directory does not exist\n"
	print "creating presets directory...\n"
	os.makedirs('./presets')

# If our presets directory does exist,
# We need to look to find out if the directory
# has the preset file for our script. 
# If it does, we will read the file and its 
# contents in a seperate function, 
# else we will tell the user
# that we are creating a new text file with 
# the presets and exit the program. 

# Get file name as argument

try: 
    filename = sys.argv[1]
except:
	print "Enter a valid file name"
	exit(0)
# Check if file exists
if not os.path.exists(filename):
	print "File doesn't exist"
	exit(0)

try:
	option = sys.argv[2]
except: 
	print "Enter a valid option (use -h for help)\n"
	exit(0)

if option not in ['-v','-s','-a','-h']:
	print "Invalid Option (use -h for help)\n"
	exit(0)

# check if the preset for file exists in our 
# our presets folder. the checkfile function
# returns the presets if the presets for the file exists.

presets = fc.checkFile(filename)

if option == '-v': #view presets
	
	if not presets:
		exit(0)

	for preset in presets:
		print "Filename : ",preset.filename
		print "Preset No : ",preset.pno
		for code in preset.presetCode:
			print "+",code,'\n'

if option == '-s': #set preset
    fc.setPreset(filename, presets)

if option == '-a': #add preset
    fc.addPreset(filename)

if option == '-h': #display help
	print "-v : view presets for existing file"
	print "-s : set preset from existing presets"
	print "-a : add new presets"
	print "-h : help 	"






# Copyright Adithya Murali