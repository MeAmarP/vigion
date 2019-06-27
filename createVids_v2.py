# -*- coding: utf-8 -*-
"""
Given Video, split current video into a several FastFwd Videos
Just to generate more Data.

Created on Fri Mar 15 11:31:51 2019
@author: apotdar
"""

import glob
import cv2

_rootDir = 'train\\suspect\\'
_fileExtn = '.mp4'
_fps = 40
VideoFilePaths = glob.glob(_rootDir+'*.mp4')
for path in VideoFilePaths:    
    filename_no_ext = path.split('\\')[2].split('.')[0]
    FramesList = glob.glob(_rootDir+filename_no_ext+'*.jpg')
#    print('Total Frames in', filename_no_ext,'video is', len(FramesList))
    NbFrmSets = len(FramesList) // _fps
    for SingleSet in range(NbFrmSets):
#        print('Current Set Num = ',SingleSet)
#        print('---------------------------------------------------------------')
        ImgArry = []
        for FramNum in range(SingleSet+1, len(FramesList),NbFrmSets):
            ImgPath = _rootDir+filename_no_ext+'_frame'+str(FramNum)+'.jpg'
            img = cv2.imread(ImgPath)
            h,w,_ = img.shape
            ImgArry.append(img)
        VdoName = filename_no_ext + '_part_' + str(SingleSet) + '.mp4'
        VdoOut = cv2.VideoWriter(VdoName,cv2.VideoWriter_fourcc(*'MP4V'),40,(w,h))
        
        for i in range(len(ImgArry)):
            VdoOut.write(ImgArry[i])
        VdoOut.release()
        print('Done With FrameSet Number ', SingleSet+1)
            
            
        
        
    
    





#def createVideo(AllFramesPath,fps):        
#    ImgArray = []
#    for singleFramePath in AllFramesPath:
#        img = cv2.imread(singleFramePath)
##        img = cv2.resize(img, (640,480), interpolation = cv2.INTER_AREA)
#        h,w,ch = img.shape
#        ImgArray.append(img)
#        
#    #Create Video Writer Object
#    VdoOut = cv2.VideoWriter('myVdo3.mp4',cv2.VideoWriter_fourcc(*'MP4V'),40,(w,h))
#        
#    for i in range(len(ImgArray)):
#        VdoOut.write(ImgArray[i])   
#    VdoOut.release()
#    print('Done!')
#
#AllFramesPath = glob.glob('\\sample\\*.jpg')    
#createVideo(AllFramesPath)