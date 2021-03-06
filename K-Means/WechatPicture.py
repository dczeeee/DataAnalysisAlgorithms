# -*- coding:utf-8 -*-
import numpy as np
import PIL.Image as image
from sklearn import preprocessing
from sklearn.cluster import KMeans
from skimage import color


# 加载图像，并对数据进行规范化
def load_data(filePath):
    # 读文件
    f = open(filePath, 'rb')
    data = []
    # 得到图像像素值
    img = image.open(f)
    # 得到图像尺寸
    width, height = img.size
    for x in range(width):
        for y in range(height):
            # 得到点(x,y)的RGB值
            r, g, b = img.getpixel((x, y))
            data.append([r, g, b])
    f.close()
    # min-max规范化
    minmax_scaler = preprocessing.MinMaxScaler()
    data = minmax_scaler.fit_transform(data)
    return np.mat(data), width, height


# 加载图像，得到规范化的结果img，以及图像尺寸
# img, width, height = load_data('weixin.jpg')
img, width, height = load_data('baby.jpg')

# 用K-Means对图像进行2聚类
kmeans = KMeans(n_clusters=2)
kmeans.fit(img)
label = kmeans.predict(img)

# 将图像聚类结果，转化成图像尺寸的矩阵
label = label.reshape([width, height])

# 创建个新图像pic_mark，用来保存图像聚类的结果，并设置不同的灰度值
pic_mark = image.new('L', (width, height))
for x in range(width):
    for y in range(height):
        # 根据类别设置图像灰度, 类别0 灰度值为255， 类别1 灰度值为127
        pic_mark.putpixel((x, y), int(256/(label[x][y]+1))-1)
# pic_mark.save('weixin_mark.jpg', 'JPEG')
pic_mark.save('baby_mark.jpg', 'JPEG')


# 用K-Means对图像进行16聚类
kmeans =KMeans(n_clusters=16)
kmeans.fit(img)
label = kmeans.predict(img)
# 将图像聚类结果，转化成图像尺寸的矩阵
label = label.reshape([width, height])

# 将聚类标识矩阵转化为不同颜色的矩阵
label_color = (color.label2rgb(label)*255).astype(np.uint8)     # 将分类标识矩阵转换成不同颜色的矩阵
label_color = label_color.transpose(1, 0, 2)    # 旋转
images = image.fromarray(label_color)   # 将矩阵转换为图像
# images.save('weixin_mark_color.jpg')
images.save('baby_mark_color.jpg')
