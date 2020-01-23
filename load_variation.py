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
plt.ylabel("FCT Slow Down\nMedian (Size>3MB)", fontsize=16)
plt.xlabel("Load (%)", fontsize=16)
plt.yscale('log')
Speed = [50,60,70,80,90]

SlowDown = [2.91, 3.60, 4.75, 6.89, 12.88]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-', color='blue', label='BFC', marker='o')

SlowDown = [5.56, 9.68, 30.07, 71.17, 113.54]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-.', color='green', label='HPCC', marker='s')

SlowDown = [3.71,5.92, 13.25, 26.29, 50.2]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='red', label='DCQCN', marker='^')

SlowDown = [4.03,5.14,7.12,10.3,19.17]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='orange', label='DCTCP', marker='x')

ax = plt.axes()
ax.get_yaxis().set_ticks([2,4,8,16,32, 64], minor=True)
ax.get_yaxis().set_ticks([], minor=False)
ax.get_xaxis().set_ticks([50,60,70,80,90])
ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())
ax.yaxis.get_minor_formatter().set_scientific(False)
ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
ax.yaxis.get_major_formatter().set_scientific(False)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_minor_ticks():
	tick.label.set_fontsize(14)
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(-0., 0.96, 1.0, 0.96), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(5,3))
plt.ylabel('FCT Slow Down\n99 pct (Size<3KB)', fontsize=16)
plt.xlabel("Load (%)", fontsize=16)
plt.yscale('log')
Speed = [50,60,70,80,90]

SlowDown = [1.11, 1.14, 1.2, 1.32, 7.14]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-', color='blue', label='BFC', marker='o')


SlowDown = [2.44, 2.66, 2.98, 3.4, 3.98]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-.', color='green', label='HPCC', marker='s')

SlowDown = [4.02, 4.533, 5.17, 5.87, 6.83]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='red', label='DCQCN', marker='^')

SlowDown = [3.1,3.44,3.94, 4.56, 5.63]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='orange', label='DCTCP', marker='x')
plt.legend(bbox_to_anchor=(-0., 0.96, 1.0, 0.96), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
ax = plt.axes()
ax.get_yaxis().set_ticks([1,2,4,8], minor=True)
ax.get_yaxis().set_ticks([], minor=False)
ax.get_xaxis().set_ticks([50,60,70,80,90])
ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())
ax.yaxis.get_minor_formatter().set_scientific(False)
ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
ax.yaxis.get_major_formatter().set_scientific(False)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_minor_ticks():
	tick.label.set_fontsize(14)
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.tight_layout()


#All links are equally congested

plt.figure(figsize=(5,3))
plt.ylabel("FCT Slow Down\nMedian (Size>3MB)", fontsize=16)
plt.xlabel("Load (%)", fontsize=16)
plt.yscale('log')
Speed = [50,60,70,80,90]

SlowDown = [3.22,4.2, 5.9, 8.75, 14.6]
#SlowDown = [3.47, 4.9, 6.4, 9.6, 16.2]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-', color='blue', label='BFC', marker='o')

SlowDown = [4.95, 7.47, 10.8, 14.65, 23.35]
#SlowDown = [6.7, 11.4, 21, 30.7, 41.7]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-.', color='green', label='HPCC', marker='s')

SlowDown = [3.5, 4.9, 7.6, 12.1, 19]
#SlowDown = [5.3, 8.1, 12.7, 19, 27.7]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='red', label='DCQCN', marker='^')

SlowDown = [4.03,5.33, 7.5, 11.1, 18.7]
#SlowDown = [4.4, 5.9, 8.3, 12.4, 21.3]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='orange', label='DCTCP', marker='x')

ax = plt.axes()
ax.get_yaxis().set_ticks([4,8,16,32], minor=True)
ax.get_yaxis().set_ticks([], minor=False)
ax.get_xaxis().set_ticks([50,60,70,80,90])
ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())
ax.yaxis.get_minor_formatter().set_scientific(False)
ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
ax.yaxis.get_major_formatter().set_scientific(False)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_minor_ticks():
	tick.label.set_fontsize(14)
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(-0., 0.96, 1.0, 0.96), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(5,3))
plt.ylabel('FCT Slow Down\n99 pct (Size<3KB)', fontsize=16)
plt.xlabel("Load (%)", fontsize=16)
plt.yscale('log')
Speed = [50,60,70,80,90]

SlowDown = [1.16, 1.22, 1.33, 1.53, 3.37]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-', color='blue', label='BFC', marker='o')


SlowDown = [2.54, 2.7, 2.84,2.95, 3.0]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-.', color='green', label='HPCC', marker='s')

SlowDown = [4.94, 5.6, 6.3, 6.9, 7.4]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='red', label='DCQCN', marker='^')

SlowDown = [3.5,3.93,4.41, 4.91, 5.52]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='orange', label='DCTCP', marker='x')
plt.legend(bbox_to_anchor=(-0., 0.96, 1.0, 0.96), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
ax = plt.axes()
ax.get_yaxis().set_ticks([1,2,4,8], minor=True)
ax.get_yaxis().set_ticks([], minor=False)
ax.get_xaxis().set_ticks([50,60,70,80,90])
ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())
ax.yaxis.get_minor_formatter().set_scientific(False)
ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
ax.yaxis.get_major_formatter().set_scientific(False)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_minor_ticks():
	tick.label.set_fontsize(14)
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.tight_layout()


plt.show()