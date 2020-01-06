from matplotlib import pyplot as plt
import sys
import numpy as np
import matplotlib
import matplotlib.cm as cm
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter
fig, ax = plt.subplots(dpi=100,figsize=(8,4))

colors=['blue', 'blue', 'blue', 'blue']#, 'purple', 'mediumvioletred', 'magenta','red', 'orange']
matplotlib.rcParams.update({'font.size': 16})

plt.ylabel('Buffer Size / Capacity (us)', fontsize=18)
label=['Trident2 (2012)', 'Tomahawk (2014)', 'Tomahawk2 (2016)', 'Tomahawk3 (2018)']
value=[80, 55, 52.5, 40]
Switch_Capacity=[1.28, 3.2, 6.4, 12.8]
#plt.plot(delay[0:3], throughput[0:3], 'o-', color='blue')
ax.scatter(Switch_Capacity, value, s=70, color=colors)
plt.xlabel(r'Switch Capacity (Tbps)', fontsize=18)
for i in range (4):
	if i==2:
		ax.annotate(label[i], (Switch_Capacity[i]-0.2,value[i]-9))
	elif i==3:
		ax.annotate(label[i], (Switch_Capacity[i]-3.8,value[i]-9))
	else:
		ax.annotate(label[i], (Switch_Capacity[i]-0.2,value[i]+3))

for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.xaxis.get_minor_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)

plt.ylim([0,100])
fig.tight_layout()
plt.draw()
plt.show()
