import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess

plt.figure(figsize=(8,4))
plt.ylabel("FCT Slow Down", fontsize=19)
plt.xlabel("Flow Size (KB)", fontsize=19)
plt.xscale('log')
plt.yscale('log')

Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown =  [1.0573281026552777, 10.42122641509434, 11.233844339622642, 11.912844036697248, 16.724673913043478, 37.022718253968257, 56.7419776119403, 41.785272828507793, 17.74737302977233]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='BFC')


Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown = [96.287620106408312, 92.103690476190479, 91.028183962264151, 89.151136363636368, 87.689618644067792, 77.868303571428569, 58.525502232142856, 36.126303680981593, 15.629069902461682]
plt.plot(Flow_Size, SlowDown, '-.', color='orange', label='SFQ+InfBuffer')

Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown = [1.0765258356240788, 135.595, 152.40082547169811, 170.74305555555554, 189.21583333333334, 201.42305389221556, 182.12931034482759, 99.945184630738524, 40.281642927308447]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='BFC-VFID')



ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(16)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(16)
plt.legend(bbox_to_anchor=(0.01, 0.97, 0.99, 0.97), loc=3, ncol=3, mode="expand", borderaxespad=0., prop={'size': 18}, frameon=False)
plt.tight_layout()


plt.figure(figsize=(4,4))
plt.ylabel("CDF", fontsize=19)
plt.xlabel("Fraction of Collisions", fontsize=19)
#plt.xscale('log')
#plt.yscale('pl
#plt.xlim([0,200])
CDF = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Collisions =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.333333,0.818182]

plt.plot(Collisions, CDF, '-', color='blue', label='BFC ')
Collisions =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.2,0.333333,0.484848,0.518519,0.571429,0.603774,0.631579,0.652174,0.666667,0.6875,0.7,0.714286,0.727273,0.736842,0.75,0.758621,0.769231,0.78,0.790698,0.8,0.814815,0.829268,0.85,0.956522]

plt.plot(Collisions, CDF, '--', color='red', label='BFC-VFID')


ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(16)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(16)
plt.legend(bbox_to_anchor=(-0.15, 0.97, 1.2, 0.97), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 18}, frameon=False)
plt.tight_layout()
plt.show()