import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess

plt.figure(figsize=(8,3))
plt.ylabel("CDF", fontsize=17)
plt.xlabel("Flow Size (B)", fontsize=17)
plt.xscale('log')
Flow_Size = []
CDF = []
with open('w3.txt') as fp:
	line = fp.readline()
	while line:
		CDF.append(float(line.split(' ')[1]))
		Flow_Size.append(float(line.split(' ')[0]))
		line = fp.readline()
CDF2 = [0]
plt.ylim([0,1.03])
avg_flow_size = 0.0
for i in range(len(CDF)-1):
	avg_flow_size += (CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])
for i in range(len(CDF)-1):
	CDF2.append(CDF2[i]+ (((CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])))/avg_flow_size)
plt.plot(Flow_Size, CDF2, '-.', color='green', label='Google')

Flow_Size = []
CDF = []
with open('w4.txt') as fp:
	line = fp.readline()
	while line:
		CDF.append(float(line.split(' ')[1]))
		Flow_Size.append(float(line.split(' ')[0]))
		line = fp.readline()
CDF2 = [0]
print(len(CDF), len(Flow_Size))
avg_flow_size = 0.0
avg_flow_size = 0.0
for i in range(len(CDF)-1):
	avg_flow_size += (CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])
for i in range(len(CDF)-1):
	CDF2.append(CDF2[i]+ (((CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])))/avg_flow_size)
plt.plot(Flow_Size, CDF2, '-', color='blue', label='Facebook_Hadoop')

Flow_Size = [0, 100, 10000, 20000, 30000, 50000, 80000, 200000, 1000000, 2000000, 5000000, 10000000, 30000000]
CDF = [0.0, 0.0, 0.15, 0.2, 0.3, 0.4, 0.53, 0.6, 0.7, 0.8, 0.9, 0.97, 1.0]
CDF2 = [0]
avg_flow_size = 0.0
for i in range(len(CDF)-1):
	avg_flow_size += (CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])
for i in range(len(CDF)-1):
	CDF2.append(CDF2[i]+ (((CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])))/avg_flow_size)
plt.plot(Flow_Size, CDF2, '--', color='red', label='WebSearch')


# for i in range (len(W3)):
# 	print(W3[i])
# 	CDF.append(W3[0,i])
# 	Flow_Size.append(W3[1,i])
#plt.tight_layout()
ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(0.0, 1.02, 0.95, 1.02), loc=3, ncol=3, mode="expand", borderaxespad=0., prop={'size': 16}, frameon=False)
plt.tight_layout()
plt.show()