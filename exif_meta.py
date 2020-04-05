from PIL import Image
from PIL.ExifTags import TAGS
import os
import sys
k=('tiff','jpg','png','gif','jpe','jpeg','jif','jfi','jfif','webp','tif','raw','arw','cr2','nrw','k25') '''image file extensions'''
def get_meta():
    os.chdir(path)
    for root, dirs, files in os.walk(sys.argv[1]):
        for file in files:
            for r in k:
                if file.endswith(r):
                    try:
                        
                        img=Image.open(file)
                        width,height=img.size
                        print('')
                        print(file)
                        print('Type:',img.format,'\n'+'Dimension:',img.size,'\n','Mode:',img.mode+'\n',str(os.path.abspath(file)))
                        meta=img._getexif()
                        for tag,value in meta.items():
  
                            d=TAGS.get(tag)
                               
                            exif=value
                            print('============================')
                            print(str(d),str(exif))
                            print('')
                    except (FileNotFoundError,AttributeError):
                        pass
get_meta()
