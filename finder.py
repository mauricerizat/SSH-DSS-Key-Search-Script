#SSH DSS private key identifier

#This is a very basic script to look through the publicly released DSS keys database for a private key equivalent to your supplied public key.

#If you need it, the databse can be downloaded from here: https://github.com/g0tmi1k/debian-ssh.git

#This is a very simple program. You can modify it to accept a raw public key input as well.
#I did it in python because I don't like bash. It shouldn't be much slower, though.

import os
import sys

args = sys.argv

#Usage: python3 finder.py <path to keys directory> <public-key file eg. id_rsa.pub> 

print("This is a very basic script to look through the publicly released DSS keys database for a private key equivalent to your supplied public key.")
print("If you need it, the databse can be downloaded from here: https://github.com/g0tmi1k/debian-ssh.git")

if len(args) != 3:
	print ("\nUsage: python3 finder.py <path to keys directory> <public-key file eg. id_rsa.pub> ")
	sys.exit()
	
##Getting public key
readCommand = 'cat ' + str(args[2]) + ' | awk {\'print $2\'} 2>1'

pubKey = os.popen(readCommand).read()

#Checking directory
keysDirectory = str(args[1])

if keysDirectory[len(keysDirectory)-1] != '/':
	keysDirectory = keysDirectory + "/"	
	
directoryCommand = 'ls ' + keysDirectory	
stuff = os.popen(directoryCommand).read()

files = stuff.split()

print ("Looking for private key equialent of the public key:\n" + pubKey + "\nIn directory: " + keysDirectory + "\n")

num = 0
total = len(files)

#Actual Search

for i in files:
	num = num+1
	if '.pub' in i:
		print ("\rChecking file " + str(num) + " of " + str(total) + "     ", end='')
		command = 'cat ' + keysDirectory + i + ' | awk {\'print $2\'}'
		content = os.popen(command).read()
		
		if (pubKey in content):
			foundFile = keysDirectory + i[0:len(i)-4] 
			print ("\n\nFound! Filename: " + foundFile)
			print ("\nPrivate Key:\n")
			foundCommand = 'cat ' + foundFile
			print (os.popen(foundCommand).read())
			sys.exit()

print("\n\nPrivate key not found.")

