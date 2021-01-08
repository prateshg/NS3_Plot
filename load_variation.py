import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter

plt.figure(figsize=(4,3))
#plt.ylabel("FCT Slow Down\nMedian (Size>3MB)", fontsize=16)
plt.ylabel("FCT Slow Down\nAverage (Size>3MB)", fontsize=16)
plt.xlabel("Load (%)", fontsize=16)
plt.yscale('log')
Speed = [50,60,70,80,90, 95]

#SlowDown = [3.1, 3.8, 4.98, 6.8, 11, 15.4]#Median
SlowDown = [3.38, 4.2, 5.67, 8.15, 13.34, 18.46]#Avg
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-', color='blue', label='BFC 32', marker='o')


#SlowDown = [5.4, 8.9, 20.1, 40, 59]#Median
SlowDown = [6.58, 11.07, 24.1]#Avg
SlowDown = np.array(SlowDown)
plt.plot(Speed[0:3], SlowDown[0:3],  '-.', color='green', marker='s')# label='HPCC', marker='s')

#SlowDown = [3.6,5.92, 12.2, 23, 40]
#SlowDown = np.array(SlowDown)
#plt.plot(Speed[0:5], SlowDown[0:5], '--', color='red', label='DCQCN', marker='^')

#SlowDown = [3.14, 3.83, 5, 6.85, 11.4, 16]#Median
SlowDown = [3.37, 4.21, 5.67, 8.15, 13.61, 18.9]#Avg
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='red', label='BFC 128', marker='^')

#SlowDown = [4.03,5.2,7.12,10,16.8, 22]#Median
SlowDown = [4.23, 5.5, 7.63, 11, 18.61, 24.73]#Avg
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='orange', marker='x')#label='DCTCP', marker='x')

ax = plt.axes()
ax.get_yaxis().set_ticks([4,8,16], minor=True)
#plt.ylim([3,45])
ax.get_yaxis().set_ticks([], minor=False)
ax.get_xaxis().set_ticks([50,60,70,80,90, 95])
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
plt.legend(bbox_to_anchor=(-0.05, 0.98, 1.1, 0.98), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(4,3))
plt.ylabel('FCT Slow Down\n99 pct (Size<3KB)', fontsize=16)
plt.xlabel("Load (%)", fontsize=16)
plt.yscale('log')
Speed = [50,60,70,80,90, 95]

SlowDown = [1.1, 1.13, 1.19, 1.29, 2.63, 12.75]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-', color='blue', marker='o')#label='BFC 32', marker='o')


SlowDown = [2.44,2.65, 2.93, 3.23,3.61]
SlowDown = np.array(SlowDown)
plt.plot(Speed[0:3], SlowDown[0:3],  '-.', color='green', label='HPCC', marker='s')

#SlowDown = [4.02, 4.6, 5.2, 5.87, 6.6]
#SlowDown = np.array(SlowDown)
#plt.plot(Speed[0:5], SlowDown[0:5], '--', color='red', label='DCQCN', marker='^')

SlowDown = [1.1, 1.14, 1.2, 1.32, 1.61, 1.99]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='red', marker='^')#label='BFC 128', marker='^')


SlowDown = [3.1,3.5,3.94, 4.56, 5.63, 6.1]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='orange', label='DCTCP', marker='x')
plt.legend(bbox_to_anchor=(-0.05, 0.98, 1.1, 0.98), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
ax = plt.axes()
ax.get_yaxis().set_ticks([1,2,4,8], minor=True)
ax.get_yaxis().set_ticks([], minor=False)
ax.get_xaxis().set_ticks([50,60,70,80,90, 95])
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

plt.figure(figsize=(4,3))
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
plt.plot(Speed[0:3], SlowDown[0:3],  '-.', color='green', label='HPCC', marker='s')

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

plt.figure(figsize=(4,3))
plt.ylabel('FCT Slow Down\n99 pct (Size<3KB)', fontsize=16)
plt.xlabel("Load (%)", fontsize=16)
plt.yscale('log')
Speed = [50,60,70,80,90]

SlowDown = [1.16, 1.22, 1.33, 1.53, 3.37]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-', color='blue', label='BFC', marker='o')


SlowDown = [2.54, 2.7, 2.84,2.95, 3.0]
SlowDown = np.array(SlowDown)
plt.plot(Speed[0:3], SlowDown[0:3],  '-.', color='green', label='HPCC', marker='s')

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