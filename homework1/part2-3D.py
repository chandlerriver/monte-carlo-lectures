import os
figure_save_path = "file_fig"
import warnings
warnings.filterwarnings("error")
import numpy as np
np.random.seed(0)
import matplotlib.pyplot as plt
from PIL import Image

print("RNG:", "Python numpy.random.random")
N = 10000000

num            = list(range(N))
xpoints = np.random.random(N) * 2
ypoints = np.random.random(N) * 2
zpoints = np.random.random(N) * 3

V = 2 * 2 * 3

f = lambda i:zpoints[i]<=3-xpoints[i]/2-ypoints[i]/2

counts = np.sum(np.array(list(map(f, num))))
ave = counts/N
S2  = counts*(1-ave)**2/(N-1) + (N-counts)*ave**2/(N-1)
S   = S2**0.5
print(ave*V, "\pm", S/N**0.5*V)
