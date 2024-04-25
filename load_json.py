import os
import glob
import json
import numpy as np
class_name = ["hair","brow","eye","mouth","nose","skin","ear"]


paths = glob.glob("../img/*.json")
for item in paths:
    with open(item, 'r') as f:
        data = json.load(f)
        face_featuers = {}
        for jsondata in data["shapes"]:
            if jsondata["label"] in face_featuers:
                face_featuers[jsondata["label"]].append(jsondata["points"])
            else:
                jsondata["label"] = []
                face_featuers[jsondata["label"]].append(np.array(jsondata["points"]))


        print()