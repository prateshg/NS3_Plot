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
plt.ylim([1,160])
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
plt.legend(handlelength=1.5,bbox_to_anchor=(-0.2, 1.02, 1.2, 1.02), loc=3, ncol=3, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(3,3))
plt.yscale('log')
plt.ylim([0.1,100])
labels = ['8', '16', '32', '64', '128']
collision = [9.7,2.4, 0.47, 0.1, 0.01]

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

rects1 = ax.bar(x + width/2, collision, width, label='collision')
#rects2 = ax.bar(x - width/2, spine_Tor, width, label='Spine->ToR')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('% of collisions', fontsize=16 )
ax.set_xlabel('# Physical Q', fontsize=16 )
#ax.set_title('Scores by group and gender')
ax.get_yaxis().set_ticks([0.01,0.1,1,10,100], minor=True)
ax.get_yaxis().set_ticks([], minor=False)
plt.ylim([0.01,100])
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
ax.set_xticklabels(labels)

#ax.legend(prop={'size': 14})
plt.tight_layout()

fig, (ax1,ax2)=plt.subplots(1,2,sharey=True,figsize=(8,3))#,gridspec_kw={'hspace':0.1,'wspace':0.1})
ax1.set_ylabel("FCT SlowDown", fontsize=16)
fig.text(0.5,0.05, "FlowSize (KB)", ha="center",fontsize=16)
ax1.set_xscale('log')
ax2.set_xscale('log')
ax1.set_yscale('log')
fig.text(0.4,0.3, "60 %", ha="center",fontsize=16)
fig.text(0.9,0.3, "90%", ha="center",fontsize=16)

size = [3,12,48,192,768,3072, 12288]
SlowDown = [3.8128132028568045, 3.9942757009345793, 8.022554347826087, 9.698497267759564, 12.17308282208589, 12.374356659142212, 11.724158078763342]
ax1.plot(Flow_Size, SlowDown, '--', color='red', label='8')

SlowDown = [1.1472790715909982, 1.7331473214285715, 4.159228187919463, 6.105347222222222, 9.041122611464969, 9.954905677009872, 9.68645027451959]
ax1.plot(Flow_Size, SlowDown,  '-.', color='green', label='16')

SlowDown = [1.1479761904761905, 1.7425438596491227, 4.078298611111111, 6.254166666666666, 9.43569587628866, 10.530746336996337, 9.637086563307493]
ax1.plot(Flow_Size, SlowDown, '-', color='blue', label='32')

SlowDown = [1.1474828934506354, 1.6935416666666667, 4.225775862068965, 6.18448275862069, 8.916568914956011, 10.403214097148892, 10.734796187537329]
ax1.plot(Flow_Size, SlowDown, '-.', color='brown', label='64')

SlowDown = [1.149798575432041, 1.7757954545454546, 4.5553294573643415, 6.599954212454213, 10.134437639198218, 12.228507615700059, 12.509318722831711]
ax1.plot(Flow_Size, SlowDown, '--', color='orange', label='128')
ax = ax1
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
for tick in ax2.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax2.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)

handles, labels = ax1.get_legend_handles_labels()
plt.figlegend(handles, labels, loc='upper center', ncol=5, labelspacing=0.0, fontsize=14, frameon=False)

SlowDown = [17.527766856693532, 17.6634009009009, 38.11494932432432, 52.20625, 73.07389053254438, 63.24658624229979, 47.88624551971326]
ax2.plot(Flow_Size, SlowDown, '--', color='red', label='8')

SlowDown = [14.094274432379072, 15.37340909090909, 28.703033088235294, 38.24234104046243, 47.41044161676647, 45.70361538461538, 31.387137989778534]
ax2.plot(Flow_Size, SlowDown,  '-.', color='green', label='16')

SlowDown = [2.9154604491041387, 5.008912037037037, 13.27986577181208, 19.267457805907174, 27.044096091205212, 31.09391979301423, 29.585286492954]
ax2.plot(Flow_Size, SlowDown, '-', color='blue', label='32')

SlowDown = [1.5451145736072205, 3.691521739130435, 13.171392617449664, 20.80475663716814, 32.67304794520548, 40.515439142461965, 37.871320093457946]
ax2.plot(Flow_Size, SlowDown, '-.', color='brown', label='64')

SlowDown = [1.5100530509209955, 3.4297566371681416, 11.285799319727891, 18.317561983471073, 26.930865384615384, 33.156924643584524, 31.25363049878767]
ax2.plot(Flow_Size, SlowDown, '--', color='orange', label='128')



fig.tight_layout(rect=[0.0,0.1,1,0.9])


plt.figure(figsize=(7,3))
plt.ylabel("FCT Slow Down", fontsize=16)
plt.xlabel("Flow Size (KB)", fontsize=16)
plt.xscale('log')
plt.yscale('log')
plt.gca().set_ylim(bottom=8)

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
ax.get_yaxis().set_ticks([8,16,32,64], minor=True)
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
plt.legend(bbox_to_anchor=(-0.1, 1.02, 1.1, 1.02), loc=3, ncol=5, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()

'''fig, ax = plt.subplots(figsize=(4,4))
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
plt.tight_layout()'''


plt.figure(figsize=(7,3))
plt.ylabel("FCT Slow Down", fontsize=16)
plt.xlabel("Flow Size (KB)", fontsize=16)
plt.xscale('log')
plt.yscale('log')
plt.gca().set_ylim(bottom=8)

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
ax.get_yaxis().set_ticks([8,16,32,64], minor=True)
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
plt.legend(bbox_to_anchor=(-0.1, 1.02, 1.1, 1.02), loc=3, ncol=5, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()

plt.show()
