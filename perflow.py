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
plt.ylabel("FCT Slow Down", fontsize=17)
plt.xlabel("Flow Size (KB)", fontsize=17)
plt.xscale('log')
plt.yscale('log')
plt.gca().set_ylim(bottom=1)

Flow_Size = [3,12,48,192,768,3071,12288]
SlowDown = [2.2363346747149566, 2.6521396396396395, 4.8018581081081084, 6.9927763819095476, 9.981457703927493, 10.678372681281619, 9.715823007603491]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='Dest.q16')

SlowDown = [76.579648637978678, 78.377546296296302, 86.142407407407404, 80.876630434782612, 55.078684879288438, 24.842187500000001, 16.46639389822134]
plt.plot(Flow_Size, SlowDown,  '-.', color='green', label='Flow.q16')

SlowDown = [9.4312231801897575, 11.410630841121495, 37.679391891891889, 42.982626146788988, 37.550506230529592, 16.928660669665167, 11.916141836464673]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='Flow.q32')

SlowDown = [1.9401319427984516, 6.8454545454545457, 30.124662162162164, 41.778551912568304, 38.517669753086423, 15.880486425339367, 10.672056727480046]
plt.plot(Flow_Size, SlowDown, ':', color='black', label='Flow.q64')

ax = plt.axes()
ax.get_yaxis().set_ticks([1,2,4,8,16,32,64, 128], minor=True)
ax.get_yaxis().set_ticks([], minor=False)
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
plt.legend(bbox_to_anchor=(-0.1, 1.02, 1.1, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)
plt.tight_layout()


plt.figure(figsize=(4,3))
plt.ylabel("FCT Slow Down", fontsize=17)
plt.xlabel("Flow Size (KB)", fontsize=17)
plt.xscale('log')
plt.yscale('log')
plt.gca().set_ylim(bottom=1)

Flow_Size = [3,12,48,192,768,3071,12288]
SlowDown = [2.2109669811320756, 2.4759090909090911, 4.5656690140845066, 6.8089062499999997, 9.2628685503685499, 10.150449346405228, 9.0882846030042916]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='Dest.q16')

SlowDown = [1.1472790715909982, 1.7331473214285715, 4.1592281879194628, 6.105347222222222, 9.041122611464969, 9.9549056770098723, 9.68645027451959]
plt.plot(Flow_Size, SlowDown,  '-.', color='green', label='Flow.q16')

ax = plt.axes()
ax.get_yaxis().set_ticks([1,2,4,8,16,32,64, 128], minor=True)
ax.get_yaxis().set_ticks([], minor=False)
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
plt.legend(bbox_to_anchor=(-0.1, 1.02, 1.1, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(4,4))
plt.ylabel("CDF", fontsize=19)
plt.xlabel("Active Flow Groups", fontsize=19)

CDF = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Collisions =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4,4,4,5,5,6,8,29]

plt.plot(Collisions, CDF, '-', color='blue', label='Inast.Dest')

Collisions =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,6,6,7,7,8,9,9,10,11,12,14,17,21,26,34,104]

plt.plot(Collisions, CDF,  '-.', color='green', label='Incsat.Flow')

Collisions = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,5,6,7,18]

plt.plot(Collisions, CDF, '--', color='red', label='NoIncast.Dest')
Collisions = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,5,6,7,21]
plt.plot(Collisions, CDF, ':', color='black', label='NoIncast.Flow')


ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(16)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(16)
plt.legend(bbox_to_anchor=(-0.15, 0.97, 1.2, 0.97), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 18}, frameon=False)
plt.tight_layout()
plt.show()

plt.show()