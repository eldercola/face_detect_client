Core codes are from: https://zhuanlan.zhihu.com/p/127039696

get_face is the python file that can use your camera to take 1200 photos into a fold.

train_face is the python file that can use valid photos which are in the fold you create after the get_face.

validate is the python file that can use your camera to validate if you are in current frame.

manage_img_fold is the util file helps you get the fold name list under fold img.

来说说最后应用到真实环境的时候，怎么检测:    
  
其实，在训练的时候，对于每一张人脸，都有对应的矩阵(可以转换为直方图)。在检测过程中，先将识别到的人脸先进行区域划分，再利用LBP算法对每个区域进行特征提取转换生成对应直方图，然后计算这张直方图的距离(把所有数据加起来)。    
  
检测过程中，先识别出人脸，再对对应的人脸区域做直方图提取。接着跟人脸库中的已有人脸进行比较，比较的过程是计算对应区域上的直方图距离差的加权平均（加权平均是为了减少噪声的干扰）。接着找出与当前人脸距离差之和加权平均最小的那张图片的标签，即为当前人脸的标签。
