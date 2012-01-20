import sys
import helper
from encoder import Encoder

def main(argv):
    if argv is None or len(argv)<3:
        error="""
                 Args are INPUTCONTAINER PATH TARGETFORMAT [--RECURSE] [--DELETE]
                 eg. movie.py MKV /media/videofiles MP4-CONTAINER
                 Find any videos in MKV container and copy into an MP4 Container without transcode.
                 Recurse will recurse subdirectories. Delete will delete source when encode finished."""
        sys.exit(error)
    
    movieencoder=Encoder(argv[3],argv[2])
    movieencoder.queueFiles(helper.getFilesExt(movieencoder.targetpath,movieencoder.targetformat))
    movieencoder.encodeBatch()


main(sys.argv)
  
