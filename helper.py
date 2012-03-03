import os

def getFiles(path):
    getFilesExt(path,"")
        
def getFilesExt(path,ext):
	if(not os.path.exists(path)):
		raise "Path does not exist"
	return [file for file in os.listdir(path) if file.upper().endswith(ext.upper())]