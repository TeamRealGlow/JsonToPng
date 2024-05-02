import os
import glob
import json

import cv2
import numpy as np
# class_name = ["hair","brow","eye",'lip',"mouth","nose","skin","ear"]
# class_mapping = [(60, 0, 255),(51, 255, 255),(255, 0, 255),(255, 255, 0),(0, 255, 0),(0, 153, 0),(255, 0, 0),(255, 204, 204)]
class_name = ["skin","eye","brow","lip","mouth","nose","hair","ear"]
class_mapping = [(255, 0, 0),(255, 0, 255),(51, 255, 255),(255, 255, 0),(0, 255, 0),(0, 153, 0),(60, 0, 255),(255, 204, 204)]
class_mapping = [color[::-1] for color in class_mapping]

paths = glob.glob("image/*.json")
newpaths = "org-label"
for item in paths:
    with open(item, 'r') as f:
        data = json.load(f)
        face_featuers = {}
        for name in class_name:
            face_featuers[name] = []
        for jsondata in data["shapes"]:
            if jsondata["label"] in face_featuers:
                face_featuers[jsondata["label"]].append(jsondata["points"])
        w = data["imageWidth"]
        h = data["imageHeight"]
        canvers = np.zeros((h, w,3), dtype="uint8")

        for idx,featuer_name in enumerate(class_name):
            if len(face_featuers[featuer_name]) == 0:
                pass
            else:
                for featuer in face_featuers[featuer_name]:
                    featuer_np = np.array(featuer)
                    featuer_np = featuer_np.reshape((-1,1,2))
                    featuer_np = np.round(featuer_np).astype("int32")
                    cv2.fillPoly(canvers,[featuer_np],class_mapping[idx])
        dir = os.path.split(item)
        filename = dir[-1]
        filename,_ = os.path.splitext(filename)
        newfilename = os.path.join(dir[0],filename)
        cv2.imwrite(os.path.join(newfilename+".png"),canvers)


