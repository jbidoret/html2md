#!/usr/bin/env python

import os, sys, glob
import html2text

# usage
# ./html2md.py sourcedir destdir

try:
    source = sys.argv[1]
    destdir = sys.argv[2]
except:
    print 'The command is waiting for two args : source directory and destination directory'
    raise e
    
for sourcefile in glob.glob(os.path.join(source, '*.html')):
    
    with open(sourcefile, "rb") as f:
        # read file
        src = f.read()
        
        # process md convert
        h = html2text.HTML2Text()
        data = h.handle(src.decode('utf-8'))

        # make dest dir if it doesn't exist
        if not os.path.exists(destdir):                 
            os.makedirs(destdir)

        destfile = os.path.join(destdir, os.path.basename(sourcefile) + '.md')
        dest = open(destfile, 'wb')
        # write file
        dest.write(data.encode('utf-8'))                                
        dest.close()
        print "%s successfully processed to %s" % (sourcefile, destdir)