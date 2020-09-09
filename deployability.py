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
#plt.gca().set_ylim(bottom=1)

Flow_Size = [3,12,48,192,768,3072,12288]
SlowDown = [3.8660902902746264, 12.101914414414415, 25.73079044117647, 38.46059160305344, 35.874466463414635, 19.80738245412844, 12.59138513513513]
#SlowDown = [1.9401319427984516, 6.845454545454546, 30.124662162162164, 41.778551912568304, 38.51766975308642, 15.880486425339367, 10.672056727480046]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='BFC')

SlowDown = [6.068801490780698, 13.684027777777779, 28.98537234042553, 40.775390625, 36.74043209876543, 19.933236589271417, 12.572142371151557]
plt.plot(Flow_Size, SlowDown,  '-.', color='green')#, label='BFC + Sampling')

SlowDown = [5.053214958035925, 8.767954545454545, 23.271161417322833, 37.29549278846154, 36.90705329153605, 19.570399022801304, 13.269732983485106]
plt.plot(Flow_Size, SlowDown,  '--', color='red', label='BFC - NIC')

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
plt.legend(handlelength=1.5,bbox_to_anchor=(-0.0, 1.02, 1.0, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()



plt.figure(figsize=(4,3))
plt.ylabel("CDF", fontsize=16)
plt.xlabel("Buffer Occupancy (us)", fontsize=16)
plt.ylim([0.8,1.03])
plt.xlim([0,40])

CDF = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Buffer_Size = [159120,450157,518596,558728,586500,610980,633420,650760,668100,683400,697680,712980,725220,737460,749700,760920,773160,784380,795600,806820,817020,829260,839460,850205,860880,871249,882300,892500,903498,913920,925140,936198,946941,958800,970284,982260,994500,1005720,1017960,1031220,1045500,1058760,1073040,1086918,1102620,1119540,1135260,1153141,1170307,1188300,1205640,1224000,1243380,1262760,1281120,1300201,1319706,1340280,1360680,1380683,1403520,1424940,1446360,1467780,1489200,1510620,1534080,1557540,1579980,1602420,1623840,1647300,1673497,1699320,1723800,1749300,1774800,1802340,1832662,1860480,1893120,1926780,1963500,2003280,2046708,2093040,2140980,2186880,2237566,2291940,2348040,2403643,2463447,2526430,2597940,2691308,2804316,2986949,3299700,4659360]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/3e5, CDF, '-', color='blue')#, label='BFC')

Buffer_Size = [156060,475320,546720,590580,623220,647700,670140,690540,707880,724200,740520,755820,770100,782340,794580,807840,820080,832320,843540,856800,868020,880260,892500,903720,914940,926160,937380,947580,959820,971040,982260,994020,1006107,1018980,1030200,1041420,1053660,1066920,1079160,1093440,1106700,1120980,1135260,1150560,1166880,1182520,1199520,1215840,1232160,1250520,1268880,1286561,1306620,1326000,1346400,1366893,1389240,1410660,1432080,1454520,1475940,1497360,1518780,1540200,1561620,1583040,1606500,1627920,1650617,1672800,1695240,1718700,1743180,1767660,1793160,1819680,1848240,1876800,1908420,1941060,1977070,2013480,2051906,2094060,2139960,2190277,2239920,2293980,2346567,2403120,2462280,2520420,2582640,2648892,2717979,2804789,2913120,3090384,3428220,4713039]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/3e5, CDF, '-.', color='green', label='BFC + Sampling')

