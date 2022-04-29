from PIL import Image
from PIL.ExifTags import TAGS
import os
import sys
def get_meta():
    os.chdir(sys.argv[1])
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
                    except Exception:
                        pass
get_meta()
