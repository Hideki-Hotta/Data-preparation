import os
import glob
import shutil

OldPath = r"C:\Users\KSYS-hotta\Documents\Python Scripts\python_sample\data_preparation\data"
NewPath = r"\\10.250.1.240\Lab\Students\Hotta\Python_script\data_preparation\data"

SamplePath = glob.glob("{}/sample_*".format(OldPath))
SampleNumber = len(SamplePath)

for i in range(1,SampleNumber+1):
    OldTxtPath = glob.glob("{}/sample_{}/*.txt".format(OldPath,i))
    OldTifPath = glob.glob("{}/sample_{}/*.tif".format(OldPath,i))

    TxtName = OldTxtPath[0].replace("\\","/").split(".")[-2].split("/")[-1]
    TifName = OldTifPath[0].replace("\\","/").split(".")[-2].split("/")[-1]

    NewTxtPath = "{}/sample_{}/{}.txt".format(NewPath,i,TxtName)
    NewTifPath = "{}/sample_{}/{}.tif".format(NewPath,i,TifName)

    shutil.copy2(OldTxtPath[0],NewTxtPath)
    shutil.copy2(OldTifPath[0],NewTifPath)
