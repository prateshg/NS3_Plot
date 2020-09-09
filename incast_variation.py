import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter

fig, (ax1,ax2, ax3)=plt.subplots(1,3,sharey=True,figsize=(8,3))#,gridspec_kw={'hspace':0.1,'wspace':0.1})
ax1.set_ylabel("FCT SlowDown", fontsize=16)
fig.text(0.5,0.05, "FlowSize (KB)", ha="center",fontsize=16)
ax1.set_ylim([1,340])
ax1.set_xscale('log')
ax2.set_xscale('log')
ax3.set_xscale('log')
ax1.set_yscale('log')
fig.text(0.3,0.3, "10", ha="center",fontsize=16)
fig.text(0.6,0.3, "100", ha="center",fontsize=16)
fig.text(0.9,0.3, "1000", ha="center",fontsize=16)

size = [3,12,48,192,768,3072, 12288]
SlowDown = [1.1589285714285715, 1.9703947368421053, 5.739051724137931, 8.496163366336633, 12.478333333333333, 13.559327254805323, 10.449952300190]
ax1.plot(size,SlowDown, '-', color='blue', label='BFC + Flow FQ')

SlowDown = [1.1808962264150944, 1.9423863636363636, 5.185, 8.074785714285714, 11.341071428571428, 13.180942780337942, 10.576523656776263]
ax1.plot(size,SlowDown, ':', color='black', label='IdealFQ')

SlowDown = [2.6651614560689301, 2.7739224137931036, 3.3032258064516129, 4.056315104166667, 16.622902494331065, 36.946385017421605, 33.560745614035085]
ax1.plot(size,SlowDown, '-.', color='green', label='HPCC')

SlowDown = [1.1279104183109707, 1.668421052631579, 4.304446308724832, 6.41438679245283, 9.66253434065934, 10.655416108879963, 10.642283797216]
ax1.plot(size,SlowDown, '--', color='red', label='BFC + Dest. FQ')
ax = ax1
ax.get_yaxis().set_ticks([1,2,4,8,16,32,64,128,256], minor=True)
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
for tick in ax3.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax3.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)

handles, labels = ax1.get_legend_handles_labels()
plt.figlegend(handles, labels, loc='upper center', ncol=4, labelspacing=0.0, fontsize=14, frameon=False)

SlowDown = [3.8660902902746264, 12.101914414414415, 25.73079044117647, 38.46059160305344, 35.874466463414635, 19.80738245412844, 12.5913851351351]
ax2.plot(size,SlowDown, '-', color='blue', label='BFC.Flow')

SlowDown = [1.8357190347686652, 7.93536036036036, 33.62179054054054, 46.5646408839779, 37.80108024691358, 17.576265450264863, 13.25542191992922]
ax2.plot(size,SlowDown, ':', color='black', label='IdealFQ')

SlowDown = [65.612663670119218, 62.340771028037381, 48.514212328767123, 43.872933070866139, 54.530007530120479, 53.76351893095768, 44.55089642170634]
ax2.plot(size,SlowDown, '-.', color='green', label='HPCC')

SlowDown = [1.1331367924528302, 1.72109375, 4.697327586206897, 6.985076045627377, 9.780218160377359, 12.52962445308702, 10.99675057870370]
ax2.plot(size,SlowDown, '--', color='red', label='BFC.Dest')


SlowDown = [148.73584821781395, 143.79426605504588, 158.77682291666667, 148.97113486842105, 111.7419557416268, 53.933420229405634, 31.0183166213460]
SlowDown = [146.08889182212835, 146.1126168224299, 156.7071551724138, 151.2219827586207, 109.37156929347826, 44.54094972067039, 29.8330029732408]
ax3.plot(size,SlowDown, '-', color='blue', label='BFC.Flow')

SlowDown = [8.692839392634916, 52.606077981651374, 96.53362676056338, 78.41304945054945, 39.61287006578947, 15.926408163265306, 10.089697802197803]
ax3.plot(size,SlowDown, ':', color='black', label='IdealFQ')

SlowDown = [207.96391752577318, 197.09897727272727, 151.19586267605635, 201.83327702702704, 315.44483695652173, 192.27866869918699, 99.445710438573997]
ax3.plot(size,SlowDown, '-.', color='green', label='HPCC')

