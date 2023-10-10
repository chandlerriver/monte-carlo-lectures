import os
figure_save_path = "file_fig"
import warnings
warnings.filterwarnings("error")
import numpy as np
np.random.seed(0)
import matplotlib.pyplot as plt
from PIL import Image

X_start = 0
Y_start = 0

X_end = 1
Y_end = 1

N = 10000000

num_points     = list(range(N))
random_xpoints = np.random.uniform(X_start, X_end, N)
random_ypoints = np.random.uniform(Y_start, Y_end, N)

X = np.arange(X_start, X_end, 100)
Y = np.arange(Y_start, Y_end, 100)

f = lambda i: random_xpoints[i]**2 * random_ypoints[i]**2
guess = np.array(list(map(f, num_points)))
ave = sum(guess)/N
I = ave*(X_end-X_start)*(Y_end-Y_start)

S2 = sum((guess-ave)**2)/(N-1)
S  = S2**0.5

print(I, "\pm", S/N**0.5)
