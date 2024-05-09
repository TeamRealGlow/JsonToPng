from json_to_png import json_to_png
from make_jpg import make_jpg
import argparse
import os
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('imgpath', type=str, metavar="img path", help="input your img path")
    parser.add_argument('savepath', type=str, metavar="save path", help="want save jpg path")
    args = parser.parse_args()
    path = args.imgpath
    savepath = args.savepath
    try:
        if os.path.exists(savepath):
            pass
        else:
            os.mkdir(savepath)
        make_jpg(path=args.imgpath, savepath=savepath)
        json_to_png(path=args.imgpath, savepath=savepath)
    except Exception as e:  # 예외가 발생했을 때 실행됨
        print(e)

