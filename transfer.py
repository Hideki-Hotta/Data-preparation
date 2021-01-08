import os
import glob
import shutil

OldPath = r"C:\Users\KSYS-hotta\Documents\Python Scripts\python_sample\data_preparation\data"
NewPath = r"\\10.250.1.240\Lab\Students\Hotta\Python_Scripts\data_preparation\data"

SamplePath = glob.glob("{}/sample_*".format(OldPath))
SampleNumber = len(SamplePath)

for i in range(1,SampleNumber+1):
    print(i)

    OldTxtPath = glob.glob("{}/sample_{}/*.txt".format(OldPath,i))
    OldTifPath = glob.glob("{}/sample_{}/*.tif".format(OldPath,i))

    FilePath = "{}/sample_{}/1_Movie_No.txt".format(OldPath,i)

    f = open(FilePath,"r")
    FileName = f.read()
    f.close()

    NewTxtPath_0 = "{}/sample_{}/1_Final_L_{}.txt".format(NewPath,i,FileName)
    NewTxtPath_1 = "{}/sample_{}/1_Final_L_p_{}.txt".format(NewPath,i,FileName)
    NewTxtPath_2 = "{}/sample_{}/1_Final_results_{}.txt".format(NewPath,i,FileName)
    NewTxtPath_3 = "{}/sample_{}/1_Movie_No.txt".format(NewPath,i)
    NewTifPath = "{}/sample_{}/{}.tif".format(NewPath,i,FileName)

    shutil.copy2(OldTxtPath[0],NewTxtPath_0)
    shutil.copy2(OldTxtPath[1],NewTxtPath_1)
    shutil.copy2(OldTxtPath[2],NewTxtPath_2)
    shutil.copy2(OldTxtPath[3],NewTxtPath_3)
    shutil.copy2(OldTifPath[0],NewTifPath)
