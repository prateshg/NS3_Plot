import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import matplotlib
import matplotlib.cm as cm
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter
import subprocess

plt.figure(figsize=(4,3))
plt.ylabel("Fraction", fontsize=17)
plt.xlabel("Link Speed (Gbps)", fontsize=17)
plt.xscale('log')
plt.xlim([1,400])
plt.ylim([0,1.03])

Flow_Size = []
CDF = []
with open('NSDI2020/w3.txt') as fp:
	line = fp.readline()
	while line:
		CDF.append(float(line.split(' ')[1]))
		Flow_Size.append(float(line.split(' ')[0]))
		line = fp.readline()
CDF2 = [0]
avg_flow_size = 0.0
for i in range(len(CDF)-1):
	avg_flow_size += (CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])
for i in range(len(CDF)-1):
	CDF2.append(CDF2[i]+ (((CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])))/avg_flow_size)
speed=[]
fraction=[]
for i in range(len(CDF2)):
	speed.append(Flow_Size[i]/1500.0)
	fraction.append(1-CDF2[i])
plt.plot(speed,fraction,'-.', color='green', label='Google')
Flow_Size = []
CDF = []
with open('NSDI2020/w4.txt') as fp:
	line = fp.readline()
	while line:
		CDF.append(float(line.split(' ')[1]))
		Flow_Size.append(float(line.split(' ')[0]))
		line = fp.readline()
CDF2 = [0]
avg_flow_size = 0.0
for i in range(len(CDF)-1):
	avg_flow_size += (CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])
for i in range(len(CDF)-1):
	CDF2.append(CDF2[i]+ (((CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])))/avg_flow_size)
speed=[]
fraction=[]
for i in range(len(CDF2)):
	speed.append(Flow_Size[i]/1500.0)
	fraction.append(1-CDF2[i])
plt.plot(speed,fraction,'-.', color='blue', label='FB_Hadoop')
Flow_Size = [0, 100, 10000, 20000, 30000, 50000, 80000, 200000, 1000000, 2000000, 5000000, 10000000, 30000000]
CDF = [0.0, 0.0, 0.15, 0.2, 0.3, 0.4, 0.53, 0.6, 0.7, 0.8, 0.9, 0.97, 1.0]
CDF2 = [0]
avg_flow_size = 0.0
for i in range(len(CDF)-1):
	avg_flow_size += (CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])
for i in range(len(CDF)-1):
	CDF2.append(CDF2[i]+ (((CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])))/avg_flow_size)
speed=[]
fraction=[]
for i in range(len(CDF2)):
	speed.append(Flow_Size[i]/1500.0)
	fraction.append(1-CDF2[i])
plt.plot(speed,fraction, '--', color='red', label='WebSearch')
ax=plt.gca()
xt=[1,4, 10, 40,100,400]
ax.get_xaxis().set_ticks(xt)
ax.xaxis.set_major_formatter(mticker.ScalarFormatter())
ax.xaxis.get_major_formatter().set_scientific(False)
for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(14)
for tick in ax.xaxis.get_minor_ticks():
        tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(-0.2, 1.02, 1.25, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 16}, frameon=False)       
plt.tight_layout()


plt.figure(figsize=(4,3))
plt.ylabel("CDF", fontsize=17)
plt.xlabel("Flow Size (B)", fontsize=17)
plt.xscale('log')
plt.ylim([0,1.03])
Flow_Size = []
CDF = []
with open('NSDI2020/w3.txt') as fp:
	line = fp.readline()
	while line:
		CDF.append(float(line.split(' ')[1]))
		Flow_Size.append(float(line.split(' ')[0]))
		line = fp.readline()
CDF2 = [0]
avg_flow_size = 0.0
for i in range(len(CDF)-1):
	avg_flow_size += (CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])
for i in range(len(CDF)-1):
	CDF2.append(CDF2[i]+ (((CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])))/avg_flow_size)
plt.plot(Flow_Size, CDF2, '-.', color='green', label='Google')
Flow_Size = []
CDF = []
with open('NSDI2020/w4.txt') as fp:
	line = fp.readline()
	while line:
		CDF.append(float(line.split(' ')[1]))
		Flow_Size.append(float(line.split(' ')[0]))
		line = fp.readline()
CDF2 = [0]
print(len(CDF), len(Flow_Size))
avg_flow_size = 0.0
for i in range(len(CDF)-1):
	avg_flow_size += (CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])
for i in range(len(CDF)-1):
	CDF2.append(CDF2[i]+ (((CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])))/avg_flow_size)
plt.plot(Flow_Size, CDF2, '-', color='blue', label='FB_Hadoop')

Flow_Size = [0, 100, 10000, 20000, 30000, 50000, 80000, 200000, 1000000, 2000000, 5000000, 10000000, 30000000]
CDF = [0.0, 0.0, 0.15, 0.2, 0.3, 0.4, 0.53, 0.6, 0.7, 0.8, 0.9, 0.97, 1.0]
CDF2 = [0]
avg_flow_size = 0.0
for i in range(len(CDF)-1):
	avg_flow_size += (CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])
for i in range(len(CDF)-1):
	CDF2.append(CDF2[i]+ (((CDF[i+1]-CDF[i])*0.5*(Flow_Size[i]+Flow_Size[i+1])))/avg_flow_size)
plt.plot(Flow_Size, CDF2, '--', color='red', label='WebSearch')
ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(-0.2, 1.02, 1.2, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 16}, frameon=False)
plt.tight_layout()

plt.show()