SlowDown = [1.134551886792453, 27.14090909090909, 125.70985099337749, 111.80944293478261, 59.41096416382253, 20.778836797877045, 13.282551858254]
SlowDown = [1.1291666666666667, 17.71553738317757, 123.52814569536424, 111.34241071428572, 63.3261673151751, 19.708230531996914, 12.040085415135929]
ax3.plot(size,SlowDown, '--', color='red', label='BFC.Dest')


fig.tight_layout(rect=[0.0,0.1,1,0.9])





fig, (ax1, ax3)=plt.subplots(1,2,sharey=True,figsize=(9,3))#,gridspec_kw={'hspace':0.1,'wspace':0.1})
ax1.set_ylabel("FCT SlowDown", fontsize=16)
fig.text(0.5,0.05, "FlowSize (KB)", ha="center",fontsize=16)
ax1.set_ylim([1,340])
ax1.set_xscale('log')
#ax2.set_xscale('log')
ax3.set_xscale('log')
#ax4.set_xscale('log')
ax1.set_yscale('log')
fig.text(0.3,0.3, "Avg", ha="center",fontsize=16)
#fig.text(0.4,0.3, "Median", ha="center",fontsize=16)
#fig.text(0.6,0.3, "95 pct", ha="center",fontsize=16)
fig.text(0.9,0.3, "99 pct", ha="center",fontsize=16)

size = [3,12,48,192,768,3072, 12288]
SlowDown = [9.828473651802701, 10.87176834550494, 15.01734361762278, 15.037329598540348, 12.811792395753807, 9.403667754238509, 8.870374066034225]
ax1.plot(size,SlowDown, '-', color='blue', label='BFC (32 queues)')

SlowDown = [2.154193479141136, 2.460837766824902, 4.245420015549881, 4.597364985546442, 4.86405425703747, 4.705767652441029, 4.71692506915023]
ax1.plot(size,SlowDown, '--', color='orange', label='BFC (128 queues)')

SlowDown = [1.352490183709537, 2.8403311256318036, 4.339482388855659, 4.44829931815507, 4.2720230985764776, 4.087448979451594, 3.975683149985877]
ax1.plot(size,SlowDown, ':', color='black', label='IdealFQ')

SlowDown = [35.531974090675774, 33.76407003745634, 27.072437281574523, 26.86085263147327, 41.03052895189085, 40.379013162296346, 25.033824172961584]
ax1.plot(size,SlowDown, '-.', color='green', label='HPCC')

#SlowDown = [1.1752638062329448, 2.525006649179079, 5.023025984307366, 5.082399353473469, 4.641367423858549, 4.13464212159792, 4.13807573019288]
#ax1.plot(size,SlowDown, '--', color='red', label='BFC + Dest. FQ')
ax = ax1
ax.get_yaxis().set_ticks([1,2,4,8,16,32,64,128,256], minor=True)
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
'''for tick in ax2.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax2.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)'''
for tick in ax3.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax3.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
'''for tick in ax4.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax4.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)'''

handles, labels = ax1.get_legend_handles_labels()
plt.figlegend(handles, labels, loc='upper center', ncol=4, labelspacing=0.0, fontsize=14, frameon=False)

'''SlowDown = [1.0328358792045942, 1.1653260869565218, 1.89, 2.4971428571428573, 3.717935982339956, 5.157446473551637, 7.34382719335604]
ax4.plot(size,SlowDown, '-', color='blue', label='BFC + Flow FQ (Q32)')

SlowDown = [1.034986937418359, 1.1675675675675676, 1.7901079136690647, 2.2548828125, 2.97123745819398, 3.464941837144003, 3.6201127819548873]
ax4.plot(size,SlowDown, ':', color='black', label='IdealFQ')

SlowDown = [2.4566666666666666, 2.7274774774774775, 3.25275, 4.114006024096385, 8.551067493112948, 23.201060514676318, 18.3567270553614]
ax4.plot(size,SlowDown, '-.', color='green', label='HPCC')

SlowDown = [1.0273685559894292, 1.1291666666666667, 1.6378472222222222, 2.0941929133858266, 2.9375, 3.452571243523316, 3.672790441911617]
ax4.plot(size,SlowDown, '--', color='red', label='BFC + Dest. FQ')'''


