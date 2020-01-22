import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter

fig, (ax1,ax2)=plt.subplots(1,2,sharey=True,figsize=(8,3))#,gridspec_kw={'hspace':0.1,'wspace':0.1})
ax1.set_ylabel("FCT SlowDown", fontsize=17)
fig.text(0.5,0.05, "FlowSize (KB)", ha="center",fontsize=17)
ax1.set_ylim([1,340])
ax1.set_xscale('log')
ax2.set_xscale('log')
ax1.set_yscale('log')
fig.text(0.42,0.3, "BFC", ha="center",fontsize=17)
fig.text(0.9,0.3, "HPCC", ha="center",fontsize=17)

size = [3,12,48,192,768,3072, 12288]
SlowDown = [1.8424982431482784, 1.9661697247706422, 3.7758333333333334, 5.3842857142857143, 7.3458607456140355, 8.3863170640834568, 7.790475040666938]
ax1.plot(size,SlowDown, '-.', color='green', label='50')

SlowDown = [2.6639103917429039, 2.8108644859813086, 5.0054999999999996, 7.0892086330935253, 9.2720367847411449, 10.58001956652619, 10.44185645724258]
ax1.plot(size,SlowDown, '-', color='blue', label='60')

SlowDown = [4.5190052765292164, 4.6032710280373834, 9.1516544117647065, 12.57147766323024, 17.144822888283379, 17.55893743793446, 15.99210373383699]
ax1.plot(size,SlowDown, '--', color='red', label='70')

SlowDown = [11.435844083114475, 11.528440366972477, 23.099834437086091, 31.150303398058252, 39.21541385135135, 36.728461918892187, 29.164477118496606]
ax1.plot(size,SlowDown, ':', color='black', label='80')

SlowDown = [33.384167424032874, 33.337037037037035, 75.210099337748346, 104.43815789473685, 131.22907348242811, 106.96746449559255, 71.003528005464474]
ax1.plot(size,SlowDown, '-.', color='brown', label='90')
for tick in ax1.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax1.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax2.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax2.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)

handles, labels = ax1.get_legend_handles_labels()
plt.figlegend(handles, labels, loc='upper center', ncol=5, labelspacing=0.0, fontsize=16, frameon=False)

SlowDown = [2.4458735886392735, 2.5472477064220183, 3.0235927152317883, 3.7469262295081966, 11.695949074074074, 26.036448598130843, 23.215639108352143]
ax2.plot(size,SlowDown, '-.', color='green', label='50')

SlowDown = [2.6677878752114559, 2.7778669724770642, 3.2875919117647059, 4.2464100346020759, 17.995683661645423, 41.472025371828522, 42.00660985304745]
ax2.plot(size,SlowDown, '-', color='blue', label='60')

SlowDown = [2.9876190476190478, 3.044626168224299, 3.6235833333333334, 4.8223066298342543, 37.416561251664447, 79.621779247910865, 85.53881196847126]
ax2.plot(size,SlowDown, '--', color='red', label='70')

SlowDown = [3.408089531194924, 3.3486238532110093, 3.9004340277777776, 5.6865310077519382, 75.674832521315466, 146.18906976744185, 146.97642744038748]
ax2.plot(size,SlowDown, ':', color='black', label='80')

SlowDown = [3.9855573556723436, 3.984009009009009, 4.3478535353535355, 7.6079896907216495, 142.82244121715075, 232.74816655243316, 220.33611427757197]
ax2.plot(size,SlowDown, '-.', color='brown', label='90')

fig.tight_layout(rect=[0.0,0.1,1,0.9])


plt.figure(figsize=(5,3))
plt.ylabel("Long Median FCT \nSlow Down (%)", fontsize=17)
plt.xlabel("Load (%)", fontsize=17)
plt.yscale('log')
Speed = [50,60,70,80,90]

#SlowDown = [3.13,3.91,5.19,7.41,13.64]
SlowDown = [2.9, 3.56, 4.68, 6.3, 9.7]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-', color='blue', label='BFC.Destq16', marker='o')

#SlowDown = [6.82,11.99,31.6,67.14,102.93]
SlowDown = [5.56, 9.68, 30.07, 71.17, 113.54]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-.', color='green', label='HPCC', marker='s')

#SlowDown = [3.12,4.03,5.73,8.81,16.81]
SlowDown = [2.86, 3.52, 4.77, 6.75, 11.45]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, ':', color='black', label='IDEAL FQ', marker='^')

SlowDown = [4.03,5.14,7.12,10.3,19.17]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='orange', label='DCTCP', marker='x')

SlowDown = [2.9,3.6, 4.78, 6.99, 12.45]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='brown', label='BFC.Flowq32', marker='<')
ax = plt.axes()
ax.xaxis.set_ticks(Speed)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_minor_ticks():
	tick.label.set_fontsize(14)
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(-0.3, 0.94, 1.3, 0.94), loc=3, ncol=3, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()


plt.figure(figsize=(5,3))
plt.ylabel("Small 99pct FCT \nSlow Down (%)", fontsize=17)
plt.xlabel("Load (%)", fontsize=17)
plt.yscale('log')
Speed = [50,60,70,80,90]

#SlowDown = [3.13,3.91,5.19,7.41,13.64]
SlowDown = [1.84, 2.66, 4.5, 11.43, 33.38]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-', color='blue', label='BFC.Destq16', marker='o')

#SlowDown = [6.82,11.99,31.6,67.14,102.93]
SlowDown = [2.44, 2.66, 2.98, 3.4, 3.98]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-.', color='green', label='HPCC', marker='s')

#SlowDown = [3.12,4.03,5.73,8.81,16.81]
SlowDown = [2.38, 4.25, 9.41, 24.96, 81.79]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, ':', color='black', label='IDEAL FQ', marker='^')

SlowDown = [3.1,3.44,3.94, 4.56, 5.63]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='orange', label='DCTCP', marker='x')

SlowDown = [1.11, 1.14, 1.2, 1.32, 7.048]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='brown', label='BFC.Flowq32', marker='<')

ax = plt.axes()
ax.xaxis.set_ticks(Speed)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_minor_ticks():
	tick.label.set_fontsize(14)
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(-0.3, 0.94, 1.3, 0.94), loc=3, ncol=3, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(5,3))
plt.ylabel("Avg Collisions (%)", fontsize=17)
plt.xlabel("Load (%)", fontsize=17)
Speed = [50,60,70,80,90]

SlowDown = [0.0007,0.1,2.3, 14, 27.4]
SlowDown = [0.,0.01, 0.14, 1.25, 6.92]#BFC_2
SlowDown = [0.04,0.19, 0.77, 2.56, 7.53]#BFC_3 ($NF-$7)/$NF
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-', color='blue', marker='o')

ax = plt.axes()
ax.xaxis.set_ticks(Speed)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_minor_ticks():
	tick.label.set_fontsize(14)
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
#plt.legend(bbox_to_anchor=(0.16, 0.8, 1.0, 0.8), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 16}, frameon=False)
plt.tight_layout()



plt.show()