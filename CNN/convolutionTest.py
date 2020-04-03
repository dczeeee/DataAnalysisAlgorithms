import numpy as np
from scipy import signal

# 设置原图像
img = np.array([
    [10, 10, 10, 10, 10],
    [10, 5, 5, 5, 10],
    [10, 5, 5, 5, 10],
    [10, 5, 5, 5, 10],
    [10, 10, 10, 10, 10]
])

# 设置卷积核
fil = np.array([
    [-1, -1, 0],
    [-1, 0, 1],
    [0, 1, 1]
])

res = signal.convolve2d(img, fil, 'valid')

print(res)

