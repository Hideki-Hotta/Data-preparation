from ij import IJ
import glob

DataPath = "C:/Users/KSYS-hotta/Documents/Python Scripts/python_sample/data_preparation/data"

for i in range(1,147):
	TiffPath = glob.glob("{}/sample_{}/*.tif".format(DataPath,i))
	IJ.open(TiffPath[0])
	imp = IJ.getImage()
	IJ.run("8-bit")
	IJ.saveAs("Tiff", "{}/sample_{}/movie_{}_8bit.tif".format(DataPath,i,i))
	imp.close()
