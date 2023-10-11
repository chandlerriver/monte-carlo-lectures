import os
figure_save_path = "file_fig"
import warnings
warnings.filterwarnings("error")
import numpy as np
np.random.seed(0)
import matplotlib.pyplot as plt
from PIL import Image
import time


f = lambda x,y: x**2 * y**2
def cal(N, X_start=0, X_end=1, Y_start=0, Y_end=1, f=f):
    
    start = time.time()
    random_xpoints = np.random.uniform(X_start, X_end, N)
    random_ypoints = np.random.uniform(Y_start, Y_end, N)

    X = np.arange(X_start, X_end, 100)
    Y = np.arange(Y_start, Y_end, 100)

    guess = np.array(list(map(f, random_xpoints, random_ypoints)))

    ave = sum(guess)/N
    I = ave*(X_end-X_start)*(Y_end-Y_start)

    S2 = sum((guess-ave)**2)/(N-1)
    S  = S2**0.5
    end = time.time()
    
    return I,S/N**0.5

def main():
    print("RNG:", "Python numpy.random.random")
    print("开始估算")
    
    times = 60
    
    Nlist = [50000*i for i in range(1, times)]
    Ilist = []
    Slist = []
    gif_frames = []
    
    for i in range(1, times):
        result = cal(Nlist[i-1])
        Ilist.append(result[0])
        Slist.append(result[1])

        plt.title("MC 2D integral")
        plt.xlabel("times")
        plt.ylabel("2D NIntegral", rotation=90)

        plt.errorbar(Nlist[:i], Ilist[:i], Slist[:i], label="MC 2D integral", c="green")
        plt.axhline(0.11111111, label="exact integral", c="red")
        plt.legend()
        if not os.path.exists(figure_save_path):
            os.makedirs(figure_save_path)
        else:
            pass
        plt.savefig(os.path.join(figure_save_path, str(i) + ".jpg"))
        plt.cla()
        
        img = Image.open(os.path.join(figure_save_path, str(i) + ".jpg"))
        gif_frames.append(img)

    print("估算完成")
    print("开始绘制动画")
    gif_frames[0].save("MC 2D integral.gif",
        save_all=True, append_images=gif_frames[1:], duration=200, loop=0)
    print("动画绘制完成")

main()
input("press any key to exit")
