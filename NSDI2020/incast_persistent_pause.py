import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess



plt.figure(figsize=(6,4))
plt.ylabel("Throughput (Tbps)", fontsize=19)
Incast = [0,2,4,6,8,10,12,14,16,18,20,22]
Incast = np.array(Incast)
Agg=[4.8,4.8,4.8,4.8,4.8,4.8,4.8,4.8,4.8,4.8,4.8,4.8]

plt.plot(Incast*10, Agg, linestyle='--', color='black', label='Capacity')
#Agg=[1459502.0,1461159,1462375,1466288,1465773,1467089,1466545, 1463666,1439223, 608970, 330867, 273241]
Agg=[729745.0, 730413, 731749,733005, 734407, 733550, 733505, 735047, 721287, 116093, 108753, 96940]

Agg=np.array(Agg)
plt.ylim([0,5])
for i in range (len(Incast)):
	Agg[i] += Incast[i]*10*50
	print(Agg[i])
	Agg[i] *= ((20.0*8*1000)/(25.0*1e6))
	print(Agg[i])
	Agg[i] *= 1e-3
plt.xlabel("Incast Degree", fontsize=19)

plt.plot(Incast*10, Agg, linestyle='-', marker='o', color='blue', label='BFC')

Agg=[144489.0, 141843, 133836, 129163, 118658, 109539, 91321, 81471, 72059, 63311, 58581, 53986]	
#50msAgg=[287326.0, 280254 ,265047, 255992, 242923 ,229349,197557,178151, 159525, 149956, 137898, 131176]
Agg=np.array(Agg)
for i in range (len(Incast)):
	Agg[i] += Incast[i]*10*50
	Agg[i] *= ((100.0*8*1000)/(25.0*1e6))
	Agg[i] *= 1e-3
plt.plot(Incast*10, Agg, linestyle='-', marker='x', color='red', label='DCQCN + Win')

Agg=[729745.0, 730413, 731749, 733005, 734407,733761,732414,730395,679850,573828,445675,389162]

Agg=np.array(Agg)
plt.ylim([0,5])
for i in range (len(Incast)):
	Agg[i] += Incast[i]*10*50
	print(Agg[i])
	Agg[i] *= ((20.0*8*1000)/(25.0*1e6))
	print(Agg[i])
	Agg[i] *= 1e-3
plt.xlabel("Incast Degree", fontsize=19)

plt.plot(Incast*10, Agg, linestyle='-', marker='s', color='lightblue', label='BFC+PFC')

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(16)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(16)
plt.legend(bbox_to_anchor=(0.05, 0.97, 0.9, 0.97), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 18}, frameon=False)
plt.tight_layout()


plt.figure(figsize=(6,4))
plt.ylabel("FCT Slow Down", fontsize=19)
Incast = [0, 2,4,6,8,10,12,14,16,18,20,22]
Incast = np.array(Incast)

plt.plot(Incast*10, Incast*10+4, linestyle='--', color='black', label='Ideal*')
Incast = [2,4,6,8,10,12,14,16,18,20,22]
Incast = np.array(Incast)
FCT_slowdown=[19.789193227091634, 37.785806772908366, 62.66060231023102, 98.39368811881188, 122.67681518151815, 158.61592409240924, 184.56707920792078, 217.10214521452144, 542.65502988047808,413.21344621513947,553.65567729083671]
plt.xlabel("Incast Degree", fontsize=19)

plt.plot(Incast*10, FCT_slowdown[:len(Incast)], linestyle='-', marker='o', color='blue', label='BFC')

FCT_slowdown=[19.940057755775577, 47.912665016501649, 92.845173267326729, 156.81171617161715, 179.73139438943895, 286.21382013201321, 293.85544554455447, 436, 429, 376,415]
plt.plot(Incast*10, FCT_slowdown[:len(Incast)], linestyle='-', marker='x', color='red', label='DCQCN + Win')


FCT_slowdown=[19.796065737051794, 40.614768976897693, 72.87669141914192, 74.117533003300323, 123.09232673267327, 166.14262948207173, 178.25775577557755, 217.89327557755774, 276.74636963696372, 265.62751650165018, 379.50251650165018]
plt.plot(Incast*10, FCT_slowdown[:len(Incast)], linestyle='-', marker='s', color='lightblue', label='BFC+PFC')


ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(16)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(16)
plt.legend(bbox_to_anchor=(0.05, 0.97, 0.9, 0.97), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 18}, frameon=False)
plt.tight_layout()

plt.show()