import cv2
import os


def mkdir(name):
    path = 'img/'+name
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print("Hello, {0}, your folder has been created.".format(name))
    else:
        print("{0}, your folder has existed.".format(name))
    return path


def generate(name):
    # 人脸识别, 参数为分类器所在地址
    faceCascade = cv2.CascadeClassifier('/home/linshengfeng/PycharmProjects/face_detect_client/venv/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml')

    # 识别眼睛
    # eyeCascade = cv2.CascadeClassifier('/home/linshengfeng/PycharmProjects/face_detect_client/venv/lib/python3.8/site-packages/cv2/data/haarcascade_eye.xml')

    # 开启摄像头
    cap = cv2.VideoCapture(0)
    ok = True
    count = 0   # result = []
    path = mkdir(name)
    while ok:
        # 读取摄像头中的图像，ok为是否读取成功的判断参数
        ok, img = cap.read()
        # 转换成灰度图像
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 人脸检测
        """
        大概意思是Haar cascade的工作原理是一种“滑动窗口”的方法，通过在图像中不断的“滑动检测窗口”来匹配人脸。
        因为图像的像素有大有小，图像中的人脸因为远近不同也会有大有小，所以需要通过scaleFactor参数设置一个缩小的比例，对图像进行逐步缩小来检测，这个参数设置的越大，计算速度越快，但可能会错过了某个大小的人脸。
        其实可以根据图像的像素值来设置此参数，像素大缩小的速度就可以快一点，通常在1~1.5之间。
        那么，经过多次的迭代，实际会检测出很多很多个人脸，这一点可以通过把minNeighbors 设为0来验证。
        所以呢，minNeighbors参数的作用就来了，只有其“邻居”大于等于这个值的结果才认为是正确结果。
        ————————————————
        版权声明：本文为CSDN博主「赵赵赵颖」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
        原文链接：https://blog.csdn.net/leaf_zizi/article/details/107637433
        """
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(32, 32)
        )

        # 在检测人脸的基础上检测眼睛
        for (x, y, w, h) in faces:
            # 画矩形
            cv2.rectangle(img, (x, y), (x + w, y + w), (255, 0, 0))
            count += 1
            cv2.imwrite(path+'/'+str(count)+".jpg", gray[y:y+h, x:x+w])
            cv2.imshow('video', img)
            # fac_gray = gray[y: (y + h), x: (x + w)]
            # result = []
            # eyes = eyeCascade.detectMultiScale(fac_gray, 1.3, 2)

            # 眼睛坐标的换算，将相对位置换成绝对位置
            """for (ex, ey, ew, eh) in eyes:
                result.append((x + ex, y + ey, ew, eh))"""

        """for (ex, ey, ew, eh) in result:
            cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)"""

        k = cv2.waitKey(1)
        if k == 27:  # 按 'ESC' to quit
            break
        elif count >= 1200:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    your_name = input("Please input your name: ")
    generate(your_name)
