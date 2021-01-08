"""
画像データ
1. 8bitのマルチページtiffファイルを分割してRGB型で.png形式で保存
2. RGB画像をグレースケール化し.png形式で保存
3. グレースケール画像を正規化し.npy形式で保存
4. 画像の高さ・幅を全画像で揃えるために輝度値0をつなげてサイズを合わせ.npy形式で保存
5. 全画像データを４次元配列img(画像の高さ,画像の幅,フレーム番号,サンプル番号)(dtype:float)に格納し.npy形式で保存

Lpデータ
1. 全サンプルのLpを１次元配列Lp(dtype:float)に格納し.npy形式で保存

Lデータ
1. 全サンプルのLを１次元配列L(dtype:float)に格納し.npy形式で保存

備考
・tiffファイルの16bit→8bitはコードが分からなかったのでimageJのマクロ(ijm.py)で別途実施
・後から確認できるように各ステップの.pngや.npyは逐次保存しているが，処理がかなり遅くなるのでなくしてもいいかも
"""
import numpy as np
import cv2
import os
from PIL import Image
import shutil
import glob

def maxsize(SampleNumber):
    """
    画像の最大サイズを検索
    """
    height = 0
    width = 0
    for n in range(1,SampleNumber+1):
        FILENAME = ("data/sample_{}/movie_{}_8bit.{}".format(n,n,"tif"))
        img_pil = Image.open(FILENAME)
        if height < img_pil.height:
            height = img_pil.height
        if width < img_pil.width:
            width = img_pil.width
    return (height,width)

def saveoriginal(SampleNumber):
    """
    8bitのマルチページtiffファイルを分割してRGB型でpngファイルに保存
    """
    for n in range(1,SampleNumber+1):
        FILENAME = ("data/sample_{}/movie_{}_8bit.{}".format(n,n,"tif"))
        img_pil = Image.open(FILENAME)
        remove_image("data/sample_{}/1_original".format(n))
        count = 0
        while count<=img_pil.n_frames-1:
            img_pil.seek(count)
            img_pil.save("data/sample_{}/1_original/frame_{}.{}".format(n,count,"png"))
            count += 1

def do_grayscale(SampleNumber):
    """
    RGB画像をグレースケール化
    """
    for n in range(1,SampleNumber+1):
        remove_image("data/sample_{}/2_gray".format(n))
        for path in glob.glob("data/sample_{}/1_original/*.png".format(n)):
            img = cv2.imread(path)
            gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
            save_image(path,n,"2_gray",gray)

def do_normalize(SampleNumber):
    """
    グレースケール画像を正規化
    """
    for n in range(1,SampleNumber+1):
        remove_image("data/sample_{}/3_norm".format(n))
        for path in glob.glob("data/sample_{}/2_gray/*.png".format(n)):
            img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
            norm = (img-np.amin(img))/(np.amax(img)-np.amin(img))
            save_array(path,n,"3_norm",norm)

def do_modification(SampleNumber,size):
    """
    輝度値0をつなげてサイズ合わせ
    """
    for n in range(1,SampleNumber+1):
        remove_image("data/sample_{}/4_modified".format(n))
        for path in glob.glob("data/sample_{}/3_norm/*.npy".format(n)):
            img = np.load(path)
            img_mod = []
            for i in range(max(img.shape[0],size[0])):
                try:
                    x_temp = img[i]
                    if img.shape[1] < size[1]:
                       temp = np.concatenate([img[i],np.zeros(size[1]-img.shape[1],np.uint8)])
                       img_mod.append(temp)
                    else:
                        img_mod.append(img[i])
                except IndexError:
                    temp = np.zeros(size[1],np.uint8)
                    img_mod.append(temp)
            img_mod = np.array(img_mod)
            save_array(path,n,"4_modified",img_mod)

def save_image(img_path,n,dir,img):
    """
    画像を保存
    img_path : 画像のパス
    n : サンプル番号
    dir : ディレクトリ名
    img : 画像データ
    """
    file_name = img_path.replace("\\","/").split(".")[0].split("/")[-1]
    cv2.imwrite("data/sample_{}/{}/{}.{}".format(n,dir,file_name,"png"), img)

def save_array(img_path,n,dir,img):
    """
    画像をnpy形式に保存
    img_path : 画像のパス
    n : サンプル番号
    dir : ディレクトリ名
    img : 画像データ
    """
    file_name = img_path.replace("\\","/").split(".")[0].split("/")[-1]
    np.save("data/sample_{}/{}/{}".format(n,dir,file_name), img)

def remove_image(img_path):
    """
    フォルダ"img_path"の中身を削除
    フォルダ"img_path"が存在しなければ新たに作成
    """
    if os.path.exists(img_path) == True:
        shutil.rmtree(img_path)
        os.mkdir(img_path)
    else:
        os.mkdir(img_path)

def get_Lp(SampleNumber):
    """
    全サンプルのLpを格納した１次元配列を.npy形式で保存
    dtypeはfloat
    """
    Lp = []
    for i in range(1,SampleNumber+1):
        FilePath = glob.glob("data/sample_{}/1_Final_results_*.txt".format(i))
        FilePath = FilePath[0].replace("\\","/")
        f = open(FilePath,"r")
        data = f.read()
        f.close()
        temp = float(data.split()[-2])
        Lp.append(temp)
    np.save("data/final_data/Lp",Lp)

def get_L(SampleNumber):
    """
    全サンプルのLを格納した１次元配列を.npy形式で保存
    dtypeはfloat
    """
    L = []
    for i in range(1,SampleNumber+1):
        FilePath = glob.glob("data/sample_{}/1_Final_results_*.txt".format(i))
        FilePath = FilePath[0].replace("\\","/")
        f = open(FilePath,"r")
        data = f.read()
        f.close()
        temp = float(data.split()[-4])
        L.append(temp)
    np.save("data/final_data/L",L)

def get_img(SampleNumber,size,n_frames):
    """
    全サンプルの画像データをimg(画像の高さ,画像の幅,フレーム番号,サンプル番号)の４次元配列に格納
    .npy形式で保存
    dtypeはfloat
    """
    img = np.zeros((size[0],size[1],n_frames,SampleNumber))
    for n in range(1,SampleNumber+1):
        count = 0
        for path in glob.glob("data/sample_{}/4_modified/*.npy".format(n)):
            mod = np.load(path)
            img[:,:,count,n-1] = mod
            count = count + 1
    np.save("data/final_data/img",img)


if __name__=="__main__":
    SamplePath = glob.glob("data/sample_*")
    SampleNumber = len(SamplePath)
    n_frames = 500
    print("Number of samples is",SampleNumber)
    print("Number of frames is",n_frames)
    size = maxsize(SampleNumber)
    print("Max size of all images is",size)
    print("Now saving frames...")
    saveoriginal(SampleNumber)
    print("Now grayscaling...")
    do_grayscale(SampleNumber)
    print("Now normalization...")
    do_normalize(SampleNumber)
    print("Now modification...")
    do_modification(SampleNumber,size)
    get_Lp(SampleNumber)
    get_L(SampleNumber)
    get_img(SampleNumber,size,n_frames)
    print("Done!")
    