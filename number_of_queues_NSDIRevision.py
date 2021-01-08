import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter


#BFC LogNormal W3 100Gbps

plt.figure(figsize=(5,2))
plt.ylabel("CDF", fontsize=16)
plt.xlabel("# of active flows at a port", fontsize=16)
plt.ylim([0.8,1.03])
plt.xlim([1,1400])
plt.xscale('log')

CDF = [0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Buffer_Size = [2,2,2,2,3,3,3,3,3,3,3,4,4,4,5,5,5,6,7,8,23]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '--', color='red', label='50')

Buffer_Size = [3,3,3,3,4,4,4,4,4,5,5,5,5,6,6,7,7,8,9,11,30]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='blue', label='60')

Buffer_Size = [4,5,5,5,5,5,6,6,6,6,7,7,8,8,9,9,10,11,12,15,45]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='green', label='70')

Buffer_Size = [7,7,7,8,8,8,9,9,9,10,10,11,12,12,13,14,16,17,20,26,87]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='brown', label='80')

Buffer_Size = [14,14,15,15,16,17,18,19,20,21,23,26,29,33,38,45,54,66,84,115,222]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='magenta', label='90')

Buffer_Size = [25,26,28,30,32,34,37,40,44,50,56,64,73,83,96,115,138,165,192,231,382]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='orange', label='95')

plt.axvline(x=32, color='black',linewidth=1.0)

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(handlelength=1.5,bbox_to_anchor=(-0.2, 1.02, 1.2, 1.02), loc=3, ncol=6, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()


#BFC LogNormal W3 400Gbps

plt.figure(figsize=(5,2))
plt.ylabel("CDF", fontsize=16)
plt.xlabel("# of active flows at a port", fontsize=16)
plt.ylim([0.8,1.03])
plt.xlim([1,1400])
plt.xscale('log')

CDF = [0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Buffer_Size = [2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,6,7,8,20]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '--', color='red', label='50')

Buffer_Size = [3,3,3,3,3,4,4,4,4,4,5,5,5,6,6,6,7,8,9,11,26]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='blue', label='60')

Buffer_Size = [4,4,5,5,5,5,5,6,6,6,7,7,7,8,8,9,10,11,12,14,36]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='green', label='70')

Buffer_Size = [6,7,7,7,7,8,8,8,9,9,10,10,11,12,12,13,15,16,19,24,82]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='brown', label='80')

Buffer_Size = [12,13,13,14,15,15,16,17,19,20,23,26,30,37,48,63,76,93,112,144,279]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='magenta', label='90')

Buffer_Size = [25,27,29,32,35,39,44,49,55,63,72,85,99,114,135,156,176,207,249,297,477]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='orange', label='95')

plt.axvline(x=32, color='black',linewidth=1.0)

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(handlelength=1.5,bbox_to_anchor=(-0.2, 1.02, 1.2, 1.02), loc=3, ncol=6, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()


#FIFO FW 100 Lognormal W3 100Gbps

plt.figure(figsize=(5,2))
plt.ylabel("CDF", fontsize=16)
plt.xlabel("# of active flows at a port", fontsize=16)
plt.ylim([0.8,1.03])
plt.xlim([1,1400])
plt.xscale('log')

CDF = [0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Buffer_Size = [13,15,17,18,20,22,24,27,29,32,35,39,43,47,52,58,64,72,83,100,225]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '--', color='red', label='50')

Buffer_Size = [32,34,36,39,42,45,48,51,55,58,62,66,71,78,84,91,100,109,122,145,278]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='blue', label='60')

Buffer_Size = [60,63,66,69,73,77,81,86,90,95,101,108,116,124,133,143,155,169,189,223,361]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='green', label='70')

Buffer_Size = [110,114,119,124,129,135,141,148,155,162,170,179,190,201,215,230,249,274,301,351,477]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='brown', label='80')

Buffer_Size = [240,248,257,267,278,291,303,316,332,351,369,389,420,458,492,536,592,653,703,753,869]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='magenta', label='90')

Buffer_Size = [421,437,452,469,487,503,519,538,557,581,603,632,668,711,759,808,869,910,975,1079,1356]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='orange', label='95')

plt.axvline(x=32, color='black',linewidth=1.0)

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(handlelength=1.5,bbox_to_anchor=(-0.2, 1.02, 1.2, 1.02), loc=3, ncol=6, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()


#BFC SRPT Lognormal W3 100Gbps

plt.figure(figsize=(5,2))
plt.ylabel("CDF", fontsize=16)
plt.xlabel("# of active flows at a port", fontsize=16)
plt.ylim([0.8,1.03])
plt.xlim([1,1400])
plt.xscale('log')

CDF = [0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Buffer_Size = [1,1,1,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,4,4,10]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '--', color='red', label='50')

Buffer_Size = [2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,5,12]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='blue', label='60')

Buffer_Size = [2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,5,5,6,13]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='green', label='70')

Buffer_Size = [3,3,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,6,6,7,17]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='brown', label='80')

Buffer_Size = [4,4,5,5,5,5,5,5,5,5,6,6,6,6,6,7,7,7,8,9,17]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='magenta', label='90')

Buffer_Size = [5,5,6,6,6,6,6,6,6,6,7,7,7,7,8,8,8,9,9,10,17]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='orange', label='95')

plt.axvline(x=32, color='black',linewidth=1.0)

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(handlelength=1.5,bbox_to_anchor=(-0.2, 1.02, 1.2, 1.02), loc=3, ncol=6, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()

plt.show()