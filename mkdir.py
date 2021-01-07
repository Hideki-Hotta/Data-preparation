import os

for i in range(131,151):
    print(i)
    DirPath = "data/sample_{}".format(i)
    os.mkdir(DirPath)