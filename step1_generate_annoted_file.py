'''
Filename: f:/Dataset/Anomaly_Dataset/Anomaly_Videos/testcode/generate_annoted_file.py
Path: f:/Dataset/Anomaly_Dataset/Anomaly_Videos/testcode
Created Date: Monday, June 10th 2019, 7:40:56 pm
Author: apotdar
Description:
    -We have Crime Video annoted text file
    -We generated file with classlabele/ID and absolute path to video file
    -Next we replaced Filename by filepath in annoted file
Copyright (c) 2019 Your Company
'''

import os
import glob
import cv2


def getClassNames(_path_to_dataset):
    AllCrimeList = os.listdir(_path_to_dataset)
    AllCrimeDict = {val:key for val,key in enumerate(AllCrimeList)}
    return AllCrimeDict


def generateLableFile(_rootDir,_fileExtension,output_filepath):
    """First Generate file with Absolute video path and ClassID/Label
    
    Arguments:
        _rootDir {string} -- Path to Rootdir where dataset is located
        _fileExtension {string} -- type of a file extension of the 
                                   video data(.avi,.mp4 etc.)
    """
    for root, dirs, _ in os.walk(_rootDir):
        for classid, folder in enumerate(dirs):
            path_to_dir = os.path.join(root,folder)
            AllPath = glob.glob(path_to_dir+'/*'+_fileExtension)
            for path in AllPath:
                myFile = open(output_filepath,"a")
                finPath = path + ' ' +str(classid+1)+'\n'
                myFile.write(finPath)
                # print(path, classid+1)    
    myFile.close()
    print("Done!! Writting file")
    return

def updateAnnotedFile(labeled_filepath,annoted_filepath,output_filepath):
    """Second Generate new annoted file with path, classid and trime frame values
        This function will compare generated labeled file with Old Annoted file
        and keeps rows only which have available in directory
    
    Arguments:
        labeled_filepath {string} -- labeled file path
        annoted_filepath {string} -- annoted file of video trim frames and classID
        output_filepath {string} -- file with path and annoted trim frame data
    """
    with open(annoted_filepath) as ann_file:
        with open(labeled_filepath) as l_file:
            with open(output_filepath,'a') as o_file:
                for line in l_file:
                    annLine = ann_file.readline()
                    if annLine.split(' ')[0] == ((line.split(' ')[0]).split('\\'))[-1]:
                        o_file.write(annLine)
    print("Done! Updating annoted file")
    return

def getFinalAnnoFile(NewAnno_file,labeled_file,output_filepath):
    """Generate final trimmed text file with:
    - path_to_video_file, classid, start-end frame no of action
    - replace filename with absolute file path
    
    Arguments:
        NewAnno_file {string} -- path to the new annoted file with classes as much in directory
        labeled_file {[type]} -- path to the labeled file with absolute path
        output_filepath {[type]} -- path to the output file
    """
    with open(NewAnno_file) as f:
        with open(labeled_file) as l_file:
            with open(output_filepath,"a") as o_file:
                for line in f:
                    l_file_line = l_file.readline()
                    if line.split(' ')[0] == (l_file_line.split(' ')[0]).split('\\')[-1]:
                        oldString = line.split(' ')[0]
                        newString = l_file_line.split(' ')[0]
                        o_file.write(line.replace(oldString,newString))
    print("Done Writing File!!")
    return


if __name__ == "__main__":

    _FILE_EXTENSION = '.mp4'
    _path_to_base_dir = os.getcwd()
    #_path_to_sample_data = os.path.join(_path_to_base_dir,'testcode','sample_data')
    _path_to_anomaly_data = os.path.join(_path_to_base_dir,'dataset','anomaly')
    _path_to_train_data = os.path.join(_path_to_base_dir,'dataset','train')
    _path_to_test_data = os.path.join(_path_to_base_dir,'dataset','test')

    #getAbsoultePathToVideoFile(_path_to_sample_data)
    new_labeled_file = "v1_labeled_data.txt"
    old_annoted_file = "UCF_Crimes_temporal_annotation.txt"
    new_annoted_file = 'v1_updated_video_anno_file.txt'
    # NewAnno_file = "fin_anno_video.txt" 

    #Step 1
    # generateLableFile(_path_to_anomaly_data,'.mp4','v1_labeled_data.txt')

    #Step 2
    # updateAnnotedFile(labeled_file,annoted_file,'v1_updated_video_anno_file.txt')

    #Step 3
    # getFinalAnnoFile(new_annoted_file,labeled_file,'v1_final_trimmed_anno_file.txt')

                        



        
  
        



    


    
