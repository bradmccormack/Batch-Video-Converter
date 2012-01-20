import Queue
from collections import deque


class Encoder(object):
    
    SUPPORTEDINPUTCONTAINER=('MKV')

    #change to dicts and make the key the format and the value the x264 args
    SUPPORTEDTARGETFORMATS=('MP4-CONTAINER','DVD','X264BASE','X264HIGH')
    targetformat=""
    targetpath=""
    encodeQueue=Queue.Queue()
     
    def __init__(self, targetformat, targetpath):
       
        self.targetformat=targetformat
        self.targetpath=targetpath
    
    def queueFiles(self,inputfiles):
        if inputfiles is None or len(inputfiles)==0:
            print "No files found that match "+self.targetformat+" in "+self.targetpath
            return
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
            
            
            
            #gomardi lena book for the 30th paety photo
            