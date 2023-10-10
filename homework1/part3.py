import os
figure_save_path = "figure"
import warnings
warnings.filterwarnings("error")
import numpy as np
np.random.seed(0)
import matplotlib.pyplot as plt
from PIL import Image

X1_start = 0
X2_start = 0
X3_start = 0
X4_start = 0
X5_start = 0

X6_start = 0
X7_start = 0
X8_start = 0
X9_start = 0
X0_start = 0


X1_end = 2
X2_end = 2
X3_end = 2
X4_end = 2
X5_end = 2

X6_end = 2
X7_end = 2
X8_end = 2
X9_end = 2
X0_end = 2


N = 100000000

num_points     = list(range(N))
random_x1points = np.random.uniform(X1_start, X1_end, N)
random_x2points = np.random.uniform(X2_start, X2_end, N)
random_x3points = np.random.uniform(X3_start, X3_end, N)
random_x4points = np.random.uniform(X4_start, X4_end, N)
random_x5points = np.random.uniform(X5_start, X5_end, N)

random_x6points = np.random.uniform(X6_start, X6_end, N)
random_x7points = np.random.uniform(X7_start, X7_end, N)
random_x8points = np.random.uniform(X8_start, X8_end, N)
random_x9points = np.random.uniform(X9_start, X9_end, N)
random_x0points = np.random.uniform(X0_start, X0_end, N)

f = lambda i: np.exp(-(random_x1points[i]**2 +
                       random_x2points[i]**2 +
                       random_x3points[i]**2 +
                       random_x4points[i]**2 +
                       random_x5points[i]**2 +

                       random_x6points[i]**2 +
                       random_x7points[i]**2 +
                       random_x8points[i]**2 +
                       random_x9points[i]**2 +
                       random_x0points[i]**2 ))

guess = np.array(list(map(f, num_points)))
ave = sum(guess)/N
I = ave*(X1_end-X1_start)*\
        (X2_end-X2_start)*\
        (X3_end-X3_start)*\
        (X4_end-X4_start)*\
        (X5_end-X5_start)*\
        (X6_end-X6_start)*\
        (X7_end-X7_start)*\
        (X8_end-X8_start)*\
        (X9_end-X9_start)*\
        (X0_end-X0_start)

S2 = sum((guess-ave)**2)/(N-1)
S  = S2**0.5

print(I, "\pm", S/N**0.5)
