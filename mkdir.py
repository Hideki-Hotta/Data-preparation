import os

FilePath = r"\\10.250.1.240\Lab\Students\Hotta\Python_Scripts\data_preparation\data"

for i in range(1,147):
    print(i)
    DirPath = "{}/sample_{}".format(FilePath,i)
    os.mkdir(DirPath)
