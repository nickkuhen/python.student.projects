#Python Version 2.7

import shutil
import os


srcPath = "C:/Users/Student/Desktop/Folder_A"
dstPath = "C:/Users/Student/Desktop/Folder_B"

fileList = os.listdir(srcPath)
for fileName in os.listdir(srcPath):
    if fileName.endswith(".txt"):

        src_fileName = "C:/Users/Student/Desktop/Folder_A/%s" % fileName
        dst_fileName = "C:/Users/Student/Desktop/Folder_B/%s" % fileName

        print 'This file was moved: %s' % (src_fileName)
        shutil.move(src_fileName,dst_fileName)
