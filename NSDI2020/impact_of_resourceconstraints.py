import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess

plt.figure(figsize=(8,4))
plt.ylabel("FCT Slow Down", fontsize=19)
plt.xlabel("Flow Size (KB)", fontsize=19)
plt.xscale('log')
plt.yscale('log')

Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown = [1.0571805869971007, 14.61404761904762, 15.468514150943395, 16.414285714285715, 22.929891304347827, 43.03186813186813, 60.918193717277489, 42.092099471830984, 17.963747810858145]
plt.plot(Flow_Size, SlowDown, '-.', color='green', label='1024')

Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown = [1.0573862296628154, 11.096666666666666, 11.953181818181818, 12.197935779816513, 18.085745614035087, 36.164156626506021, 58.654753521126757, 40.200843425605534, 17.667319749216301]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='4096')


Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown = [1.0573281026552777, 10.42122641509434, 11.233844339622642, 11.912844036697248, 16.724673913043478, 37.022718253968257, 56.7419776119403, 41.785272828507793, 17.74737302977233]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='16384')


Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown = [1.0572709163346614, 10.452500000000001, 10.971990740740742, 11.575568181818182, 16.935951327433628, 36.80885416666667, 59.022314049586775, 41.724136971046768, 17.813671190893171]
plt.plot(Flow_Size, SlowDown, linestyle=':', color='brown', label='65536')

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(16)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(16)
plt.legend(bbox_to_anchor=(0.01, 0.97, 0.99, 0.97), loc=3, ncol=4, mode="expand", borderaxespad=0., prop={'size': 18}, frameon=False)
plt.tight_layout()


fig, ax = plt.subplots(figsize=(4,4))
plt.yscale('log')
plt.ylim([0.01,2])
labels = ['1024', '4096', '16384', '65536']
collision = [1.409, 0.37, 0.08, 0.03]
overflows = [0.02, 0.0, 0.0, 0.0]
x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

rects1 = ax.bar(x - width/2, collision, width, label='Collisions')
rects2 = ax.bar(x + width/2, overflows, width, label='Overflows')
#rects2 = ax.bar(x - width/2, spine_Tor, width, label='Spine->ToR')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Fraction (%)', fontsize=19 )
ax.set_xlabel('# VFID', fontsize=19 )
#ax.set_title('Scores by group and gender')
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(15)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(15)
ax.set_xticks(x)
ax.set_xticklabels(labels)
#ax.legend(bbox_to_anchor=(-0.05, 0.97, 0.99, 0.97), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 16}, frameon=False)
ax.legend(prop={'size': 16})

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


#autolabel(rects1)
#autolabel(rects2)

fig.tight_layout()


plt.figure(figsize=(8,4))
plt.ylabel("FCT Slow Down", fontsize=19)
plt.xlabel("Flow Size (KB)", fontsize=19)
plt.xscale('log')
plt.yscale('log')

Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown = [2.0401709231443483, 3.4157142857142859, 5.4080607476635514, 9.1999999999999993, 15.622563559322034, 33.164172535211264, 60.245172413793107, 42.826310483870969, 17.316309106830122]
plt.plot(Flow_Size, SlowDown, '--', color='black', label='Ideal-FQ')


Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown = [1.0551739474204389, 104.78559523809524, 103.63925233644859, 102.25520833333333, 101.15323660714286, 118.6633064516129, 130.61707048458149, 94.369604492187506, 41.017481684981682]
plt.plot(Flow_Size, SlowDown, '-.', color='green', label='8')

Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown = [1.0562126666402945, 105.07440476190476, 104.41627358490567, 104.53497706422019, 101.07047413793103, 105.62255859375, 93.981898148148147, 58.83609068627451, 22.708320811419984]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='16')


Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown = [1.0573281026552777, 10.42122641509434, 11.233844339622642, 11.912844036697248, 16.724673913043478, 37.022718253968257, 56.7419776119403, 41.785272828507793, 17.74737302977233]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='32')


Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown = [1.0572564573482865, 2.2514150943396225, 4.4259090909090908, 6.7326834862385319, 12.840848214285714, 30.940163934426231, 59.444830508474574, 43.726311188811188, 18.067038170163169]
plt.plot(Flow_Size, SlowDown, linestyle=':', color='brown', label='64')

Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown = [1.057060346544513, 2.1819047619047618, 4.3609813084112146, 8.3583333333333325, 15.376495726495726, 33.631250000000001, 63.345531400966181, 44.118444055944053, 17.734518599562364]
plt.plot(Flow_Size, SlowDown, linestyle='-.', color='gold', label='128')

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(16)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(16)
plt.legend(bbox_to_anchor=(-0.05, 0.97, 1.05, 0.97), loc=3, ncol=6, mode="expand", borderaxespad=0., prop={'size': 17}, frameon=False)
plt.tight_layout()


fig, ax = plt.subplots(figsize=(4,4))
plt.yscale('log')
plt.ylim([0.0001,11])
labels = ['8', '16', '32', '64', '128']
collision = [9.68,5.2945, 0.601, 0.0021, 0.0001]

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

rects1 = ax.bar(x + width/2, collision, width, label='collision')
#rects2 = ax.bar(x - width/2, spine_Tor, width, label='Spine->ToR')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('% of collisions', fontsize=19 )
ax.set_xlabel('# Physical Q', fontsize=19 )
#ax.set_title('Scores by group and gender')
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(16)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(16)
ax.set_xticks(x)
ax.set_xticklabels(labels)
#ax.legend(bbox_to_anchor=(0.0, 0.97, 0.99, 0.97), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 16}, frameon=False)


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


#autolabel(rects1)
#autolabel(rects2)

fig.tight_layout()


plt.figure(figsize=(8,3))
plt.ylabel("FCT Slow Down", fontsize=17)
plt.xlabel("Flow Size (KB)", fontsize=17)
plt.xscale('log')
plt.yscale('log')

Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown = [1.0570285534985879, 15.469285714285714, 16.054398148148149, 16.002455357142857, 22.846381578947369, 41.351858108108111, 57.799450549450547, 41.662103873239438, 18.13174234135667]
plt.plot(Flow_Size, SlowDown, ':', color='brown', label='16B')

Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown = [1.0571848237402908, 10.447261904761906, 11.0, 11.323958333333334, 17.209348739495798, 35.075757575757578, 58.430961538461538, 40.20831473214286, 17.311060065825561]
plt.plot(Flow_Size, SlowDown, '-.', color='green', label='32B')

Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown = [1.0571611228234561, 10.169642857142858, 10.801363636363636, 11.895756880733945, 16.570200892857144, 34.815322580645159, 55.55124309392265, 40.473218262806235, 17.548522329246936]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='64B')


Flow_Size = [1, 2, 4, 8, 16, 64, 256, 1024, 2048]
SlowDown = [1.0573281026552777, 10.42122641509434, 11.233844339622642, 11.912844036697248, 16.724673913043478, 37.022718253968257, 56.7419776119403, 41.785272828507793, 17.74737302977233]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='128B')


ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(0.05, 0.97, 0.95, 0.97), loc=3, ncol=4, mode="expand", borderaxespad=0., prop={'size': 16}, frameon=False)
plt.tight_layout()


plt.show()