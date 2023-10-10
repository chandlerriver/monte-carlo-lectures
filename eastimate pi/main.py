import os
figure_save_path = "file_fig"
import warnings
warnings.filterwarnings("error")
import numpy as np
np.random.seed(0)
import matplotlib.pyplot as plt
from PIL import Image

def main(times=100):
    print("RNG:", "Python numpy.random.random")
    print("开始估算")
    Nlist = [1000000*i for i in range(1, times)]
    Pilist = []
    Slist  = []
    gif_frames = []

    for i in range(1, times):
        N = Nlist[i-1]
        random_points = np.random.random((2, N))
        radius = sum(random_points[:]**2)
        count = np.sum(radius<=1)
        ave = count/N
        S2 = ((N-count)*ave**2+count*(1-ave)**2)/(N-1)
        S  = S2**0.5 
        Pilist.append(4*ave)    
        Slist.append(4*S/N**0.5)

        plt.xlabel("test_times")
        plt.ylabel("eastimate_pi_value", rotation=90)
        plt.title("Eastimate Pi")
        plt.errorbar(Nlist[:i], Pilist[:i], Slist[:i], label="eastimate pi", c="green")
        plt.axhline(np.pi,label="exact pi", c="red")
        plt.legend()
        if not os.path.exists(figure_save_path):
            os.makedirs(figure_save_path)
        plt.savefig(os.path.join(figure_save_path, str(i) + ".jpg"))  
        plt.cla()
     
        img = Image.open(os.path.join(figure_save_path, str(i) + ".jpg"))
        gif_frames.append(img)
    print("估算完成")
    print("开始绘制动画")
    gif_frames[0].save("eastimate-pi.gif",
        save_all=True, append_images=gif_frames[1:], duration=200, loop=0)
    print("动画绘制完成")
    
main()
input("press any key to exit")
