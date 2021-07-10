Core codes are from: https://zhuanlan.zhihu.com/p/127039696

get_face is the python file that can use your camera to take 1200 photos into a fold.

train_face is the python file that can use valid photos which are in the fold you create after the get_face.

validate is the python file that can use your camera to validate if you are in current frame.

manage_img_fold is the util file helps you get the fold name list under fold img.

来说说最后应用到真实环境的时候，怎么分类:(突然中文是因为晚上刚面试完发现了这个漏洞)  
其实，在训练的时候，对于每一张人脸，都有对应的直方图。在检测过程中，采用KNN分类算法，先将识别到的人脸进行转换生成对应直方图，然后计算这张直方图的距离(把所有数据加起来), 接着去跟已有人脸的直方图"距离"进行比较，找到最近的那一个，然后就判断当前人脸是属于最近的那一类。  
至于如何训练呢，```挖个坑```，过两天填, 先忙别的去了  
