import os
figure_save_path = "file_fig"
import warnings
warnings.filterwarnings("error")
import numpy as np
np.random.seed(0)
import matplotlib.pyplot as plt
from PIL import Image

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False

######
#待抽样分布x~f(x)
#已有分布g(x)
#建议分布c*g(x)
#在概率空间有c*g(x)恒大于f(x)

#step 1 按f(x)抽样 得x,x_i~f(x) x.size 
#step 2 生成u,u_i~U[0, max(c*g(x))] u.size = x.size
#step 3 从x中选取满足u_i<f(x_i)的样本
######

# 假设f1为我们想要进行抽样的分布
f1 = lambda x:0.3/np.sqrt(np.pi*2)*np.exp(-(x+2)**2/2) + 0.7/np.sqrt(np.pi*2)*np.exp(-(x-4)**2/2)


x = np.arange(-10, 10, 0.01)
plt.plot(x, f1(x), color='red', label='待抽样分布', linewidth=3)  # 画出这个分布的图像


# 计划采用[-10, 10]之间的均匀分布为已有分布
size = int(1e+7)
s = np.random.uniform(-10, 10, size)  # 生成数据
t = 0.3/np.sqrt(np.pi*2)*np.exp(-(s+2)**2/2) + 0.7/np.sqrt(np.pi*2)*np.exp(-(s-4)**2/2)


c  = 6
def decro(func):
    global c
    def wrapper(x):
        return c*func(x)
    return wrapper

@decro
def f2(X):
    r = np.zeros(X.size)
    for x in range(X.size):
        if X[x]>=-10:
            if X[x]<=10:
                r[x] = 1/20
            else:
                r[x] = 0
        else:
            r[x] = 0
    return r

sample_test = f2(x)    
plt.plot(x, sample_test, label='建议分布', linewidth=3)  # 画出建议分布的图像


ran = np.random.uniform(0, c*max(sample_test), size)

sampling = s[ran < t]  # 生成的随机数小于待抽样分布的函数值则接受
plt.hist(sampling, bins=200, label='抽样数据', color='green', density=True)
plt.legend(prop={'size': 20})
plt.show()
