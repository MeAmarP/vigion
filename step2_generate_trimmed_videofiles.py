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

Copyright (c) 2019 Your Company
'''

import cv2
import os

import pandas as pd

def readAnnotedFile():
    return

def getClassNames(_path_to_dataset):
    AllCrimeList = os.listdir(_path_to_dataset)
    AllCrimeDict = {val+1:key for val,key in enumerate(AllCrimeList)}
    return AllCrimeDict    

# num_of_act_frame = (act_end_frame-act_start_frame)+5
# VidCap = cv2.VideoCapture(path_to_video_file)
# VidCap.set(cv2.CAP_PROP_POS_FRAMES,act_start_frame-1)
# video_frame_height = VidCap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# video_frame_width = VidCap.get(cv2.CAP_PROP_FRAME_WIDTH)
# video_file_name = path_to_video_file.split('/')[-1]

# # #Create object to write test Video
# fourcc = cv2.VideoWriter_fourcc(*'MP4V')
# OutVideo = cv2.VideoWriter(video_file_name,fourcc,20,(int(video_frame_width),int(video_frame_height)))


# for frame_num in range(num_of_act_frame):
#     _,frame = VidCap.read()
#     OutVideo.write(frame)
#     cv2.imshow("Video",frame)
#     cv2.waitKey(1)
    
# VidCap.release()
# OutVideo.release()
# print('Done!! Writing Video')
# cv2.destroyAllWindows()

def generateTrimmedVideo(path_input_video_file,act_start_frame,act_end_frame,path_output_video_file):
    num_of_act_frame = (act_end_frame-act_start_frame)+5
    # Create Vidoe Capture object to read video
    VidCap = cv2.VideoCapture(path_input_video_file)
    # Get Video Properties
    VidCap.set(cv2.CAP_PROP_POS_FRAMES,act_start_frame-1)
    video_frame_height = VidCap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    video_frame_width = VidCap.get(cv2.CAP_PROP_FRAME_WIDTH)
    # Get Video Name
    video_file_name = path_input_video_file.split('/')[-1]
    # Create object to generate output Video
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    OutVideo = cv2.VideoWriter(video_file_name,fourcc,20,(int(video_frame_width),int(video_frame_height)))

    for _ in range(num_of_act_frame):
        _,frame = VidCap.read()
        OutVideo.write(frame)
        # cv2.imshow("Video",frame)
        # cv2.waitKey(1)    
    VidCap.release()
    OutVideo.release()

    os.rename(path_input_video_file,path_output_video_file)
    print('Done!! Writing Video')
    # cv2.destroyAllWindows()
    return



if __name__ == "__main__":
    _TRAIN_SPLIT_VAL = 0.7
    _TEST_SPLIT_VAL = 0.3
    _FILE_EXTENSION = '.mp4'
    final_annoted_file = 'F:/Dataset/Anomaly_Dataset/Anomaly_Videos/testcode/fin_video_trimtime.txt'
    data_dir_path = os.path.join(os.getcwd(),'dataset','anomaly')
    CrimeTypeDict = getClassNames(data_dir_path)

    import pandas as pd
    df = pd.read_csv(final_annoted_file,
                            delimiter=' ',
                            names=['path',
                                   'classid',
                                   'act_start1',
                                   'act_end1',
                                   'act_start2',
                                   'act_end2'])
    #Acess the path based on classid
    
    for class_id in df.classid.unique():
        no_of_files_in_class = df[df.classid==class_id].path.size
        no_of_train_files = int(no_of_files_in_class * _TRAIN_SPLIT_VAL)
        #get path to the train/test files
        train_video_paths = df[df.classid==class_id].path[:no_of_train_files]
        test_video_paths = df[df.classid==class_id].path[no_of_train_files:]             
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
        lilpath = os.path.join(os.getcwd(),'dataset','train',CrimeTypeDict[class_id])
        # if os.path.isdir(lilpath):
        #     os.makedirs(lilpath)
    # generateTrimmedVideo(path_input_video_file,act_start_frame,act_end_frame,path_output_video_file)

    