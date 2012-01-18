import os
import sys
import Queue
from collections import deque

OUTDIR="/media/WDTVLiveUSB"
SUPPORTEDINPUTCONTAINER=('MKV')
SUPPORTEDTARGETFORMATS=('MP4-CONTAINER','DVD','X264BASE','X264HIGH')


class Encoder:
    encodeQueue=Queue.Queue()
    targetformat=""
    targetpath=""
    
    def queueFiles(self,inputfiles):
        if inputfiles is None:
            return "blah"
        for f in inputfiles:
            self.encodeQueue.put(f)
            
    def encodeBatch(self):
        while True:
            if not self.encodeQueue.empty():
                nextFile=self.encodeQueue.get()
                self._encodeFile(nextFile)
            else:
                break
    def _encodeFile(self,file):
        try:
            #do the encode .. use ffmpeg wrapper or just call the binary
            print file+" has been encoded to format "+self.targetformat+" in location "+self.targetpath
        except:
            print "exception occured"
            
class Helper:
    def getFiles(self,path):
        getFiles(path,"")
	
    def getFilesExt(self,path,ext):
        return [file for file in os.listdir(path) if file.upper().endswith(ext.upper())]


def main(argv):
    if argv is None or len(argv)<3:
        error="""
                 Args are INPUTCONTAINER PATH TARGETFORMAT
                 eg. movie.py MKV /media/videofiles MP4-CONTAINER
                 Find any videos in MKV container and copy into an MP4 Container without transcode"""
        sys.exit(error)
    
    encoder=Encoder()
    helper=Helper()

    encoder.targetformat=argv[3]
    encoder.targetpath=argv[2]
    encoder.queueFiles(helper.getFilesExt(encoder.targetpath,encoder.targetformat))
    encoder.encodeBatch()


main(sys.argv)
  
