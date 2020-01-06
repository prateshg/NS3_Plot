import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess



plt.figure(figsize=(6,4))
plt.ylabel("Throughput (Tbps)", fontsize=19)
Incast = [10,20,40,100,200,400,800]
Incast = np.array(Incast)
plt.xscale('log')

#Agg=[1459502.0,1461159,1462375,1466288,1465773,1467089,1466545, 1463666,1439223, 608970, 330867, 273241]
Agg=[4.8,4.8,4.8,4.8,4.8,4.8,4.8]
plt.plot(Incast, Agg, linestyle='--', color='black', label='Capacity')

Agg=[2939320.0, 2930075, 2931453, 2935089, 2882998, 2781313, 2664503]

Agg=np.array(Agg)
plt.ylim([0,5])
for i in range (len(Incast)):
	if i == len(Incast)-1:
		Agg[i] += 100*0.5*Incast[i]
	else:
		Agg[i] += 100*Incast[i]
	Agg[i] *= ((10.0*8*1000)/(50.0*1e6))
	print(Agg[i])
	Agg[i] *= 1e-3
plt.xlabel("Fan In", fontsize=19)

plt.plot(Incast, Agg, linestyle='-', marker='o', color='blue', label='BFC')
Agg=[2798726.0,2772566,2659031,2348775,2036459,1948512, 1944721]
#Agg=[2804303.0,2766305, 2614609, 2203338, 1654242, 1489104, 1422189]	
Agg=np.array(Agg)
for i in range (len(Incast)):
	if i == len(Incast)-1:
		Agg[i] += 100*0.5*Incast[i]
	else:
		Agg[i] += 100*Incast[i]
	Agg[i] *= ((10.0*8*1000)/(50.0*1e6))
	print(Agg[i])
	Agg[i] *= 1e-3
plt.plot(Incast, Agg, linestyle='-', marker='x', color='red', label='DCQCN + Win')

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(16)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(16)
plt.legend(bbox_to_anchor=(0.01, 0.97, 0.99, 0.97), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 18}, frameon=False)
plt.tight_layout()


plt.figure(figsize=(6,4))
plt.ylabel("FCT Slow Down", fontsize=19)
plt.xscale('log')

IDEAL = []
for i in range(len(Incast)):
	IDEAL.append(1.6004/((0.004) + (1.6004/(4+Incast[i]))))
#plt.plot(Incast, IDEAL, linestyle='--', color='black', label='Ideal*')
FCT_slowdown=[23.639847836424156, 36.527176498572786, 64.411815920398013, 121.26914191419142, 198.09125615763546, 266.50866013071897, 259.48876953125]
plt.xlabel("Fan In", fontsize=19)

plt.plot(Incast, FCT_slowdown, linestyle='-', marker='o', color='blue', label='BFC')
FCT_slowdown=[34.026569186875889, 55.874456029011789,83.689821724709788,178.86051980198019,189.72592364532019, 220.50457920792078, 269.85390625000002]
#FCT_slowdown=[33.869828815977172, 54.254975067996376, 83.462126865671635, 179.40895214521453, 221.50240147783251, 260.89648692810459, 278.03338815789476]
plt.plot(Incast, FCT_slowdown, linestyle='-', marker='x', color='red', label='DCQCN + Win')


ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(16)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(16)
plt.legend(bbox_to_anchor=(0.01, 0.97, 0.99, 0.97), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 18}, frameon=False)
plt.tight_layout()

plt.show()