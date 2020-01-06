import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter


plt.figure(figsize=(6,3))
plt.ylabel("FCT Slowdown", fontsize=15)
plt.xlabel("Flow Size (KB)", fontsize=15)
plt.xscale('log')
plt.yscale('log')
#plt.ylim([1,19])
bins = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
#Slowdown = [2.14181148469966, 2.2119565217391304, 2.404166666666667, 2.80875, 3.584732142857143, 6.407472527472527, 8.4394, 9.861733870967742, 9.70844056372549]
#plt.plot(bins[:len(bins)-2], Slowdown[:len(bins)-2], linestyle='-', color='blue', label='BFC')
#Slowdown = [15.873470193446506, 14.702, 14.925625, 14.430104166666666, 12.32778846153846, 8.958793103448276, 11.156061224489797, 16.76635632183908, 31.32118849436308]
#plt.plot(bins[:len(bins)-2], Slowdown[:len(bins)-2], linestyle='--', color='red', label='DCQCN + Win')
Slowdown = [2.511514221073045, 2.66328125, 3.316, 4.474090909090909, 6.438836206896552, 9.270338983050847, 10.50847067039106, 10.907072916666667, 10.600346331452027]
plt.plot(bins[:len(bins)], Slowdown[:len(bins)], linestyle='-', color='blue', label='BFC')
Slowdown = [16.458638695492855, 13.74625, 12.125277777777777, 10.523472222222223, 9.898020833333334, 11.503632075471698, 11.17608552631579, 11.557673865300146, 11.67114784649365]
plt.plot(bins[:len(bins)], Slowdown[:len(bins)], linestyle='--', color='red', label='DCQCN + Win')
ax = plt.axes()
plt.legend(bbox_to_anchor=(0.05, 0.97, 0.9, 0.97), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)
ax.get_yaxis().set_ticks([2,4,8,16], minor=True)
ax.get_yaxis().set_ticks([], minor=False)
ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())
ax.yaxis.get_minor_formatter().set_scientific(False)
ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
ax.yaxis.get_major_formatter().set_scientific(False)

#ax.get_yaxis().set_minorticks([2,4,8])
for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(12)
for tick in ax.yaxis.get_minor_ticks():
        tick.label.set_fontsize(12)
for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(12)

plt.tight_layout()

plt.figure(figsize=(6,3))
plt.ylabel("FCT Slowdown", fontsize=15)
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Flow Size (KB)", fontsize=15)
plt.ylim(bottom=1)
bins = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
#Slowdown = [1.0034697053681831, 1.0163249516441006, 1.0309613526570047, 1.065262904003859, 1.1232067307692308, 1.4692620624408703, 2.4710170231340025, 5.46134163208852, 12.378630937261875]
#plt.plot(bins[:len(bins)-2], Slowdown[:len(bins)-2], linestyle='-', color='blue', label='BFC')
#Slowdown = [2.1396848828378863, 2.1608075435203093, 2.0988091787439616, 2.142727930535456, 2.1391927710843373, 2.175617313150426, 2.220450513538749, 2.4647062190003814, 51.34139513998944]
#plt.plot(bins[:len(bins)-2], Slowdown[:len(bins)-2], linestyle='--', color='red', label='DCQCN + Win')
Slowdown = [1.0136256509269355, 1.0360444550669217, 1.0730166666666667, 1.1481309297912714, 1.2615037243947858, 1.9656348511383537, 3.4889441747572816, 6.243870211102424, 9.064813500258131]
plt.plot(bins[:len(bins)], Slowdown[:len(bins)], linestyle='-', color='blue', label='BFC')
Slowdown = [2.2727606771428737, 2.243324569789675, 2.1901595238095237, 2.169637784090909, 2.001480263157895, 2.349952445652174, 2.5453309352517985, 9.550392992424243, 17.48751749820531]
plt.plot(bins[:len(bins)], Slowdown[:len(bins)], linestyle='--', color='red', label='DCQCN + Win')

ax = plt.axes()
ax.get_yaxis().set_ticks([1,2,4,8], minor=True)
ax.get_yaxis().set_ticks([], minor=False)
ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())
ax.yaxis.get_minor_formatter().set_scientific(False)
ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
ax.yaxis.get_major_formatter().set_scientific(False)
for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(12)
for tick in ax.yaxis.get_minor_ticks():
        tick.label.set_fontsize(12)
for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(12)
plt.legend(bbox_to_anchor=(0.05, 0.97, 0.9, 0.97), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)
plt.tight_layout()
plt.show()