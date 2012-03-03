import sys
import helper
import argparse
from encoder import Encoder

def main(argv):
	parser = argparse.ArgumentParser(description=' Batch Movie Encoder. Converts from one container to another with specified codec for all files in the specified Destination path.',
	epilog='If the codec specified is the same as the codec in the source container only a copy will not be done and no transcoding to speed up the process.')
	
	parser.add_argument('-p',help='Destination path',required=True)
	
	parser.add_argument('-i',choices=Encoder.SUPPORTEDINPUTCONTAINER,
	help='The input movie container format. Generally the same as the file extension. Eg .avi',required=True)
	
	parser.add_argument('-o',choices=Encoder.SUPPORTEDTARGETCONTAINER,
	help='The output movie container format.',required=True)
	
	parser.add_argument('-c',choices=Encoder.SUPPORTEDTARGETVIDEOFORMATS,
	help='The video codec to encode with.',required=False,default='H264')
	
	parser.add_argument('-r',help='Recurse subdirectories.')
	parser.add_argument('-d',help='Delete source file after conversion completion.')
	
	EncoderOptions= parser.parse_args()
	
	try:
		movieEncoder=Encoder(EncoderOptions.p,EncoderOptions.i,EncoderOptions.o,EncoderOptions.c)
		movieEncoder.queueFiles(helper.getFilesExt(EncoderOptions.p,EncoderOptions.i))
		movieEncoder.encodeBatch()
	except Exception as e:
		print e
	
main(sys.argv)
  
