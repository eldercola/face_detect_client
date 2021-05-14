import os

def getImgList():
    fold = 'img'
    path_list = os.listdir(fold)
    return path_list


def getYourFoldNum(name):
    fold_list = getImgList()
    for i in range(len(fold_list)):
        if fold_list[i] == name:
            return i
    return -1
