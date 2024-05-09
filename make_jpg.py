import os
import glob
import cv2

def make_jpg(path,savepath):
    if os.path.exists(path):
        paths = glob.glob(f"{path}/*")
        if len(paths) == 0:
            raise Exception(f"{path} have no image file")
        paths = [file for file in paths if not (file.endswith('.png') or file.endswith('.json'))]
        for item in paths:
            img = cv2.imread(item)
            filename = os.path.basename(item)
            filename = filename.split(".")
            filename[-1] = ".jpg"
            filename = "".join(filename)
            cv2.imwrite(os.path.join(savepath,filename),img)
    else:
        raise Exception(f"{path} exists in the current directory.")



