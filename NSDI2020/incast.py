import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess



plt.figure(figsize=(8,3))
plt.ylabel("Physical Queue\nSize(KB)", fontsize=17)
plt.xlabel("Concurrent flows", fontsize=17)
#plt.ylim([0,270])
#plt.xscale('log')
ax = plt.axes()
Incast = [4, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240]
Buffer_Size_90 = [83640,342720,698700,937380,1140360,1309680,1499400,1540200,1663620,1646280,1661580,1709520,1755420,1695240,1723800,1716660]
Buffer_Size_95 = [85680,358020,711960,956760,1186260,1348440,1533060,1589160,1715640,1695240,1711560,1747260,1785000,1738080,1794180,1769700]
Buffer_Size_99 = [93840,366180,722160,1003680,1249500,1409640,1605480,1670760,1795200,1758480,1803360,1816620,1885980,1826820,1902300,1836000]
Buffer_Size_90=np.array(Buffer_Size_90)/1e3
Buffer_Size_95=np.array(Buffer_Size_95)/1e3
Buffer_Size_99=np.array(Buffer_Size_99)/1e3
for i in range(len(Incast)):
	divide = 32
	if Incast[i]<=32:
		divide = Incast[i]
	Buffer_Size_90[i] = Buffer_Size_90[i]/divide
	Buffer_Size_95[i] = Buffer_Size_95[i]/divide
	Buffer_Size_99[i] = Buffer_Size_99[i]/divide
Buffer_Size_90 = (Buffer_Size_95)-Buffer_Size_90
Buffer_Size_99 = Buffer_Size_99 - Buffer_Size_95
ax.errorbar(Incast, Buffer_Size_95, yerr=[1*Buffer_Size_90, 1*Buffer_Size_99], linestyle='-', color='blue', marker='s',label='BFC')

	
Incast = [4, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240]
Buffer_Size_90 = [83640,324360,700740,1279080,1803360,2399040,2984520,3552660,4121820,4658340,5276460,5809920,6412740,6706500,7224660,7528620]
Buffer_Size_95 = [86700,343740,718080,1311720,1840080,2425560,3010020,3581220,4148340,4684860,5316240,5837460,6437220,6739140,7256280,7571460]
Buffer_Size_99 = [93840,354960,730320,1335180,1891080,2451060,3045720,3619980,4194240,4722600,5356020,5876220,6469860,6779940,7290960,7630620]
Buffer_Size_90=np.array(Buffer_Size_90)/1e3
Buffer_Size_95=np.array(Buffer_Size_95)/1e3
Buffer_Size_99=np.array(Buffer_Size_99)/1e3
for i in range(len(Incast)):
	divide = 32
	if Incast[i]<=32:
		divide = Incast[i]
	Buffer_Size_90[i] = Buffer_Size_90[i]/divide
	Buffer_Size_95[i] = Buffer_Size_95[i]/divide
	Buffer_Size_99[i] = Buffer_Size_99[i]/divide
Buffer_Size_90 = (Buffer_Size_95)-Buffer_Size_90
Buffer_Size_99 = Buffer_Size_99 - Buffer_Size_95
ax.errorbar(Incast, Buffer_Size_95, yerr=[1*Buffer_Size_90, 1*Buffer_Size_99], linestyle='--', color='red', marker='x',label='BFC-BufferOpt')
plt.axhline(y=50,linestyle='--',color='black',label='2 Hop BDP')
plt.ylim([0,250])
plt.xlim([0,250])

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(0.05, 0.97, 0.9, 0.97), loc=3, ncol=3, mode="expand", borderaxespad=0., prop={'size': 16}, frameon=False)
plt.tight_layout()

plt.show()