import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess



plt.figure(figsize=(6,3))
plt.ylabel("Utilization", fontsize=15)
Incast = [10,20,40,100,200,400,800]
Incast = np.array(Incast)
plt.xscale('log')
plt.xlim([8,1000])
#Agg=[1459502.0,1461159,1462375,1466288,1465773,1467089,1466545, 1463666,1439223, 608970, 330867, 273241]

Agg=[1469733.0, 1465114, 1465819, 1467674, 1440750, 1412997, 1373677]

Agg=np.array(Agg)
plt.ylim([0,1])
for i in range (len(Incast)):
	if i == len(Incast)-1:
		Agg[i] += 100*0.25*Incast[i]
	else:
		Agg[i] += 100*Incast[i]
	Agg[i] *= ((20.0*8*1000)/(4.8*50.0*1e6))
	print(Agg[i])
	Agg[i] *= 1e-3
plt.xlabel("Fan In", fontsize=15)

plt.plot(Incast, Agg, linestyle='-', marker='o', color='blue', label='BFC')
Agg=[2798726.0,2772566,2659031,2348775,2036459,1948512, 1944721]
#Agg=[2804303.0,2766305, 2614609, 2203338, 1654242, 1489104, 1422189]	
Agg=np.array(Agg)
for i in range (len(Incast)):
	if i == len(Incast)-1:
		Agg[i] += 100*0.5*Incast[i]
	else:
		Agg[i] += 100*Incast[i]
	Agg[i] *= ((10.0*8*1000)/(4.8*50.0*1e6))
	print(Agg[i])
	Agg[i] *= 1e-3
plt.plot(Incast, Agg, linestyle='-', marker='x', color='red', label='DCQCN + Win')

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(12)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(12)
plt.legend(bbox_to_anchor=(0.01, 0.97, 0.99, 0.97), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)
plt.tight_layout()


plt.figure(figsize=(6,3))
plt.ylabel("Incast Time (ms)", fontsize=15)
plt.xscale('log')
plt.ylim([0,6.5])
plt.xlim([8,1000])

FCT_slowdown=[23.466494293865907,35.236378059836809, 64.411815920398013, 121.26914191419142, 199.40104679802957, 258.50114379084965, 259.21152343749998]
plt.xlabel("Fan In", fontsize=15)
for i in range(len(Incast)):
	FCT_slowdown[i] = FCT_slowdown[i]*(0.004 + (1.6/Incast[i]))
plt.plot(Incast, FCT_slowdown, linestyle='-', marker='o', color='blue', label='BFC')
FCT_slowdown=[34.026569186875889, 55.874456029011789,83.689821724709788,178.86051980198019,189.72592364532019, 220.50457920792078, 269.85390625000002]
for i in range(len(Incast)):
	FCT_slowdown[i] = FCT_slowdown[i]*(0.004 + (1.6/Incast[i]))
plt.plot(Incast, FCT_slowdown, linestyle='-', marker='x', color='red', label='DCQCN + Win')


ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(12)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(12)
plt.legend(bbox_to_anchor=(0.01, 0.97, 0.99, 0.97), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)
plt.tight_layout()


plt.figure(figsize=(6,3))
plt.ylim([0,8.5])
plt.xlim([8,1000])

plt.ylabel("Buffer Occupancy (MB)", fontsize=15)
plt.xscale('log')
plt.xlabel("Fan In", fontsize=15)

Buffer=np.array([1523880.0, 1851300, 2464320, 3770940, 5425380, 6471900, 6159780])
plt.plot(Incast, Buffer/1e6, linestyle='-', marker='o', color='blue', label='BFC')

Buffer=np.array([1249500, 1968600, 2918220, 6714660,8046780, 8136540, 8253840])
plt.plot(Incast, Buffer/1e6, linestyle='-', marker='x', color='red', label='DCQCN + Win')


ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(12)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(12)
plt.legend(bbox_to_anchor=(0.01, 0.97, 0.99, 0.97), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)
plt.tight_layout()

plt.show()

