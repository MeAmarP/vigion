'''
Filename: f:/Dataset/Anomaly_Dataset/Anomaly_Videos/step2_generate_trimmed_videofiles.py
Path: f:/Dataset/Anomaly_Dataset/Anomaly_Videos
Created Date: Thursday, June 13th 2019, 6:17:03 pm
Author: apotdar

Description:
    - Read final generated annoted file[in step 1] 

    - [video_path video_class act_start1 act_end1 act_start2 act_end2]

    - trim the video as per the frame no for every action in the video

    - Move the video into test-train folders
        """
    #TODO:
    * * Read the path >> Apply VideoClip func >> Move the file to respective directory
    * * We have splited paths between Train and Test
    * * Apply respective dataset VideClip function
    * * Add function argument for explicit mention of 'train' or 'test'
    * * Write a function to getClassName() based on ClassID
    * * Create path using os.getcwd(), 'train/test' 'className'
    * * Check if os.isDir() if not then os.mkdirs()
    """

Copyright (c) 2019 Your Company
'''

import cv2
import os

import pandas as pd

def getDframe_AnnotedFile(path_final_annoted_file):
    df = pd.read_csv(path_final_annoted_file,
                        delimiter=' ',
                        names=['path',
                                'classid',
                                'act_start1',
                                'act_end1',
                                'act_start2',
                                'act_end2'])
    return df

def getClassNames(_path_to_dataset):
    AllCrimeList = os.listdir(_path_to_dataset)
    AllCrimeDict = {val+1:key for val,key in enumerate(AllCrimeList)}
    return AllCrimeDict    

def generateTrimmedVideo_v2(df,data_for='test',class_id = None):
    if class_id:
    # for class_id in anno_df.classid.unique():
        no_of_files_in_class = df[df.classid==class_id].path.size
        no_of_train_files = int(no_of_files_in_class * _TRAIN_SPLIT_VAL)
        #get path to the train/test files
        if data_for == 'train':
            video_paths = df[df.classid==class_id].path[:no_of_train_files]
        elif data_for == 'test':
            video_paths = df[df.classid==class_id].path[no_of_train_files:]
        
        for index in video_paths.index:
            path_input_video_file = df.at[index,'path']
            act_start1 = df.at[index,'act_start1']
            act_end1 = df.at[index,'act_end1']
            act_start2 = df.at[index,'act_start2']
            act_end2 = df.at[index,'act_end2']            
            # print(video_file_name)
            print(path_input_video_file)
            VidCap = cv2.VideoCapture(path_input_video_file)
            if (VidCap.isOpened() == False):
                print('Err!!! Can\'t Open Video File')
            elif (VidCap.isOpened() == True): 
                video_frame_height = VidCap.get(cv2.CAP_PROP_FRAME_HEIGHT)
                video_frame_width = VidCap.get(cv2.CAP_PROP_FRAME_WIDTH)
                if (act_start1 != -1) and (act_end1 != -1):
                    # Set Video Start Position Frame No.
                    VidCap.set(cv2.CAP_PROP_POS_FRAMES,act_start1-1)
                    diff1 = (act_end1 - act_start1)                   
                    # Get Video Name
                    video_file_name = 'trimmed1_'+path_input_video_file.split('\\')[-1]
                    print(video_file_name)
                    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
                    OutVideo1 = cv2.VideoWriter(video_file_name,fourcc,40,(int(video_frame_width),int(video_frame_height)))
                    # Create object to generate output Video
                    for _ in range(diff1):
                        _,frame = VidCap.read()
                        OutVideo1.write(frame)
                    OutVideo1.release()
                    VidCap.release()
                    #===========================================================
                    lilpath = os.path.join(os.getcwd(),'vigion','dataset',data_for,CrimeTypeDict[class_id])
                    #print(lilpath)
                    if not os.path.isdir(lilpath):
                        os.makedirs(lilpath)
                    finPath = os.path.join(lilpath, video_file_name)
                    #print(finPath)
                    os.rename(os.path.abspath(video_file_name), finPath)
                if (act_start2 != -1) and (act_end2 != -1):
                    VidCap = cv2.VideoCapture(path_input_video_file)
                    VidCap.set(cv2.CAP_PROP_POS_FRAMES,act_start2-1)
                    diff2 = (act_end2 - act_start2)
                    video_file_name = 'trimmed2_'+path_input_video_file.split('\\')[-1]
                    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
                    OutVideo2 = cv2.VideoWriter(video_file_name,fourcc,40,(int(video_frame_width),int(video_frame_height)))
                    for _ in range(diff2):
                        _,frame = VidCap.read()
                        OutVideo2.write(frame)
                    OutVideo2.release()
                    VidCap.release()            
                    #===========================================================
                    lilpath = os.path.join(os.getcwd(),'vigion','dataset',data_for,CrimeTypeDict[class_id])
                    #print(lilpath)
                    if not os.path.isdir(lilpath):
                        os.makedirs(lilpath)
                    finPath = os.path.join(os.path.abspath(lilpath), video_file_name)
                    #print(finPath)
                    os.rename(os.path.abspath(video_file_name), finPath)
    return



if __name__ == "__main__":
    _TRAIN_SPLIT_VAL = 0.7
    _TEST_SPLIT_VAL = 0.3
    _FILE_EXTENSION = '.mp4'
    path_final_annoted_file = 'F:\\Dataset\\Anomaly_Dataset\\Anomaly_Videos\\vigion\\v1_final_trimmed_anno_file.txt'
    data_dir_path = os.path.join(os.getcwd(),'vigion','dataset','anomaly')
    CrimeTypeDict = getClassNames(data_dir_path)
    dFrame = getDframe_AnnotedFile(path_final_annoted_file)

    data_category = 'test'
    for class_id in dFrame.classid.unique():        
        generateTrimmedVideo_v2(dFrame,data_for=data_category,class_id=class_id)
        print('Video processing Done for<< {0} | {1} >>class'.format(data_category,CrimeTypeDict[class_id]))



    



    