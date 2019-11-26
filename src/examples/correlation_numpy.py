import numpy as np
import sys
sys.path.append('./../')

from pilot_utils import build_pilot_scatter

np.random.seed(1)

# 1000 random integers between 0 and 50
x = np.random.randint(0, 50, 999)

# Positive Correlation with some noise
y = x + np.random.normal(0, 10, 999)

r = np.corrcoef(x,y)

build_pilot_scatter(data_x=x, data_y=y, title="Compare Germany vs China",showTable=True, saveFig=True);