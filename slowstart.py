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
SlowDown = [9.431223180189757, 11.410630841121495, 37.67939189189189, 42.98262614678899, 37.55050623052959, 16.928660669665167, 11.916141836464673]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='BFC + FQ')

SlowDown = [1.0452472559665638, 1.069954128440367, 1.6386363636363637, 2.4962409420289857, 34.69265129682997, 13.805351394849785, 12.70157242148618]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='BFC + SRF')

SlowDown = [1.0451190476190477, 1.0628472222222223, 1.3683333333333334, 1.8876146788990826, 31.232734375, 12.139696351416227, 11.818746440098728]
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
SlowDown = [1.1479761904761905, 1.7425438596491227, 4.078298611111111, 6.254166666666666, 9.43569587628866, 10.530746336996337, 9.637086563307493]
plt.plot(Flow_Size, SlowDown, '-', color='blue')#, label='BFC')

SlowDown = [1.0437199400772688, 1.0642361111111112, 1.5926666666666667, 2.2704761904761903, 3.3337470794392523, 5.8310760053026955, 11.53074839055794]
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
SlowDown = [9.431223180189757, 11.410630841121495, 37.67939189189189, 42.98262614678899, 37.55050623052959, 16.928660669665167, 11.916141836464673]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='BFC + FQ')

SlowDown = [85.374285714285719, 77.400877192982449, 60.229051724137932, 56.950907821229052, 62.861604361370716, 36.228673861620344, 25.960575391964724]
plt.plot(Flow_Size, SlowDown, '--', color='orange', label='DCTCP')

SlowDown = [3.4556002414988507, 4.5433486238532108, 18.849751655629138, 36.950067567567565, 42.387974051896208, 20.24007723304231, 13.972763012690821]
plt.plot(Flow_Size, SlowDown, '-.', color='red')#, label='BFC + SFF')
ax = plt.axes()
ax.get_yaxis().set_ticks([1,2,4,8,16,32,64,128], minor=True)
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
SlowDown = [1.1479761904761905, 1.7425438596491227, 4.078298611111111, 6.254166666666666, 9.43569587628866, 10.530746336996337, 9.637086563307493]
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



plt.figure(figsize=(4,3))
plt.ylabel("CDF", fontsize=16)
plt.xlabel("# of active flows at a port", fontsize=16)
plt.ylim([0.8,1.03])
plt.xlim([0,200])

CDF = [0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Buffer_Size = [9,9,9,10,10,10,11,11,12,12,13,14,15,15,17,18,20,24,36,85,715]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size, CDF, '--', color='red', label='With-Incast')

Buffer_Size = [2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,6,6,7,9,36]
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
