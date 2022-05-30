import os
import json
from json import JSONEncoder
import numpy as np
import face_recognition


class NumpyArrEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


data, i = [], 0
for x in os.listdir('Apps'):

    for y in os.listdir(f"Apps/{x}"):
        name = y.split(".")[0]
        app_name = f"Apps/{x}/{y}"
        picture = face_recognition.load_image_file(app_name)
        encod_picture = face_recognition.face_encodings(picture)[0]

        d = {
            'name': name,
             'app_name': app_name,
             'dir': x,
             'encoding': encod_picture}

        data.append(d)

encodedNumpyData = json.dumps(data, cls=NumpyArrEncoder)

with open("encode.json", "w") as outfile:
    outfile.write(encodedNumpyData)
