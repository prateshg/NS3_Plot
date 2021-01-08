import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter


plt.figure(figsize=(5,2))
plt.ylabel("CDF", fontsize=16)
plt.xlabel("# of active flows at a port", fontsize=16)
plt.ylim([0.8,1.03])
plt.xlim([0,40])

CDF = [0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Buffer_Size = [2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,5,6,6,7,8,13]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '--', color='red', label='50')

Buffer_Size = [4,4,4,4,5,5,5,5,6,6,7,7,7,8,9,9,10,10,11,13,23]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='blue', label='60')

Buffer_Size = [7,7,7,8,8,8,8,9,9,9,10,10,10,11,11,11,12,12,13,15,24]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='green', label='70')

Buffer_Size = [10,10,10,10,11,11,11,11,12,12,12,13,13,13,14,14,15,16,17,18,26]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='brown', label='80')

Buffer_Size = [13,13,13,14,14,14,15,15,16,16,16,17,17,18,19,19,20,21,23,25,36]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='magenta', label='90')

Buffer_Size = [15,15,16,16,16,17,17,17,18,18,19,19,20,20,21,22,23,24,25,27,40]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='orange', label='95')

plt.axvline(x=30, color='black',linewidth=1.0)

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(handlelength=1.5,bbox_to_anchor=(-0.2, 1.02, 1.2, 1.02), loc=3, ncol=6, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(5,2))
plt.ylabel("CDF", fontsize=14)
plt.xlabel("# of active flows at a port", fontsize=14)
plt.ylim([0.8,1.02])
plt.xlim([0,28])

CDF = [0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Buffer_Size = [2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,5,9]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-', color='red', label='50')

Buffer_Size = [2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,5,5,6,11]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='blue', label='60')

Buffer_Size = [3,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,6,6,6,7,10]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, ':', color='green', label='70')

Buffer_Size = [4,5,5,5,5,5,5,5,6,6,6,6,6,6,7,7,7,8,8,9,13]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '--', color='brown', label='80')

Buffer_Size = [8,8,8,8,8,8,9,9,9,9,9,10,10,10,10,11,11,12,13,15,21]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-', color='magenta', label='90')

Buffer_Size = [11,12,12,12,12,13,13,13,14,14,14,14,15,15,16,16,17,17,18,20,27]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='orange', label='95')

#plt.axvline(x=30, color='black',linewidth=1.0)

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(handlelength=1.5,bbox_to_anchor=(-0.2, 1.02, 1.2, 1.02), loc=3, ncol=6, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()


plt.figure(figsize=(5,2))
plt.ylabel("CDF", fontsize=14)
plt.xlabel("# of active flows at a port", fontsize=14)
plt.ylim([0.8,1.02])
plt.xlim([0,28])

CDF = [0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Buffer_Size = [2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,5,8]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-', color='red', label='50')

Buffer_Size = [2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,5,5,6,10]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='blue', label='60')

Buffer_Size = [3,3,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,6,6,7,9]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, ':', color='green', label='70')

Buffer_Size = [4,4,4,4,5,5,5,5,5,5,5,6,6,6,6,7,7,7,8,8,13]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '--', color='brown', label='80')

Buffer_Size = [7,7,7,7,7,7,8,8,8,8,8,8,9,9,9,10,10,10,11,12,19]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-', color='magenta', label='90')

Buffer_Size = [10,10,10,10,11,11,11,11,12,12,12,13,13,13,14,14,15,15,16,18,23]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='orange', label='95')

#plt.axvline(x=30, color='black',linewidth=1.0)

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(handlelength=1.5,bbox_to_anchor=(-0.2, 1.02, 1.2, 1.02), loc=3, ncol=6, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(5,3))
plt.ylabel("CDF", fontsize=14)
plt.xlabel("# of active flows at a port", fontsize=14)
plt.ylim([0.8,1.02])
plt.xlim([0,1000])

CDF = [0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Buffer_Size = [511,523,534,546,559,571,587,604,623,642,663,684,707,727,742,757,774,792,815,860,993]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-', color='red', label='Single Queue (No CC, window cap)')

Buffer_Size = [28,30,32,35,39,44,49,54,60,66,73,82,92,106,121,136,156,177,199,225,288]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='blue', label='BFC (FQ)')



#plt.axvline(x=30, color='black',linewidth=1.0)

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(handlelength=1.5,bbox_to_anchor=(-0.2, 1.02, 1.2, 1.02), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()

plt.show()