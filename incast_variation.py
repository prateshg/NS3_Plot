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
ax1.set_ylabel("FCT SlowDown", fontsize=17)
fig.text(0.5,0.05, "FlowSize (KB)", ha="center",fontsize=17)
ax1.set_ylim([1,340])
ax1.set_xscale('log')
ax2.set_xscale('log')
ax3.set_xscale('log')
ax1.set_yscale('log')
fig.text(0.3,0.3, "10", ha="center",fontsize=17)
fig.text(0.6,0.3, "100", ha="center",fontsize=17)
fig.text(0.9,0.3, "1000", ha="center",fontsize=17)

size = [3,12,48,192,768,3072, 12288]
SlowDown = [1.1811825318940137, 1.9551535087719298, 5.3253378378378375, 8.142579681274901, 11.630259295499021, 13.820681710775048, 11.197148314014752]
ax1.plot(size,SlowDown, '-', color='blue', label='BFC.Flow')

SlowDown = [2.6651614560689301, 2.7739224137931036, 3.3032258064516129, 4.056315104166667, 16.622902494331065, 36.946385017421605, 33.560745614035085]
ax1.plot(size,SlowDown, '--', color='green', label='HPCC')

SlowDown = [2.0937413609257138, 2.3983695652173913, 4.4918074324324326, 6.7105263157894735, 9.2157534246575334, 10.531673819742489, 9.9525620576213729]
ax1.plot(size,SlowDown, ':', color='red', label='BFC.Dest')
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

SlowDown = [9.431223180189757, 11.410630841121495, 37.67939189189189, 42.98262614678899, 37.55050623052959, 16.928660669665167, 11.916141836464673]
ax2.plot(size,SlowDown, '-', color='blue', label='BFC.Flow')

SlowDown = [65.612663670119218, 62.340771028037381, 48.514212328767123, 43.872933070866139, 54.530007530120479, 53.76351893095768, 44.55089642170634]
ax2.plot(size,SlowDown, '--', color='green', label='HPCC')

SlowDown = [2.2363346747149566, 2.6521396396396395, 4.8018581081081084, 6.9927763819095476, 9.981457703927493, 10.678372681281619, 9.7158230076034915]
ax2.plot(size,SlowDown, ':', color='red', label='BFC.Dest')


fig.tight_layout(rect=[0.0,0.1,1,0.9])

SlowDown = [159.2502864706812, 152.65969626168226, 151.9576286764706, 141.93381818181817, 93.60061643835617, 39.87015255905512, 23.605209088711625]
ax3.plot(size,SlowDown, '-', color='blue', label='BFC.Flow')

SlowDown = [207.96391752577318, 197.09897727272727, 151.19586267605635, 201.83327702702704, 315.44483695652173, 192.27866869918699, 99.445710438573997]
ax3.plot(size,SlowDown, '--', color='green', label='HPCC')

SlowDown = [2.0119729561218924, 2.2796052631578947, 4.5492943548387093, 6.2531655844155845, 8.6755255255255257, 9.3961096205442693, 8.2748427190425033]
ax3.plot(size,SlowDown, ':', color='red', label='BFC.Dest')


fig.tight_layout(rect=[0.0,0.1,1,0.9])




plt.show()