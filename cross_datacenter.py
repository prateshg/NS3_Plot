import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter


plt.figure(figsize=(4,3))
plt.ylabel("FCT Slow Down", fontsize=16)
plt.xlabel("Flow Size (KB)", fontsize=16)
plt.xscale('log')
plt.yscale('log')
plt.gca().set_ylim(bottom=1)

Flow_Size = [3,12,48,192,768,3072,12288]
SlowDown = [2.0925860994234067, 2.3875, 4.092030201342282, 5.871381578947369, 8.250862068965517, 9.078923551959114, 8.74932689980639]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='BFC')

SlowDown = [7.380878532935292, 6.014189189189189, 7.2712121212121215, 7.229960317460318, 21.940391969407266, 31.93050296532847, 31.83663692558899]
plt.plot(Flow_Size, SlowDown,  '-.', color='green', label='HPCC')

SlowDown = [6.245842788950622, 5.750462962962963, 5.5054227941176475, 5.077696078431373, 5.5725527108433734, 11.710488041370395, 30.880978099480327]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='DCQCN')

ax = plt.axes()
ax.get_yaxis().set_ticks([2,4,8,16,32,64], minor=True)
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
plt.legend(handlelength=1.5,bbox_to_anchor=(-0.3, 1.02, 1.3, 1.02), loc=3, ncol=3, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()


fig, ax = plt.subplots(figsize=(4,3))
labels = ['BFC', 'HPCC', 'DCQCN']
#plt.yscale('log')
plt.xlim([-0.5,2.5])
ToR_spine = [99.0, 69.8, 21.4]#, 183]

x = np.arange(len(labels))  # the label locations
width = 0.4  # the width of the bars

#rects2 = ax.bar(x - width, spine_Tor, width, label='Avg', hatch='\\\\')
#rects3 = ax.bar(x, ninrty_five, width, label='95 pct', hatch='-')
rects1 = ax.bar(x, ToR_spine, width)#, label='99 pct', hatch='//')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Utilization (%)', fontsize=16 )
#ax.set_title('Scores by group and gender')
ax.get_yaxis().set_ticks([20, 40,60,80,100], minor=True)
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
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=30)
#ax.legend(bbox_to_anchor=(-0.2, 0.97, 1.2, 0.97), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)

fig.tight_layout()

plt.show()