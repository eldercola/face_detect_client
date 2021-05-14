import numpy as np
from PIL import Image
import os
import cv2
import manage_img_fold as mif

path = 'img'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('/home/linshengfeng/PycharmProjects/face_detect_client/venv/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml')


def getImagesAndLabels(path):
    print(path)
    imagePaths = []
    paths = [os.path.join(path, f) for f in os.listdir(path)]
    for singlePerson in paths:
        imagePaths = imagePaths + [os.path.join(singlePerson, f) for f in os.listdir(singlePerson)]
    print(imagePaths)
    faceSamples = []
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')
        # id = int(os.path.split(imagePath)[-1].split(".")[0])
        id = mif.getYourFoldNum(os.path.dirname(imagePath)[4:])
        faces = detector.detectMultiScale(img_numpy)
        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y + h, x: x + w])
            ids.append(id)
    print(ids)
    return faceSamples, ids


print("PLease wait...")
faces, ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

recognizer.write(r'face_trainer/trainer.yml')
print("{0} faces trained. Exiting Program".format(len(np.unique(ids))))
