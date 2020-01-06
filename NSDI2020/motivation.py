import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter

plt.figure(figsize=(8,3))
plt.ylabel("FCT Slow Down", fontsize=17)
plt.xlabel("Flow Size (KB)", fontsize=17)
plt.xscale('log')
Flow_Size = [3,12, 48, 192, 768, 3072, 12288, 49152]
SlowDown = [9.7536542832510378, 10.935869565217391, 11.865, 10.942600574712644, 10.126118119266055, 35.17375849451124, 67.516450043566664, 55.606732439577037]
plt.plot(Flow_Size, SlowDown, '-.', color='green', label='10 us')

Flow_Size = [3,12, 48, 192, 768, 3072, 12288, 49152]
SlowDown = [8.82839953409405, 8.3497767857142851, 7.8617708333333329, 6.4161206896551723, 6.8491974708171206, 33.93321578345406, 63.112737068965515, 59.520963935045316]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='20 us')

Flow_Size = [3,12, 48, 192, 768, 3072, 12288, 49152]
SlowDown = [5.0679533476478626, 4.8673863636363635, 4.7528846153846152, 4.465740740740741, 5.0160206718346254, 24.811237494044782, 60.934214531498149, 68.629657063070425]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='30 us')

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(0.1, 1.02, 0.8, 1.02), loc=3, ncol=3, mode="expand", borderaxespad=0., prop={'size': 16}, frameon=False)
plt.xlim([2.7,768])
plt.ylim([0,13])

plt.tight_layout()

plt.figure(figsize=(8,3))
plt.ylabel("FCT Slow Down", fontsize=17)
plt.xlabel("Flow Size (KB)", fontsize=17)
plt.xscale('log')
plt.yscale('log')
Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown = [34.185359132393032, 33.653690476190476, 33.671580188679243, 33.431651376146789, 32.705818965517238, 29.636356707317074, 24.09596994535519, 22.775596816976126, 82.60147544612451]
plt.plot(Flow_Size[:len(Flow_Size)-1], SlowDown[:len(Flow_Size)-1], '-.', color='green', label='10 us')

SlowDown = [19.892973533478173, 19.495833333333334, 19.015566037735848, 18.537274774774776, 17.74380341880342, 15.436483739837398, 11.579587765957447, 13.227056623931624, 77.399186966348566]
plt.plot(Flow_Size[:len(Flow_Size)-1], SlowDown[:len(Flow_Size)-1], '-', color='blue', label='20 us')

SlowDown = [15.799694843147391, 15.491190476190477, 15.164252336448598, 14.697935779816513, 14.053794642857143, 11.853912213740458, 9.4568478260869568, 11.056504629629629, 76.740526107594931]
plt.plot(Flow_Size[:len(Flow_Size)-1], SlowDown[:len(Flow_Size)-1], '--', color='red', label='30 us')
ax = plt.axes()
ax.get_yaxis().set_ticks([10,20,30], minor=True)
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
plt.legend(bbox_to_anchor=(0.1, 1.02, 0.8, 1.02), loc=3, ncol=3, mode="expand", borderaxespad=0., prop={'size': 16}, frameon=False)
#plt.xlim([2.7,768])
#plt.ylim([0,40])

plt.tight_layout()

plt.figure(figsize=(8,3))
plt.ylabel("FCT Slow Down", fontsize=17)
plt.xlabel("Flow Size (KB)", fontsize=17)
plt.xscale('log')
Flow_Size = [3,12, 48, 192, 768, 3072, 12288, 49152]
SlowDown = [5.0679533476478626, 4.8673863636363635, 4.7528846153846152, 4.465740740740741, 5.0160206718346254, 24.811237494044782, 60.934214531498149, 68.629657063070425]
plt.plot(Flow_Size, SlowDown, '-.', color='green', label='Google')

Flow_Size = [3,12, 48, 192, 768, 3072, 12288, 49152]
SlowDown = [4.0754767157828384, 4.1184090909090907, 4.0392123287671229, 4.1585435779816518, 4.5022842639593907, 13.12682423323222, 34.625180406735183, 0.0]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='Facebook_Hadoop')

Flow_Size = [3,12, 48, 192, 768, 3072, 12288, 49152]
SlowDown = [3.0892857142857144, 3.1802570093457945, 3.4708661417322832, 3.9580357142857143, 4.8520312499999996, 7.6835181721004808, 17.427703790238837, 18.302935710605727]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='WebSearch')
plt.xlim([2.7,760])
plt.ylim([1,6])
ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(0.0, 1.02, 0.9, 1.02), loc=3, ncol=3, mode="expand", borderaxespad=0., prop={'size': 16}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(8,3))
plt.ylabel("CDF", fontsize=17)
plt.xlabel("Measured Buffer Occupancy (MB)", fontsize=17)
plt.ylim([0,1.03])
#plt.xscale('log')
Buffer_Size = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1020,1020,2040,3060,4579,6447,8492,10660,13157,15551,18360,21428,24732,28102,31346,34542,38137,42214,46437,50648,54745,59229,64078,69345,74421,79608,85271,91708,98860,106279,113787,121354,129308,138137,147634,157417,167646,178096,187347,197125,209047,222528,237714,256602,290282,502044]
CDF = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/(1e6), CDF, '-.', color='green', label='10 Gbps')

Buffer_Size = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,126,1020,2040,4080,6120,8960,12101,15818,19807,24399,29234,34176,39208,44320,50029,55959,61576,67368,73181,79510,86496,92852,99705,106567,113333,120159,127354,134903,142813,151464,160138,169576,180040,190868,203754,217026,231495,247197,265592,286041,309678,337362,370209,408913,460634,542463,707592,1513594]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/(1e6), CDF, '-', color='blue', label='40 Gbps')

Buffer_Size = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,515,1217,3060,5100,8323,12437,17230,22440,29009,35748,43767,51971,60892,70655,81380,91903,103279,114978,127683,140867,154676,169666,185912,203164,221731,241553,261571,283083,307757,333759,362813,395514,430550,472703,519740,573112,633354,707725,787401,882298,997940,1117107,1261881,1419579,1591004,1809719,2109583,4009349]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/1e6, CDF, '--', color='red', label='100 Gbps')
ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(0.1, 1.02, 0.8, 1.02), loc=3, ncol=3, mode="expand", borderaxespad=0., prop={'size': 16}, frameon=False)
plt.tight_layout()

plt.show()