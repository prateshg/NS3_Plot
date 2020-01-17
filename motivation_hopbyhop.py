import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter

plt.figure(figsize=(8,3))
plt.ylabel("CDF", fontsize=17)
plt.xlabel("Measured Buffer Occupancy (MB)", fontsize=17)
plt.ylim([0.8,1.003])
plt.xlim([0,20])

CDF = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Buffer_Size = [2,3,4,5,6,6,7,8,8,9,9,10,10,11,11,12,12,13,14,14,15,15,16,17,17,18,19,19,20,21,22,22,23,24,24,25,26,27,27,28,29,29,30,31,32,33,34,36,38,44,38760,61200,77520,89760,102000,113220,123420,132600,141780,151980,161160,170340,178500,187680,197880,207060,217260,228858,241740,255000,270300,286620,309060,339660,389640,554880,701334,781320,840480,886380,927180,963900,996540,1027140,1056720,1085280,1113840,1143420,1173000,1203600,1234200,1267860,1301520,1339260,1381080,1426466,1482060,1547340,1649340,2221061]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/1e6, CDF, '-', color='blue', label='BFC')

Buffer_Size = [0,1090,1090,1090,2180,2180,3270,3270,4360,4360,5450,6540,6540,7630,8720,9810,10900,13080,14170,15260,17440,18530,20710,21800,23980,25070,27250,29430,30520,32700,34880,36380,38150,40330,42510,44690,46870,49050,51087,52997,55231,57770,59950,62130,64310,67580,69760,71940,75210,77674,80660,83930,87200,90470,93740,97010,100280,104640,108103,112270,116630,121421,126440,131890,137340,143880,150420,158050,165997,175490,185670,197693,211460,227810,248471,273229,303020,339246,380165,428370,479600,533120,587510,645847,711049,786560,870733,966404,1091066,1299448,1822851,2754378,3724751,4859104,5750248,6568443,7408273,8193881,8896020,14877612]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/1e6, CDF, '-.', color='green', label='HPCC')

Buffer_Size = [0,1020,2040,4080,8160,12240,17340,22440,27540,32640,37740,42840,47940,53040,58140,62220,67320,72420,76500,81600,86700,91800,96900,102000,107100,112200,117300,122563,128520,133620,139319,144840,150565,156060,162180,168300,174420,181130,187680,194318,201072,208080,215486,223321,230068,238680,246840,255000,263536,273360,283111,293760,305987,317673,330480,343674,358020,374011,392208,411772,433853,456803,485549,519748,557251,603840,660474,728850,804869,890808,977861,1065900,1158848,1250221,1354560,1476848,1603440,1741692,1889440,2019640,2153220,2300100,2457180,2600823,2736660,2910660,3074959,3271140,3516224,3807067,4173696,4614780,5198939,5908568,6691741,7479173,8231448,8951475,9794212,17982158]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/1e6, CDF, '--', color='red', label='DCQCN')


ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(0.1, 1.02, 0.8, 1.02), loc=3, ncol=3, mode="expand", borderaxespad=0., prop={'size': 16}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(8,3))
plt.ylabel("FCT Slow Down", fontsize=17)
plt.xlabel("Flow Size (KB)", fontsize=17)
plt.xscale('log')
plt.yscale('log')
plt.gca().set_ylim(bottom=1)

Flow_Size = [3,12,48,192,768,3072,12288]
SlowDown = [1.7614814887288666, 2.0563063063063063, 4.55375, 6.7936507936507935, 9.5851027397260271, 11.017340405198777, 9.5547609614368731]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='BFC')

SlowDown = [37.339306872037916, 44.950000000000003, 24.021232876712329, 23.926445578231291, 32.546551724137935, 41.574526515151518, 35.050402557968347]
plt.plot(Flow_Size, SlowDown,  '-.', color='green', label='HPCC')

SlowDown = [84.311817878454775, 83.493750000000006, 58.51672794117647, 48.563155021834064, 27.561369346733667, 31.396985446985447, 36.465393197907048]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='DCQCN')
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
plt.legend(bbox_to_anchor=(0.1, 1.02, 0.8, 1.02), loc=3, ncol=3, mode="expand", borderaxespad=0., prop={'size': 16}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(8,3))
plt.ylabel("CDF", fontsize=17)
plt.xlabel("Measured Buffer Occupancy (MB)", fontsize=17)
plt.ylim([0.8,1.003])
plt.xlim([0,2])

CDF = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Buffer_Size = [2,3,4,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,12,13,13,14,14,15,15,15,16,16,17,17,18,18,19,19,20,21,21,22,22,23,24,25,25,26,27,28,30,32,34,41,30600,48960,60834,70380,79560,88740,95880,103020,110160,117300,123420,130560,136680,143348,149940,157080,163200,170340,178500,186660,195840,205020,216240,228480,242760,259080,277440,297143,318240,338640,358020,376380,393720,410040,425340,441660,456960,472260,486878,502250,518160,533787,550800,569160,589560,613020,641580,676260,730320,1152600]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/1e6, CDF, '-', color='blue', label='BFC')

Buffer_Size = [0,0,1090,1090,1090,2180,2180,2180,2604,3270,3270,4360,4360,4360,5450,5450,6540,7630,7630,8720,9810,10900,11990,13080,14170,15260,16350,17440,18530,20023,21800,22890,23980,25070,26943,28340,29430,30520,32353,33790,34880,35970,38150,39240,40330,42510,43600,45076,46870,47960,50140,51230,53410,54500,56680,57770,59950,61620,63220,65400,67091,68670,70850,73030,75210,77042,79074,81090,83438,85877,88290,90470,92650,95364,98100,100521,103550,106820,109384,112270,115540,119345,123170,126841,130800,135160,140005,144970,150420,155870,162410,169799,177670,187425,197800,210370,226720,249610,287240,654160]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/1e6, CDF, '-.', color='green', label='HPCC')

