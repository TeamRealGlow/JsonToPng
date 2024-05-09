import glob2 as glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np
import os
import cv2
import time
first = time.time()
folder_path = '.\\CelebAMask-HQ\\CelebAMask-HQ-mask-anno\\'
modelname = {}

dir = os.listdir(folder_path)
for i in range(len(dir)):
    dir[i] = os.path.join(folder_path,dir[i])
filterList = ["skin","l_eye","r_eye","l_brow","r_brow","u_lip","l_lip","mouth","nose","l_ear","r_ear","hair","eye_g"]
color_map = {
            "hair": (60, 0, 255),
             "l_brow": (51, 255, 255),
             "r_brow": (51, 255, 255),
             "l_eye": (255, 0, 255),
             "r_eye": (255, 0, 255),
             "u_lip": (255, 255, 0),
             "l_lip": (255, 255, 0),
             "mouth": (0, 255, 0),
             "nose": (0, 153, 0),
             "skin": (255, 0, 0),
             "l_ear": (255, 204, 204),
             "r_ear": (255, 204, 204),
             "eye_g": (0, 0, 0)
             }
#폴더마다 순회하며 가져옴
for item in dir:
    files = glob.glob(item+'/*')

    for initem in files:
        filename = os.path.basename(initem)
        file = filename.split("_")
        name = file[1:]
        fileNumber = int(file[0])
        name = "_".join(name)
        name = name.replace(".png","")
        if name in filterList:
            if fileNumber in modelname:
                modelname[fileNumber][0].append(initem)
                modelname[fileNumber][1].append(name)
            else:
                modelname[fileNumber] = [[],[]]
                modelname[fileNumber][0].append(initem)
                modelname[fileNumber][1].append(name)


def addall(pics: list,name:list):
    width, height = 512, 512
    canvas = Image.new('RGB', (width, height), color='black')
    canvas = np.array(canvas)

    for i in range(13):
        if pics[i] == "":
            continue
        pic = cv2.imread(pics[i])
        pic[np.all(pic == 255, axis=-1)] = color_map[name[i]]
        mask = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        canvas = cv2.copyTo(pic,mask,canvas)
    return canvas

for i in range(len(modelname)):
    start_time = time.time()
    newList = ["", "", "", "", "", "", "", "", "", "", "", "", ""]
    nameList = ["", "", "", "", "", "", "", "", "", "", "", "", ""]
    model = modelname[i]
    file_paths = model[0]
    filename = os.path.basename(file_paths[0])
    filename = filename.split("_")
    filename = filename[0]
    unitNames = model[1]
    for idx in range(len(file_paths)):
        vname = unitNames[idx]
        file_path = file_paths[idx]
        if vname == "hair":
            newList[12] = file_path
            nameList[12] = vname
        elif vname == "l_brow":
            newList[5] = file_path
            nameList[5] = vname
        elif vname == "r_brow":
            newList[6] = file_path
            nameList[6] = vname
        elif vname == "l_eye":
            newList[3] = file_path
            nameList[3] = vname
        elif vname == "r_eye":
            newList[4] = file_path
            nameList[4] = vname
        elif vname == "u_lip":
            newList[7] = file_path
            nameList[7] = vname
        elif vname == "l_lip":
            newList[8] = file_path
            nameList[8] = vname
        elif vname == "mouth":
            newList[2] = file_path
            nameList[2] = vname
        elif vname == "nose":
            newList[9] = file_path
            nameList[9] = vname
        elif vname == "skin":
            newList[0] = file_path
            nameList[0] = vname
        elif vname == "l_ear":
            newList[10] = file_path
            nameList[10] = vname
        elif vname == "r_ear":
            newList[11] = file_path
            nameList[11] = vname
        elif vname == "eye_g":
            newList[1] = file_path
            nameList[1] = vname

    croeentimg = addall(newList,nameList)
    result_image = Image.fromarray(croeentimg)
    result_image.save(f"./CelebAMask-HQ/gray_mask/{filename}.png")
    end_time = time.time()
    print(f"{filename} 생성완료, 시간:{end_time-start_time}")

last_time= time.time()
print(f"작업완료 총 걸린시간:{last_time-first}")



