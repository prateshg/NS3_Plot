import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter

plt.figure(figsize=(4,2.6))
plt.ylabel("FCT Slow Down", fontsize=16)
plt.xlabel("Flow Size (KB)", fontsize=16)
plt.xscale('log')
plt.yscale('log')

Flow_Size = [3,12,48,192,768,3072,12288]
SlowDown = [3.8660902902746264, 12.101914414414415, 25.73079044117647, 38.46059160305344, 35.874466463414635, 19.80738245412844, 12.591385135135136]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='BFC + FQ')

SlowDown = [1.0452472559665638, 1.069954128440367, 1.6386363636363637, 2.4962409420289857, 34.69265129682997, 13.805351394849785, 12.70157242148618]
SlowDown = [1.04, 1.2, 2.5, 4.5, 34.7, 15.6, 13.3]#markup 1.5
#SlowDown = [1.04, 1.1, 2.8, 3.8, 35.5, 13.8, 12.9]#markup 3
plt.plot(Flow_Size, SlowDown, '--', color='red', label='BFC + SRF')

SlowDown = [1.0451190476190477, 1.0628472222222223, 1.3883333333333334, 1.976146788990826, 31.232734375, 12.139696351416227, 11.818746440098728]
plt.plot(Flow_Size, SlowDown,  ':', color='black')#, label='Ideal-')


