import os
figure_save_path = "file_fig"
import warnings
warnings.filterwarnings("error")
import numpy as np
np.random.seed(0)
import matplotlib.pyplot as plt
from PIL import Image
from copy import deepcopy

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

f1 = lambda x:0.3/np.sqrt(np.pi*2)*np.exp(-(x+2)**2/2) +\
              0.7/np.sqrt(np.pi*2)*np.exp(-(x-4)**2/2)

x_start = -10
x_end   =  10

def main(f1=f1, x_start=x_start, x_end=x_end, N = int(1e+5), maxiter = 100):

    #已有分布为 numpy.random.random 导出的均匀分布
    
    num_wanted  = deepcopy(N)
    result = np.zeros(num_wanted)
    
    has_get_num = 0
    itertimes   = 0
    random_num  = np.zeros(N)
    x           = np.arange(x_start, x_end, 0.01)
    
    if N >= int(1e4):
        N = int(num_wanted /10)
    else:
        pass
    
    while has_get_num < num_wanted:
        itertimes += 1
        if itertimes >= maxiter:
            print("无法生成足够多的随机数")
            break
        else:
            pass

        #拒绝方法：cg(x)<=f(x)        
        sample_try = np.random.random(N)
        sample_try = (x_end - x_start) * sample_try + x_start

        sample_test= f1(sample_try)
        c = 1 + max(f1(x))
        sample_test *= c
        
        sample_help = np.random.random(N) * (max(sample_test)-0) + 0

        sample = sample_try[sample_help<sample_test]

        if has_get_num + sample.size > num_wanted:
            result[has_get_num:num_wanted-1] = sample[:num_wanted-has_get_num-1]
        else:
            result[has_get_num:has_get_num+sample.size] = sample

        has_get_num += sample.size

        
    plt.plot(x, f1(x), color='red', label='待抽样分布', linewidth=3)
    plt.hist(result, bins=200, label='抽样数据', color='green', density=True)
    plt.legend(prop={'size': 10})
    plt.pause(0.01)
    return result

    
c = main()
