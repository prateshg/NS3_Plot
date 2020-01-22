import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter

fig, (ax1,ax2)=plt.subplots(1,2,sharey=True,figsize=(8,3))#,gridspec_kw={'hspace':0.1,'wspace':0.1})
ax1.set_ylabel("FCT SlowDown", fontsize=17)
fig.text(0.5,0.05, "FlowSize (KB)", ha="center",fontsize=17)
ax1.set_ylim([1,340])
ax1.set_xscale('log')
ax2.set_xscale('log')
ax1.set_yscale('log')
fig.text(0.42,0.3, "BFC", ha="center",fontsize=17)
fig.text(0.9,0.3, "HPCC", ha="center",fontsize=17)

size = [3,12,48,192,768,3072, 12288]
SlowDown = [2.0937413609257138, 2.3983695652173913, 4.4918074324324326, 6.7105263157894735, 9.2157534246575334, 10.531673819742489, 9.9525620576213729]
ax1.plot(size,SlowDown, '-.', color='green', label='10')

SlowDown = [2.2363346747149566, 2.6521396396396395, 4.8018581081081084, 6.9927763819095476, 9.981457703927493, 10.678372681281619, 9.7158230076034915]
ax1.plot(size,SlowDown, '-', color='blue', label='100')

SlowDown = [2.0119729561218924, 2.2796052631578947, 4.5492943548387093, 6.2531655844155845, 8.6755255255255257, 9.3961096205442693, 8.2748427190425033]
ax1.plot(size,SlowDown, '--', color='red', label='1000')
for tick in ax1.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax1.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax2.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax2.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)

handles, labels = ax1.get_legend_handles_labels()
plt.figlegend(handles, labels, loc='upper center', ncol=3, labelspacing=0.0, fontsize=16, frameon=False)

SlowDown = [2.6651614560689301, 2.7739224137931036, 3.3032258064516129, 4.056315104166667, 16.622902494331065, 36.946385017421605, 33.560745614035085]
ax2.plot(size,SlowDown, '-.', color='green', label='10')

SlowDown = [65.612663670119218, 62.340771028037381, 48.514212328767123, 43.872933070866139, 54.530007530120479, 53.76351893095768, 44.55089642170634]
ax2.plot(size,SlowDown, '-', color='blue', label='100')

SlowDown = [207.96391752577318, 197.09897727272727, 151.19586267605635, 201.83327702702704, 315.44483695652173, 192.27866869918699, 99.445710438573997]
ax2.plot(size,SlowDown, '--', color='red', label='1000')


fig.tight_layout(rect=[0.0,0.1,1,0.9])




plt.show()