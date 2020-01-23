import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter
plt.figure(figsize=(5,3))
plt.ylabel("Long Median FCT \nSlow Down (%)", fontsize=17)
plt.xlabel("Load (%)", fontsize=17)
plt.yscale('log')
Speed = [50,60,70,80,90]

#SlowDown = [3.13,3.91,5.19,7.41,13.64]
SlowDown = [2.91, 3.60, 4.75, 6.89, 12.88]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-', color='blue', label='BFC', marker='o')

#SlowDown = [6.82,11.99,31.6,67.14,102.93]
SlowDown = [5.56, 9.68, 30.07, 71.17, 113.54]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-.', color='green', label='HPCC', marker='s')

#SlowDown = [3.12,4.03,5.73,8.81,16.81]
SlowDown = [3.71,5.92, 13.25, 26.29, 50.2]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='red', label='DCQCN', marker='^')

SlowDown = [4.03,5.14,7.12,10.3,19.17]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='orange', label='DCTCP', marker='x')

SlowDown = [5.66, 10.2, 33.372, 75.65, 118]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, ':', color='brown', label='HPCC+SFQ', marker='<')
ax = plt.axes()
ax.xaxis.set_ticks(Speed)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_minor_ticks():
	tick.label.set_fontsize(14)
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(-0.3, 0.94, 1.3, 0.94), loc=3, ncol=3, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(5,3))
plt.ylabel("Small 99pct FCT \nSlow Down (%)", fontsize=17)
plt.xlabel("Load (%)", fontsize=17)
plt.yscale('log')
Speed = [50,60,70,80,90]

#SlowDown = [3.13,3.91,5.19,7.41,13.64]
SlowDown = [1.11, 1.14, 1.2, 1.32, 7.14]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-', color='blue', label='BFC', marker='o')

#SlowDown = [6.82,11.99,31.6,67.14,102.93]
SlowDown = [2.44, 2.66, 2.98, 3.4, 3.98]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-.', color='green', label='HPCC', marker='s')

#SlowDown = [3.12,4.03,5.73,8.81,16.81]
SlowDown = [4.02, 4.533, 5.17, 5.87, 6.83]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='red', label='DCQCN', marker='^')

SlowDown = [3.1,3.44,3.94, 4.56, 5.63]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='orange', label='DCTCP', marker='x')

SlowDown = [2.05, 2.08, 2.17, 2.44, 3.02]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, ':', color='brown', label='HPCC+SFQ', marker='<')





plt.show()