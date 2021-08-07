f=open('fileone.txt','w+')
f.write('this is fileone')
f.close()

f=open('filetwo.txt','w+')
f.write('this is filetwo')
f.close()

import zipfile

r=zipfile.ZipFile('a_zip_file','w')
r.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)
r.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
r.close()