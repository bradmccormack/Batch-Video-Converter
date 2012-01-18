import os
import sys


OUTDIR="/media/WDTVLiveUSB"
SUPPORTEDINPUTCONTAINER=('MKV')
SUPPORTEDTARGETFORMATS=('MP4-CONTAINER','DVD','X264BASE','X264HIGH')


class Encoder:
    inputfiles=()


#static methods .. class functions? what is the terminology
class Helper:
    def getFiles(path):
        getFiles(path,"")
	
    def getFilesExt(path,ext):
        return [file for file in os.listdir(path) if file.upper().endswith(ext.upper())]


def main(argv):
    if argv is None or len(argv)<3:
        error="""
                 Args are INPUTCONTAINER PATH TARGETFORMAT
                 eg. movie.py MKV /media/videofiles MP4-CONTAINER
                 Find any videos in MKV container and copy into an MP4 Container without transcode"""
        sys.exit(error)
    

    encoder=Encoder()
    
    #use instance field to store list of movies
    encoder.inputfiles=Helper.getFilesExt(argv[2],argv[1])
    if encoder.inputfiles is None:
        sys.exit("No files found in "+argv[2]+" that are of type "+argv[1])
        
  
  
main(sys.argv)
  
