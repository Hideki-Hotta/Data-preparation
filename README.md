# Data-preparation
main.py:
画像データ
1. 8bitのマルチページtiffファイルを分割してRGB型で.png形式で保存
2. RGB画像をグレースケール化し.png形式で保存
3. グレースケール画像を正規化し.npy形式で保存
4. 画像の高さ・幅を全画像で揃えるために輝度値0をつなげてサイズを合わせ.npy形式で保存
5. 全画像データを４次元配列img(画像の高さ,画像の幅,フレーム番号,サンプル番号)(dtype:float)に格納し.npy形式で保存

Lpデータ
1. 全サンプルのLpを１次元配列Lp(dtype:float)に格納し.npy形式で保存

Lデータ
1. 全サンプルのLを１次元配列Lp(dtype:float)に格納し.npy形式で保存

備考
・tiffファイルの16bit→8bitはコードが分からなかったのでimageJのマクロ(ijm.py)で別途実施
・後から確認できるように各ステップの.pngや.npyは逐次保存しているが，処理がかなり遅くなるのでなくしてもいいかも
・ファイルのパスは適宜変更をお願いします

ijm.py:
1. tiffファイルの16bit→8bitを実施しmovie_*_8bit.tifの名前(形式)で保存

備考
・imageJのマクロでのみ動作（ijというライブラリが必要のため）
・ファイルのパスは適宜変更をお願いします

mkdir.py, transfer.py:
生データを移動するための適当なコード