'''SlowDown = [73.58309523809524, 78.9303738317757, 99.44486301369864, 90.65686141304347, 59.53262240356083, 29.83839420180723, 21.42560809661507]
ax2.plot(size,SlowDown, '-', color='blue', label='BFC.Flow (Q32)')

SlowDown = [1.1302380952380953, 1.659009009009009, 4.1213576158940395, 5.931578947368421, 10.79961251435132, 12.507556675062972, 9.49452507598784]
ax2.plot(size,SlowDown, '-', color='orange', label='BFC + Flow FQ(Q128)')

SlowDown = [1.5697860806714854, 5.7805045871559635, 8.031953642384106, 8.663583815028902, 8.516459074733095, 8.36689500484966, 7.653813530683]
SlowDown = [1.4, 4.76, 9.4, 9.4, 9.3, 8.82, 7.81]
ax2.plot(size,SlowDown, ':', color='black', label='IdealFQ')

SlowDown = [143.7350767621754, 133.57362385321102, 106.20546357615893, 103.45238486842105, 178.17100422195415, 133.81574448034465, 70.98916776027997]
ax2.plot(size,SlowDown, '-.', color='green', label='HPCC')

SlowDown = [1.0817857142857144, 1.4347972972972973, 3.3379528985507245, 4.78505291005291, 7.072026854219949, 7.992185843054083, 7.831763118916632]
ax2.plot(size,SlowDown, '--', color='red', label='BFC.Dest')'''


SlowDown = [146.08889182212835, 146.1126168224299, 156.7071551724138, 151.2219827586207, 109.37156929347826, 44.54094972067039, 29.8330029732408]
ax3.plot(size,SlowDown, '-', color='blue', label='BFC.Flow (Q32)')

SlowDown = [47.5175, 55.12916666666667, 94.475625, 81.29070680628273, 48.203271028037385, 21.628327686350435, 12.467382188498403]
ax3.plot(size,SlowDown, '--', color='orange', label='BFC + Flow FQ(Q128)')

SlowDown = [8.692839392634916, 52.606077981651374, 96.53362676056338, 78.41304945054945, 39.61287006578947, 15.926408163265306, 10.089697802197803]
ax3.plot(size,SlowDown, ':', color='black', label='IdealFQ')

SlowDown = [207.96391752577318, 197.09897727272727, 151.19586267605635, 201.83327702702704, 315.44483695652173, 192.27866869918699, 99.445710438573997]
ax3.plot(size,SlowDown, '-.', color='green', label='HPCC')

#SlowDown = [1.1291666666666667, 17.71553738317757, 123.52814569536424, 111.34241071428572, 63.3261673151751, 19.708230531996914, 12.040085415135929]
#ax3.plot(size,SlowDown, '--', color='red', label='BFC.Dest')

fig.tight_layout(rect=[0.0,0.1,1,0.9])



plt.figure(figsize=(4,3))
plt.ylabel("FCT Slow Down\nMedian (Size>3MB)", fontsize=16)
plt.xlabel("Incast Degree", fontsize=16)
plt.yscale('log')
Speed = [1,2,3,4,5,6]

SlowDown = [3.81, 3.99, 4.22, 5.65, 7.63, 11.27]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-', color='blue', label='BFC 32', marker='o')


SlowDown = [8.09, 10, 18.4, 19.6, 18.4, 17.3]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-.', color='green', marker='s')#label='HPCC', marker='s')

SlowDown = [3.83, 3.91, 3.92, 4, 4.13, 4.92]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='red', label='BFC 128', marker='^')

SlowDown = [5.12, 6.9, 14, 15, 14.86, 17.8]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='orange', marker='x')#label='DCTCP', marker='x')

ax = plt.axes()
ax.get_yaxis().set_ticks([4,8,16], minor=True)
ax.get_yaxis().set_ticks([], minor=False)
ax.get_xaxis().set_ticks([1, 2, 3, 4, 5, 6])
label = [item.get_text() for item in ax.get_xaxis().get_ticklabels()]
label = ["10", "100", "200", "500", "1000", "2000"]
ax.set_xticklabels(label)
plt.xticks(rotation=18)

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
plt.legend(bbox_to_anchor=(-0.05, 0.98, 1.1, 0.98), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(4,3))
plt.ylabel('FCT Slow Down\n99 pct (Size<3KB)', fontsize=16)
plt.xlabel("Incast Degree", fontsize=16)
plt.yscale('log')
Speed = [1, 2, 3, 4, 5, 6]

