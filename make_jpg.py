import os
import glob
import json

import cv2
import numpy as np
newfoloder = "org-img"
paths = glob.glob("image/*")
for item in paths:
    img = cv2.imread(item)
    filename = os.path.basename(item)
    filename = filename.split(".")
    filename[-1] = ".jpg"
    filename = "".join(filename)
    cv2.imwrite(os.path.join(newfoloder,filename),img)


