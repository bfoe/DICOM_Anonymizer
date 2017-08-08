#!/bin/python
# 
# very simple DICOM anonimzer
#

from __future__ import print_function
import os
import sys

FNULL = open(os.devnull, 'w')
old_target, sys.stderr = sys.stderr, FNULL # replace sys.stdout 
try: import dicom
except: 
    print ("Error: Pydicom library not found, download from www.pydicom.org\n")
    sys.exit(1)
sys.stderr = old_target # re-enable

try: 
	import Tkinter as tk; # Python2
	import tkMessageBox as messagebox
except: 
  try: 
	import tkinter as tk; # Python3
	from tkinter import messagebox
  except: 
	print ('ERROR: tkinter not installed')
	print ('       on Linux try "yum install tkinter"')
	print ('       on MacOS install ActiveTcl from:')
	print ('       http://www.activestate.com/activetcl/downloads')
	sys.exit(2)
  
  
def isDICOM (file):
    try: f = open(file, "rb")
    except: lprint ('ERROR: opening file'+file); exit(1)
    try:
        test = f.read(128) # through the first 128 bytes away
        test = f.read(4) # this should be "DICM"
        f.close()
    except: return False # on error probably not a DICOM file
    if test == "DICM": return True 
    else: return False    	
	

# --------------------------- main program starts here --------------------------------

TKwindows = tk.Tk(); TKwindows.withdraw() #hiding tkinter window
result = messagebox.askquestion("CAUTION !",
		 "This program will modify all DICOM files under the current folder:\n"+
		 os.getcwd()+
		 "\n\nThe following tags will be anonimized:\n"+
		 "PatientName, PatientBirthDate, PatientSex, PatientAge\n"+
		 "\nFiles named DICOMDIR can not be modified "+
		 "(however these do contain patient information), "+
		 "non-DICOM files will not be modified, "+
		 "(please use other means to anonimyze these)."+
		 "\n\n\nProceed ?")
if result != 'yes': sys.exit(0)

print ('Start ... ')

# recursively find all files in current dir
PatientName = ''; PatientBirthDate = ''; PatientSex = ''; PatientAge = ''
FileList = []
for root, subFolders, files in os.walk('.'):
    for file in files:
		FileList.append(os.path.join(root,file))          
  
# try opening file by file
for file in FileList:
    if isDICOM (file) and os.path.basename(file) != 'DICOMDIR':
        try: Dset = dicom.read_file (file)
        except: print ('Error reading ', file)
        try: 
            PatientName = Dset.PatientName
            PatientBirthDate = Dset.PatientBirthDate
            PatientSex = Dset.PatientSex
            PatientAge = Dset.PatientAge
        except: print ('Error identifying DICOM tags in file ', file)
        if PatientName == 'ANONIMIZED' and 	PatientBirthDate == '' and \
		   PatientSex == '' and PatientAge == '':	
            print ('Already anonymized ', file)
        else:
			try:
				Dset.PatientName = 'ANONIMIZED'
				Dset.PatientBirthDate = ''
				Dset.PatientSex = ''
				Dset.PatientAge = ''
				Dset.save_as(file)
				print ('Sucessfully anonymized ', file)			
			except: 
				print ('Error modifying ', file)
print ('Done\n')

#end
if sys.platform=="win32": os.system("pause") # windows
else: 
    #os.system('read -s -n 1 -p "Press any key to continue...\n"')
    import termios
    print("Press any key to continue...")
    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)
    try: result = sys.stdin.read(1)
    except IOError: pass
    finally: termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)