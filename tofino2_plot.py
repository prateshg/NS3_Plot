from scapy.all import *
import sys
import math
from matplotlib import pyplot as plt
import pylab as pl
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter

plt.figure(figsize=(7,3))
num_flows = [4,8,12,16,20]

bfc_da = [448.4,	572.125,	681.5,	860.125,	1070]
stddev = [12.30356768, 23.44865211, 24.81359075, 622.6777285, 593.8472477]
plt.errorbar(num_flows, bfc_da, yerr=stddev, marker = 's', capsize=5, label="BFC + dynamic")

bfc_sa = [600, 870, 1053, 1240, 1532]
stddev = [287.1225473, 428.0765744, 491.6847858, 579.6872155, 928.0172412]
eb1 = plt.errorbar(num_flows, bfc_sa, yerr=stddev, linestyle='--', marker = '^', capsize=5, label="BFC + stochastic")
eb1[-1][0].set_linestyle('--')

bfc_1 = [1577.875, 2060.5, 2531.5, 2525.375, 2558.125]
stddev = [22.66802342, 32.87639188, 33.08862558, 21.03016541, 37.76028715]
eb2 = plt.errorbar(num_flows, bfc_1, yerr=stddev, linestyle=':', marker = 'o', capsize=5, label="BFC + single")
eb2[-1][0].set_linestyle(':')

ideal = []
for i in range(len(num_flows)):
	tput = (48.0 * (8.0/(num_flows[i] + 8.0)))
	ideal.append(12*1e3 / tput)
#plt.plot(num_flows, ideal, label="Ideal")
plt.xlabel("# of flows in group 2", fontsize=16)
plt.ylabel("FCT (us)", fontsize=16)
#plt.yscale('log')
#plt.ylim([200,2800])

plt.ylim([0,2700])
ax = plt.axes()
'''ax.get_yaxis().set_ticks([200, 400, 800, 1600], minor=True)
ax.get_yaxis().set_ticks([], minor=False)
ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())
ax.yaxis.get_minor_formatter().set_scientific(False)
ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
ax.yaxis.get_major_formatter().set_scientific(False)'''
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_minor_ticks():
	tick.label.set_fontsize(14)
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(-0.18, 1.02, 1.18, 1.02), loc=3, ncol=3, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()
plt.figure(figsize=(4,3))
num_flows = []
bfc_sa = []
bfc_da = []
for i in range (50):
	num_flows.append(i+1)
	bfc_da.append(0.0)
	bfc_sa.append(0.0)
for i in range(len(num_flows)):
	bfc_sa[i] =  1 - ((13.0/15.0) ** num_flows[i])
	bfc_da[i] =  1 - ((13.0/15.0) ** max(0, num_flows[i]-13))
plt.plot(num_flows, bfc_da, label="BFC + dynamic")
plt.plot(num_flows, bfc_sa, label="BFC + stochastic")
plt.xlabel("Num of flows in group 2")
plt.ylabel("Probability of any collision")
plt.legend()
threshold = [26.0, 50, 75, 100, 150, 200]
utilization = [0.9185, 0.9485, 0.9835, 0.99475, 0.99075, 0.99535]
queuesize = [17.5075, 28.3, 41.9, 60.475, 77.4075, 99.4395]
for i in range(len(threshold)):
	threshold[i] = (threshold[i] * 0.34)/(12.5)
	queuesize[i] = queuesize[i] * 0.34
	utilization[i] = 100 - ((utilization[i] * 100) - 0.7)
fig,ax = plt.subplots(figsize=(4,3))
# make a plot
ax.plot(threshold, utilization, color="red", marker="o")
# set x-axis label
ax.set_xlabel("Pause Threshold (us)",fontsize=14)
# set y-axis label
ax.set_ylabel("Under-utilization (%)",color="red",fontsize=14)
ax.set_ylim([0, 15])
ax.set_xlim([0,6])
# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
ax2.set_ylim([0, 35])
# make a plot with different y-axis using second axis object
ax2.plot(threshold, queuesize, color="blue",marker="^")
ax2.set_ylabel("Avg. Queue Length (KB)",color="blue",fontsize=14)
#ax = plt.axes()
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(12)
for tick in ax2.yaxis.get_major_ticks():
	tick.label.set_fontsize(12)
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(12)
plt.tight_layout(rect=[0.05, 0, 1, 1])


plt.figure(figsize=(7,3.5))
x = []
y = []
for i in range(500):
	xval = 0.01 * i
	x.append(xval)
	yval = 1.0/((math.sqrt(xval) + 1.0) **2 + 1.0)
	y.append(yval)

plt.xlabel(r"Th ($HRTT \cdot \mu_f$)", fontsize=16)
plt.ylabel(r"$\max_{x>1} (E_f(Th,x))$", fontsize=16)
plt.ylim([0, 0.5])
plt.xlim([0, 5])
plt.plot(x,y)
ax = plt.axes()
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
#plt.legend(bbox_to_anchor=(-0.1, 1.02, 1.1, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 14}, frameon=False)
plt.tight_layout()


plt.show()
