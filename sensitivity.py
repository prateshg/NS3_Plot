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
plt.ylabel("FCT Slow Down", fontsize=17)
plt.xlabel("Flow Size (KB)", fontsize=17)
plt.xscale('log')
plt.yscale('log')
plt.gca().set_ylim(bottom=1)

Flow_Size = [3,12,48,192,768,3072,12288]
SlowDown = [95.98691213470097, 89.23489130434783, 117.19577067669172, 127.42828947368422, 114.94518914473684, 78.68586805555556, 38.39769875579924]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='8')

SlowDown = [76.57964863797868, 78.3775462962963, 86.1424074074074, 80.87663043478261, 55.07868487928844, 24.8421875, 16.466393898221344]
plt.plot(Flow_Size, SlowDown,  '-.', color='green', label='16')

SlowDown = [9.431223180189757, 11.410630841121495, 37.67939189189189, 42.98262614678899, 37.55050623052959, 16.928660669665167, 11.916141836464673]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='32')

SlowDown = [1.9401319427984516, 6.845454545454546, 30.124662162162164, 41.778551912568304, 38.51766975308642, 15.880486425339367, 10.672056727480046]
plt.plot(Flow_Size, SlowDown, '-.', color='brown', label='64')

SlowDown = [2.03135404018644, 8.388288288288289, 33.857672413793104, 47.39002808988764, 38.82804154302671, 17.773939051918735, 11.842454712926006]
plt.plot(Flow_Size, SlowDown, '--', color='orange', label='128')

SlowDown = [1.8357190347686652, 7.93536036036036, 33.62179054054054, 46.5646408839779, 37.80108024691358, 17.576265450264863, 13.25542191992922]
plt.plot(Flow_Size, SlowDown, ':', color='black', label='IdealFQ')


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
plt.legend(bbox_to_anchor=(-0.1, 1.02, 1.1, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(4,4))
plt.yscale('log')
plt.ylim([0.1,11])
labels = ['8', '16', '32', '64', '128']
collision = [9.7,2.4, 0.47, 0.1, 0.01]

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

ax.legend(prop={'size': 16})
plt.tight_layout()

plt.figure(figsize=(5,3))
plt.ylabel("FCT SlowDown", fontsize=17)
plt.xlabel("# physical queues", fontsize=17)
#plt.ylim([1,4])
plt.xscale('log')
plt.yscale('log')
Speed = [8,16,32,64,128]
SlowDown = [3.81,1.147,1.147,1.147,1.149]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-', color='blue', marker='o', label='60%')
SlowDown = [7.66, 1.37, 1.206, 1.22, 1.206]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-.', color='green', marker='^', label='70%')
SlowDown = [12.2, 4.97, 1.3, 1.33, 1.3]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '--', color='red', marker='s', label='80%')
SlowDown = [17.52,14.09, 2.91, 1.54, 1.51]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  ':', color='orange', marker='<', label='90%')
ax = plt.gca()
ax.get_xaxis().set_ticks([8,16,32,64,128], minor=True)
ax.get_xaxis().set_ticks([], minor=False)
ax.xaxis.set_minor_formatter(mticker.ScalarFormatter())
ax.xaxis.get_minor_formatter().set_scientific(False)
ax.xaxis.set_major_formatter(mticker.ScalarFormatter())
ax.xaxis.get_major_formatter().set_scientific(False)
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.xaxis.get_minor_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)

plt.legend(bbox_to_anchor=(0.1, 1.02, 0.9, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 16}, frameon=False)
plt.tight_layout()


plt.figure(figsize=(4,3))
plt.ylabel("FCT Slow Down", fontsize=17)
plt.xlabel("Flow Size (KB)", fontsize=17)
plt.xscale('log')
plt.yscale('log')
plt.gca().set_ylim(bottom=1)

Flow_Size = [3,12,48,192,768,3072,12288]
SlowDown = [12.85617517020111, 19.31632882882883, 45.804136029411765, 51.366587452471485, 37.70831151832461, 17.217796229802513, 11.738581031976745]
plt.plot(Flow_Size, SlowDown, ':', color='orange', label='1024')

SlowDown = [10.05924402663533, 14.533695652173913, 39.39746503496504, 44.79118852459016, 37.00809270516717, 16.928526354862658, 11.954161143330571]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='2048')

SlowDown = [9.194911521747642, 12.493804347826087, 35.325760135135134, 44.15647590361446, 38.26073190789474, 16.676780646992054, 11.29956300301811 ]
plt.plot(Flow_Size, SlowDown,  '-.', color='green', label='4096')

SlowDown = [9.431223180189757, 11.410630841121495, 37.67939189189189, 42.98262614678899, 37.55050623052959, 16.928660669665167, 11.916141836464673]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='8192')

SlowDown = [8.861038249226795, 10.384747706422019, 36.29279513888889, 43.4735020661157, 37.00327932098765, 16.655703745743473, 12.280001401345292]
plt.plot(Flow_Size, SlowDown, ':', color='black', label='16384')

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
plt.legend(bbox_to_anchor=(-0.1, 1.02, 1.1, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(4,4))
plt.yscale('log')
plt.ylim([0.001,0.01])
labels = ['1024', '2048', '4096', '8192', '16384']
collision = [0.0011, 0 , 0 , 0 , 0]

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

rects1 = ax.bar(x + width/2, collision, width, label='overflows')
#rects2 = ax.bar(x - width/2, spine_Tor, width, label='Spine->ToR')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('% of overflows', fontsize=19 )
ax.set_xlabel('# Physical Q', fontsize=19 )
#ax.set_title('Scores by group and gender')
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(16)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(16)
ax.set_xticks(x)
ax.set_xticklabels(labels)

ax.legend(prop={'size': 16})
plt.tight_layout()


plt.figure(figsize=(4,3))
plt.ylabel("FCT Slow Down", fontsize=17)
plt.xlabel("Flow Size (KB)", fontsize=17)
plt.xscale('log')
plt.yscale('log')
plt.gca().set_ylim(bottom=1)

Flow_Size = [3,12,48,192,768,3072,12288]
SlowDown = [8.923766595961975, 11.779556074766354, 36.96849315068493, 43.15830965909091, 35.872809278350516, 16.71843631948192, 11.761854988092088]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='32')

SlowDown = [9.19988488254117, 11.450700934579439, 39.32074652777778, 41.1603591160221, 36.07295918367347, 16.93721889055472, 11.76084943106642]
plt.plot(Flow_Size, SlowDown,  '-.', color='green', label='64')

SlowDown = [9.431223180189757, 11.410630841121495, 37.67939189189189, 42.98262614678899, 37.55050623052959, 16.928660669665167, 11.916141836464673]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='128')

SlowDown = [9.164126805404566, 11.9225, 39.51241721854305, 44.89590643274854, 35.40922297297297, 17.06150722021661, 12.36470048422368]
plt.plot(Flow_Size, SlowDown, ':', color='black', label='192')

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
plt.legend(bbox_to_anchor=(-0.1, 1.02, 1.1, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)
plt.tight_layout()

plt.show()
