import os

def getFiles(path):
    getFilesExt(path,"")
        
def getFilesExt(path,ext):
    return [file for file in os.listdir(path) if file.upper().endswith(ext.upper())]