Buffer_Size = [0,0,1020,2040,4080,6120,9180,13260,17340,20400,24480,27540,31620,34680,38760,41820,45900,48960,52020,56100,59160,62220,66300,69360,72420,75644,79045,82620,85680,88740,92028,95880,98940,102000,105810,109140,112918,116280,120360,123420,127500,130939,134640,138720,142207,145860,149639,153000,157080,160797,164554,168636,172380,176460,180540,184620,189233,193291,197880,202359,207060,211188,216240,220893,225420,230520,235620,240720,245941,251940,257040,263160,269189,274891,281149,287640,294780,301920,309060,317079,325207,333540,342703,351343,361259,371280,382500,394296,406338,419634,434520,450525,467606,488696,512044,542066,579329,632400,722078,1469464]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/1e6, CDF, '--', color='red', label='DCQCN')


ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(0.1, 1.02, 0.8, 1.02), loc=3, ncol=3, mode="expand", borderaxespad=0., prop={'size': 16}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(8,3))
plt.ylabel("FCT Slow Down", fontsize=17)
plt.xlabel("Flow Size (KB)", fontsize=17)
plt.xscale('log')
plt.yscale('log')
plt.gca().set_ylim(bottom=1)

SlowDown = [1.8404627985000988, 2.0184684684684684, 4.4074166666666663, 6.6460084033613445, 9.269750580046404, 10.239033533260633, 9.1659774436090231]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='BFC')

SlowDown = [2.634918775382693, 2.6974299065420562, 3.2298013245033115, 4.0952674897119339, 16.330216881594374, 37.763711890243904, 35.777601135557134]
plt.plot(Flow_Size, SlowDown,  '-.', color='green', label='HPCC')

SlowDown = [4.5514172224401728, 4.5377232142857142, 4.295774647887324, 4.3147972972972974, 5.1028819444444444, 16.432530864197531, 29.433623388005508]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='DCQCN')
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
plt.legend(bbox_to_anchor=(0.1, 1.02, 0.8, 1.02), loc=3, ncol=3, mode="expand", borderaxespad=0., prop={'size': 16}, frameon=False)
plt.tight_layout()


fig, (ax1,ax2,ax3)=plt.subplots(1,3,sharey=True,figsize=(8,3))#,gridspec_kw={'hspace':0.1,'wspace':0.1})
ax1.set_ylabel("FCT SlowDown", fontsize=17)
fig.text(0.5,0.05, "FlowSize (KB)", ha="center",fontsize=17)
ax1.set_ylim([1,128])
ax1.set_xscale('log')
ax2.set_xscale('log')
ax3.set_xscale('log')
ax1.set_yscale('log')
fig.text(0.3,0.76, "Median", ha="center",fontsize=17)
fig.text(0.6,0.76, "95 %ile", ha="center",fontsize=17)
fig.text(0.9,0.76, "99 %ile", ha="center",fontsize=17)

size = [3,12,48,192,768,3072, 12288]
SlowDown = [1.0303197137126903, 1.1372727272727272, 1.6591059602649008, 2.0686486486486486, 2.8228618421052634, 3.310940275310835, 3.597672710135285]
ax1.plot(size,SlowDown, '-', color='blue', label='BFC')

SlowDown = [1.049737133370227, 1.1677631578947369, 1.6470637583892618, 1.9671348314606742, 3.1511918604651163, 6.592286821705426, 8.8622225525168457]
ax1.plot(size,SlowDown, '-.', color='green', label='HPCC')

SlowDown = [1.0568698995605776, 1.175, 1.5687500000000001, 1.7964779005524862, 2.1313960280373832, 2.7582623714652956, 5.51726865548980]
ax1.plot(size,SlowDown, '--', color='red', label='DCQCN')
for tick in ax1.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax1.yaxis.get_major_ticks():
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
plt.figlegend(handles, labels, loc='upper center', ncol=3, labelspacing=0.0, fontsize=16, frameon=False)

SlowDown = [1.1049018636003172, 1.5288990825688074, 3.2783244680851062, 4.6363387978142079, 6.7663310961968683, 7.9351857062464832, 7.295728670420095]
ax2.plot(size,SlowDown, '-', color='blue', label='BFC')

SlowDown = [2.869206114398422, 3.0512731481481481, 3.3651845637583895, 4.1012430939226521, 10.629238095238096, 27.677124183006537, 25.943377976190476]
ax2.plot(size,SlowDown, '-.', color='green', label='HPCC')

SlowDown = [7.3091970745517463, 8.0702272727272728, 5.6583916083916082, 5.7144285714285719, 5.3944785276073617, 14.054482299200609, 27.640838068181818]
ax2.plot(size,SlowDown, '--', color='red', label='DCQCN')

SlowDown = [1.7614814887288666, 2.0563063063063063, 4.55375, 6.7936507936507935, 9.5851027397260271, 11.017340405198777, 9.554760961436873]
ax3.plot(size,SlowDown, '-', color='blue', label='BFC')

SlowDown = [37.339306872037916, 44.950000000000003, 24.021232876712329, 23.926445578231291, 32.546551724137935, 41.574526515151518, 35.05040255796834]
ax3.plot(size,SlowDown, '-.', color='green', label='HPCC')

SlowDown = [84.311817878454775, 83.493750000000006, 58.51672794117647, 48.563155021834064, 27.561369346733667, 31.396985446985447, 36.465393197907048]
ax3.plot(size,SlowDown, '--', color='red', label='DCQCN')

fig.tight_layout(rect=[0.0,0.1,1,0.9])


plt.show()