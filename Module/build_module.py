#Will not be updated frequently at the moment

import os

#creates a folder and takes the path of the folder as the first argument and a boolean value as a second argument, "1" means relative path and "0" means absolute path. Relative path is default.
def dirMaker(path, rel=1):
	if rel == 1:
		os.makedirs("./" + path)
	elif rel == 0:
		os.makedirs(path)


#Creates a file and takes the path of the file as an argument and a boolean value as a second argument, "1" means relative path and "0" means absolute path. Relative path is default.
def fileMaker(path, rel=1):
	if rel == 1:
		open("./" + path,"w")
	elif rel == 0:
		open(path, "w")