Buffer_Size = [216240,502860,565080,603840,632400,655354,676894,695640,712980,730320,746640,760920,776220,789480,802740,816000,829260,842520,854760,866539,878220,889440,901680,913920,925140,937380,949620,961591,974100,985320,998580,1011840,1025100,1038360,1051620,1065900,1081200,1097520,1113840,1132200,1150374,1170960,1193400,1216772,1243380,1273980,1309680,1349460,1404540,1484100,1646280,1987955,2180760,2333760,2455140,2552040,2631600,2700960,2769300,2832540,2890680,2945760,2994720,3041862,3088560,3136065,3186480,3234420,3282945,3330924,3379260,3422631,3466980,3509820,3551502,3593460,3638985,3683312,3727674,3775020,3821503,3868860,3918840,3967800,4019820,4076940,4134060,4195885,4257289,4318680,4388040,4464540,4543080,4630800,4736880,4849080,4992751,5178629,5499840,7362461] 
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/3e5, CDF, '--', color='red')#, label='BFC - NIC')

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(handlelength=1.5,bbox_to_anchor=(0.0, 1.02, 0.7, 1.02), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()




fig, (ax1,ax2, ax3)=plt.subplots(1,3,sharey=True,figsize=(8,3))#,gridspec_kw={'hspace':0.1,'wspace':0.1})
ax1.set_ylabel("FCT SlowDown", fontsize=16)
fig.text(0.5,0.05, "FlowSize (KB)", ha="center",fontsize=16)
ax1.set_ylim([1,64])
ax1.set_xscale('log')
ax2.set_xscale('log')
ax3.set_xscale('log')
#ax4.set_xscale('log')
ax1.set_yscale('log')
fig.text(0.3,0.3, "Avg", ha="center",fontsize=16)
#fig.text(0.4,0.3, "Median", ha="center",fontsize=16)
fig.text(0.6,0.3, "95 pct", ha="center",fontsize=16)
fig.text(0.9,0.3, "99 pct", ha="center",fontsize=16)

size = [3,12,48,192,768,3072, 12288]
SlowDown = [1.2559611921011773, 1.5088375842671944, 2.5747294765394284, 3.352390760286762, 4.270536353227466, 4.542130364781309, 4.63241431827121]
ax1.plot(size,SlowDown, '-', color='blue', label='BFC')

SlowDown = [1.1347127359952665, 1.3513963011726475, 2.4829057892463875, 3.2630552732953166, 4.48985088675742, 5.158818903554653, 5.22932348957241]
ax1.plot(size,SlowDown, '--', color='orange', label='BFC + GhostDelay')

#SlowDown = [1.1405316535171997, 1.4850791384154263, 2.7338779917369167, 3.568849144867053, 4.134393263723888, 4.155934208163875, 4.072520318717824]
#ax1.plot(size,SlowDown, ':', color='black', label='IdealFQ')


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
for tick in ax3.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax3.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
'''for tick in ax4.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax4.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)'''

handles, labels = ax1.get_legend_handles_labels()
plt.figlegend(handles, labels, loc='upper center', ncol=3, labelspacing=0.0, fontsize=14, frameon=False)

SlowDown = [1.0998809523809523, 1.5856359649122806, 3.696083333333333, 5.64242125984252, 8.448653314917127, 11.49003136200717, 9.758931660899654]
ax2.plot(size,SlowDown, '-', color='blue', label='BFC')

SlowDown = [1.099355710480965, 1.5551136363636364, 3.938448275862069, 5.824242424242424, 9.316679104477611, 12.045523193096008, 9.9820238095238]
ax2.plot(size,SlowDown, '--', color='orange', label='BFC + GhostDelay')

#SlowDown = [1.1346770071557757, 1.8021739130434782, 4.620166666666667, 6.477340823970038, 8.106707317073171, 9.061534749034749, 8.13251846193022]
#ax2.plot(size,SlowDown, ':', color='black', label='IdealFQ')

SlowDown = [3.8660902902746264, 12.101914414414415, 25.73079044117647, 38.46059160305344, 35.874466463414635, 19.80738245412844, 12.591385135135136]
ax3.plot(size,SlowDown, '-', color='blue', label='BFC')

SlowDown = [1.413452380952381, 5.173967889908257, 15.452892561983472, 20.868389423076923, 28.458613138686133, 20.67322906523856, 12.48287453785565]
ax3.plot(size,SlowDown, '--', color='orange', label='BFC + GhostDelay')

#SlowDown = [1.8764489953632149, 7.747727272727273, 32.36291946308725, 45.783839779005525, 38.16572327044025, 16.450433436532506, 11.26463872380356]
#ax3.plot(size,SlowDown, ':', color='black', label='IdealFQ')

fig.tight_layout(rect=[0.0,0.1,1,0.9])
plt.show()