plt.axvline(x=200, color='black', linestyle='-', linewidth=1.0)
ax = plt.axes()
ax.get_yaxis().set_ticks([1,2,4,8,16,32,64], minor=True)
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
plt.legend(handlelength=1.5,bbox_to_anchor=(-0.1, 1.02, 1.1, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()


plt.figure(figsize=(4,2.6))
plt.ylabel("FCT Slow Down", fontsize=16)
plt.xlabel("Flow Size (KB)", fontsize=16)
plt.xscale('log')
plt.yscale('log')

Flow_Size = [3,12,48,192,768,3072,12288]
SlowDown = [1.1349056603773584, 1.7268805309734514, 4.522859589041096, 6.753033088235294, 9.972690217391305, 11.647113259668508, 11.03247432306255]
plt.plot(Flow_Size, SlowDown, '-', color='blue')#, label='BFC')

SlowDown = [1.0437199400772688, 1.0642361111111112, 1.5926666666666667, 2.2704761904761903, 3.3337470794392523, 5.8310760053026955, 11.53074839055794]
#SlowDown = [1.04, 1.09, 1.8, 2.7, 4.1, 6.1, 12.3]
SlowDown = [1.04, 1.09, 1.7, 2.5, 3.7, 5.8, 12.2]
plt.plot(Flow_Size, SlowDown,  '--', color='red')#, label='HPCC')

SlowDown = [1.0445754716981133, 1.063495575221239, 1.373458904109589, 1.826541095890411, 2.6829783519553074, 5.045075187969925, 10.652255077658303]
plt.plot(Flow_Size, SlowDown, ':', color='black', label='Ideal-SRF')
ax = plt.axes()
ax.get_yaxis().set_ticks([1,2,4,8,16], minor=True)
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
plt.legend(handlelength=1.5,bbox_to_anchor=(0.25, 1.02, 0.9, 1.02), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()



plt.figure(figsize=(4,2.6))
plt.ylabel("FCT Slow Down", fontsize=16)
plt.xlabel("Flow Size (KB)", fontsize=16)
plt.xscale('log')
plt.yscale('log')

Flow_Size = [3,12,48,192,768,3072,12288]
SlowDown = [3.8660902902746264, 12.101914414414415, 25.73079044117647, 38.46059160305344, 35.874466463414635, 19.80738245412844, 12.591385135135136]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='BFC + FQ')

SlowDown = [85.374285714285719, 77.400877192982449, 60.229051724137932, 56.950907821229052, 62.861604361370716, 36.228673861620344, 25.960575391964724]
plt.plot(Flow_Size, SlowDown, '--', color='orange', label='DCTCP')

SlowDown = [3.4556002414988507, 4.5433486238532108, 18.849751655629138, 36.950067567567565, 42.387974051896208, 20.24007723304231, 13.972763012690821]
plt.plot(Flow_Size, SlowDown, '-.', color='red')#, label='BFC + SFF')
ax = plt.axes()
ax.get_yaxis().set_ticks([4,8,16,32,64, 128], minor=True)
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
plt.legend(handlelength=1.5,bbox_to_anchor=(-0.1, 1.02, 1.1, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()


plt.figure(figsize=(4,2.6))
plt.ylabel("FCT Slow Down", fontsize=16)
plt.xlabel("Flow Size (KB)", fontsize=16)
plt.xscale('log')
plt.yscale('log')

Flow_Size = [3,12,48,192,768,3072,12288]
SlowDown = [1.1349056603773584, 1.7268805309734514, 4.522859589041096, 6.753033088235294, 9.972690217391305, 11.647113259668508, 11.03247432306255]
plt.plot(Flow_Size, SlowDown, '-', color='blue')#, label='BFC')

SlowDown = [3.4244465738423027, 3.5284722222222222, 3.7558277027027027, 4.2114718614718614, 8.2120098039215694, 14.97517523364486, 13.071036216085272]
plt.plot(Flow_Size, SlowDown, '--', color='orange')#, label='DCTCP')

SlowDown = [2.9183782774480131, 3.6964130434782607, 8.0635906040268459, 11.124795081967212, 14.397446236559139, 15.688842226613966, 11.946356564810939]
plt.plot(Flow_Size, SlowDown, '-.', color='red', label='DCTCP+SS')
ax = plt.axes()
ax.get_yaxis().set_ticks([1,2,4,8,16], minor=True)
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
plt.legend(handlelength=1.5,bbox_to_anchor=(0.25, 1.02, 0.9, 1.02), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()


plt.figure(figsize=(4,2.6))
plt.ylabel("FCT Slow Down", fontsize=16)
plt.xlabel("Flow Size (KB)", fontsize=16)
plt.xscale('log')
plt.yscale('log')

Flow_Size = [3,12,48,192,768,3072,12288]
SlowDown = [1.0285075599068336, 1.1355140186915889, 1.680603448275862, 2.158196721311475, 2.9983839050131924, 3.6196178937558248, 3.990894568690096]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='BFC + FQ')

SlowDown = [1.149695547626435, 1.2736363636363637, 1.7758278145695365, 2.071458333333333, 2.852839116719243, 5.301854243542436, 6.892796337467821]
plt.plot(Flow_Size, SlowDown, '--', color='orange', label='DCTCP')

SlowDown = [1.0556060961771727, 1.7780133928571429, 3.3529761904761903, 3.522424892703863, 3.3312671703296703, 4.044787373548146, 4.730526473227639]
plt.plot(Flow_Size, SlowDown, '-.', color='red')#, label='BFC + SFF')
ax = plt.axes()
ax.get_yaxis().set_ticks([1, 2, 4], minor=True)
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
plt.legend(handlelength=1.5,bbox_to_anchor=(-0.1, 1.02, 1.1, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()


plt.figure(figsize=(4,2.6))
plt.ylabel("FCT Slow Down", fontsize=16)
plt.xlabel("Flow Size (KB)", fontsize=16)
plt.xscale('log')
plt.yscale('log')

Flow_Size = [3,12,48,192,768,3072,12288]
SlowDown = [1.0280952380952382, 1.137266355140187, 1.665625, 2.160693359375, 3.0083227848101264, 3.5272680412371136, 3.822440585009141]
plt.plot(Flow_Size, SlowDown, '-', color='blue')#, label='BFC')

SlowDown = [1.0574617993295392, 1.1917045454545454, 1.6344618055555555, 1.9022569444444444, 2.5425245098039215, 4.068779574132492, 5.148029533483823]
plt.plot(Flow_Size, SlowDown, '--', color='orange')#, label='DCTCP')

SlowDown = [1.0653794694795624, 1.7243303571428572, 3.1699468085106384, 3.3113372093023257, 3.219092987804878, 3.7929642857142856, 4.476324479013795]
plt.plot(Flow_Size, SlowDown, '-.', color='red', label='DCTCP+SS')
ax = plt.axes()
ax.get_yaxis().set_ticks([1, 2, 4], minor=True)
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
plt.legend(handlelength=1.5,bbox_to_anchor=(0.25, 1.02, 0.9, 1.02), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()



plt.figure(figsize=(4,3))
plt.ylabel("CDF", fontsize=16)
plt.xlabel("# of active flows at a port", fontsize=16)
plt.ylim([0.8,1.01])
plt.xlim([0,200])

CDF = [0.8, 0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Buffer_Size = [7,7,8,8,8,9,9,10,10,11,11,12,13,14,15,16,18,22,39,121,461]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '--', color='red', label='With-Incast')

Buffer_Size = [2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,5,5,6,7,8,32]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '-.', color='green', label='Without-Incast')

plt.axvline(x=30, color='black',linewidth=1.0)

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(handlelength=1.5,bbox_to_anchor=(0.11, 1.02, 1.0, 1.02), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()


plt.show()