SlowDown = [1.16, 3.84, 27.46, 119, 148, 190]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-', color='blue',  marker='o')#label='BFC 32', marker='o')


SlowDown = [2.53, 65, 169, 187, 201.2, 225]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-.', color='green', label='HPCC', marker='s')

SlowDown = [1.16, 1.87, 2.88, 14.79, 47.5, 80]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='red', marker='^')#label='BFC 128', marker='^')

SlowDown = [3.42, 84.6 ,170, 175,  183, 204]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='orange', label='DCTCP', marker='x')
plt.legend(bbox_to_anchor=(-0.05, 0.98, 1.1, 0.98), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)

ax = plt.axes()
ax.get_yaxis().set_ticks([1,2,4,8, 16, 32, 64, 128, 256], minor=True)
ax.get_yaxis().set_ticks([], minor=False)
ax.get_xaxis().set_ticks([1, 2, 3, 4, 5, 6])
label = [item.get_text() for item in ax.get_xaxis().get_ticklabels()]
label = ["10", "100", "200", "500", "1000", "2000"]
ax.set_xticklabels(label)
plt.xticks(rotation=18)

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
plt.tight_layout()




plt.figure(figsize=(4,3))
plt.ylabel("FCT Slow Down\nMedian (Size>3MB)", fontsize=16)
plt.xlabel("Incast Degree", fontsize=16)
plt.yscale('log')
Speed = [1,2,3,4,5,6]

SlowDown = [3.81, 3.99, 4.22, 5.65, 7.63, 11.27]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-', color='blue', label='BFC + Flow FQ', marker='o')


SlowDown = [8.09, 10, 18.4, 19.6, 18.4, 17.3]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-.', color='green', label='HPCC', marker='s')

SlowDown = [3.67, 3.74, 3.72, 3.79, 3.87, 3.89]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='red', marker='^')

SlowDown = [5.12, 6.9, 14, 15, 14.86, 17.8]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='orange',  marker='x')

ax = plt.axes()
ax.get_yaxis().set_ticks([4,8,16], minor=True)
ax.get_yaxis().set_ticks([], minor=False)
ax.get_xaxis().set_ticks([1, 2, 3, 4, 5, 6])
label = [item.get_text() for item in ax.get_xaxis().get_ticklabels()]
label = ["10", "100", "200", "500", "1000", "2000"]
ax.set_xticklabels(label)
plt.xticks(rotation=30)

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
plt.legend(bbox_to_anchor=(0.15, 0.96, 0.8, 0.96), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(4,3))
plt.ylabel('FCT Slow Down\n99 pct (Size<3KB)', fontsize=16)
plt.xlabel("Incast Degree", fontsize=16)
plt.yscale('log')
Speed = [1, 2, 3, 4, 5, 6]

SlowDown = [1.16, 3.84, 27.46, 119, 148, 190]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-', color='blue', marker='o')


SlowDown = [2.53, 65, 169, 187, 201.2, 225]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown,  '-.', color='green', marker='s')

SlowDown = [1.12, 1.13, 1.13, 1.13, 1.14, 1.16]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='red', label='BFC + IncastLabel', marker='^')

SlowDown = [3.42, 84.6 ,170, 175,  183, 204]
SlowDown = np.array(SlowDown)
plt.plot(Speed, SlowDown, '--', color='orange', label='DCTCP', marker='x')
plt.legend(bbox_to_anchor=(-0.15, 0.96, 1.25, 0.96), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)

ax = plt.axes()
ax.get_yaxis().set_ticks([1,2,4,8, 16, 32, 64, 128, 256], minor=True)
ax.get_yaxis().set_ticks([], minor=False)
ax.get_xaxis().set_ticks([1, 2, 3, 4, 5, 6])
label = [item.get_text() for item in ax.get_xaxis().get_ticklabels()]
label = ["10", "100", "200", "500", "1000", "2000"]
ax.set_xticklabels(label)
plt.xticks(rotation=30)

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
plt.tight_layout()








plt.show()