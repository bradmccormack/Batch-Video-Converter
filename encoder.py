import Queue
import os;
from collections import deque


class ConversionException(Exception): pass


class Encoder(object):
    
    SUPPORTEDTARGETCONTAINER=['AVI','MKV','MP4','M4V']
    SUPPORTEDINPUTCONTAINER=SUPPORTEDTARGETCONTAINER+['ISO']
    SUPPORTEDTARGETVIDEOFORMATS=('H263','H263+','H264', 'MPEG2','MPEG4','VP8','THEORA','WMV')
    SUPPORTEDTARGETAUDIOFORMATS=('AC3','MP3','AAC')
    
    sourcecontainer=""
    targetcodec=""
    targetcontainer=""
    targetpath=""
    encodeQueue=Queue.Queue()
     
    def __init__(self,targetpath,sourcecontainer,targetcontainer,targetcodec):
       
        if(sourcecontainer not in self.SUPPORTEDINPUTCONTAINER):
            raise ConversionException("Cannot do conversion. Input Container is not supported")
        if(targetcontainer not in self.SUPPORTEDTARGETCONTAINER):
            raise ConversionException("Cannot do conversion. Output Container is not supported")
        if(targetcodec not in self.SUPPORTEDTARGETVIDEOFORMATS):
            raise ConversionException("Cannot do conversion. Codec not valid")
 
        self.sourcecontainer=sourcecontainer
        self.targetpath=targetpath
        self.targetcontainer=targetcontainer
        self.targetcodec=targetcodec
    	
    def queueFiles(self,inputfiles):
        if inputfiles is None or len(inputfiles)==0:
            print "No files found that match "+self.targetcontainer+" in "+self.targetpath
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
            print file+" has been encoded to format "+self.targetcontainer+" in location "+self.targetpath
        except:
            print "exception occurred"
            
            
            
            