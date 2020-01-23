import pylab as pl
import math
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import subprocess
import matplotlib.ticker as mticker
from matplotlib.ticker import ScalarFormatter

#Google 65+INCAST

plt.figure(figsize=(4,3))
plt.ylabel("FCT Slow Down", fontsize=17)
plt.xlabel("Flow Size (KB)", fontsize=17)
plt.xscale('log')
plt.yscale('log')
plt.gca().set_ylim(bottom=1)

Flow_Size = [1,2,4,8,16,64,256,1024,4096]
SlowDown = [10.16691153269701, 10.981666666666667, 11.354672897196261, 16.152662037037036, 26.880088495575222, 41.9492125984252, 55.899534574468085, 37.87865566037736, 14.652324159021406]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='BFC')

SlowDown = [72.027397393882651, 69.122976190476194, 68.608018867924528, 66.427893518518516, 63.961184210526319, 56.078457446808514, 64.073117154811712, 108.44189189189188, 81.822014622258322]
plt.plot(Flow_Size, SlowDown,  '-.', color='green', label='HPCC')

SlowDown = [126.55198519515477, 122.16833333333334, 121.82676886792453, 119.1658256880734, 113.58056722689075, 101.65195312500001, 82.68113738738738, 104.44777508090615, 105.07501813346228]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='DCQCN')

SlowDown = [2.194623389494549, 3.3286904761904763, 5.434696261682243, 9.299099099099099, 15.938970588235295, 34.25208333333333, 59.268316831683165, 44.58372140522876, 16.31128566576087]
plt.plot(Flow_Size, SlowDown, ':', color='black', label='IdealFQ')

#SlowDown = [8.1422532265774379, 8.2588095238095232, 8.1824074074074069, 8.0761261261261268, 8.7123893805309738, 11.132753164556963, 84.920606060606062, 97.087581168831164, 75.512964684014875]
#plt.plot(Flow_Size, SlowDown, '-.', color='brown', label='HPCC+SFQ')

SlowDown = [93.177521423212099, 89.373809523809527, 88.060280373831773, 87.055795454545461, 82.129310344827587, 72.228614457831327, 65.358786610878667, 93.463412162162157, 42.02912754303599]
plt.plot(Flow_Size, SlowDown, '--', color='orange', label='DCTCP')
ax = plt.axes()
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
plt.legend(bbox_to_anchor=(-0.1, 1.02, 1.1, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(4,3))
plt.ylabel("CDF", fontsize=17)
plt.xlabel("Buffer Occupancy (MB)", fontsize=17)
plt.ylim([0.8,1.03])
plt.xlim([0,12])

CDF = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Buffer_Size = [259712,790700,954781,1034944,1086966,1127942,1160453,1188504,1213411,1236315,1257943,1276864,1294771,1312525,1328246,1343698,1360607,1375313,1389396,1402805,1417159,1429837,1442061,1454653,1466941,1479246,1490713,1502335,1513651,1525656,1536586,1547753,1558848,1570226,1580922,1592050,1603134,1614498,1625694,1636254,1646766,1657292,1667608,1677130,1688246,1698357,1708497,1719378,1729355,1739241,1749048,1759252,1769857,1779788,1790729,1800832,1811108,1822457,1832602,1843836,1855092,1865669,1876449,1887679,1898624,1909786,1921309,1932895,1945351,1957734,1970080,1982674,1995508,2008634,2021955,2034454,2047823,2062853,2078727,2093580,2109664,2125224,2142397,2160325,2177930,2195290,2213326,2232189,2253875,2275763,2297522,2322103,2349101,2379947,2415312,2454569,2505001,2572790,2679190,3534359]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/1e6, CDF, '-', color='blue', label='BFC')

Buffer_Size = [8720,16232,22901,29056,34940,40691,46208,51665,57093,62515,67868,73261,78468,83821,89022,94376,99740,105132,110876,116603,122423,128594,134677,141282,148300,155457,163031,170908,179418,188481,198157,208606,220014,232249,245955,261224,278833,299519,323196,351977,387027,428990,474644,525985,580798,634302,685364,740079,793411,843537,894062,943390,990811,1037291,1083088,1130840,1178700,1227406,1274804,1322177,1370357,1414372,1458421,1505856,1553709,1600095,1644815,1690813,1739108,1790453,1847580,1909840,1973901,2040459,2108868,2182022,2260562,2346903,2439969,2544298,2646961,2765282,2891466,3021643,3161644,3322431,3488275,3687272,3898597,4099947,4314727,4531112,4809573,5122604,5393182,5590178,5733911,5854983,5958590,6721697]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/1e6, CDF, '-.', color='green', label='HPCC')

Buffer_Size = [2040,6700,13113,20209,28405,37436,46321,55606,65688,75579,86080,96654,107845,119413,131112,143792,156695,171280,186819,203356,220562,240281,261539,286947,311505,341707,377389,417712,472771,546314,667310,870241,1085210,1251270,1400551,1538068,1673765,1795707,1914139,2021564,2125584,2212556,2309604,2414690,2512791,2613417,2709161,2804514,2906564,2998064,3093759,3184544,3281556,3377501,3476720,3576502,3674141,3772343,3861340,3946693,4022558,4108338,4189823,4271362,4354990,4429858,4511980,4591654,4680864,4764456,4847453,4922818,4995849,5061080,5127664,5189692,5250674,5324521,5387024,5446025,5498111,5539008,5577040,5608287,5633111,5665416,5718337,5817681,5950975,6141572,6342062,6539769,6741425,6946297,7112014,7268944,7420471,7573770,7734787,8364395]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/1e6, CDF, '--', color='red', label='DCQCN')

Buffer_Size = [2040,8160,15300,23585,32640,40800,49649,58140,67120,75696,85142,93840,102637,111306,120360,128137,136680,144840,153124,161598,170340,179642,188700,197880,207060,216240,224538,233708,242760,251940,262021,272340,281736,291849,302940,313570,324200,335046,345780,356918,368653,381199,393844,406278,419342,432860,447654,462198,477854,492972,508787,523712,539706,557424,574260,593192,610314,631380,651780,672916,694620,717614,742033,767040,794471,824391,854935,885203,918655,956282,997141,1042911,1093973,1151580,1212661,1288624,1382100,1494770,1687745,2224461,3126553,4123885,5139033,6177848,6998270,7854634,8691855,9479564,10201744,10561469,10728045,10887122,11034115,11190098,11374921,11657483,12299907,15253793,19481373,34182910]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/1e6, CDF, ':', color='black', label='IdealFQ')

#Buffer_Size=[5450,11092,16504,21608,26160,30709,35266,39560,43958,48332,52573,56886,61155,65400,69610,73834,78058,82269,86471,90767,95272,99748,104352,108968,113668,118579,123562,128857,134641,140230,146074,152246,158931,165827,173053,180835,188894,197536,206581,216656,227080,238163,249900,262224,275769,290136,305777,321719,338322,355774,373855,392326,411104,429621,449066,468933,488866,508841,529536,550224,570466,590415,611108,632782,654172,676651,699564,722876,747187,771598,797977,826142,853711,884236,916449,952216,988394,1027147,1069953,1117511,1170254,1231283,1301851,1390660,1489053,1611053,1763254,1952154,2209112,2564839,3092997,3691028,4288638,4852562,5239413,5492098,5655569,5768801,5865724,6574642]
#Buffer_Size = np.array(Buffer_Size)
#plt.plot(Buffer_Size/1e6, CDF, '-.', color='brown', label='HPCC+SFQ')

Buffer_Size=[20329,40606,58558,75881,92655,108827,125381,142173,159368,177082,195331,214482,234893,258174,283964,311630,344208,380352,420588,465803,515618,572147,629889,688643,749307,806620,865078,921711,978182,1032672,1087230,1143211,1199607,1254218,1313518,1375461,1434250,1493790,1548914,1604637,1660346,1720310,1775811,1831773,1886400,1942074,1998014,2053002,2106685,2160313,2213391,2269578,2329911,2390898,2455350,2523385,2591464,2661694,2732609,2807119,2886630,2968730,3049526,3128418,3208913,3293613,3379935,3474726,3568651,3663157,3761915,3861622,3964067,4079446,4200085,4307202,4424674,4543084,4663413,4772996,4884630,4998954,5112913,5208838,5292275,5375311,5458626,5542147,5617124,5686743,5750051,5814473,5876095,5943015,6018731,6099046,6192420,6328149,6643620,8586865]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/1e6, CDF, '--', color='orange', label='DCTCP')

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(-0.1, 1.02, 1.1, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)
plt.tight_layout()

fig, ax = plt.subplots(figsize=(4,3))
labels = ['BFC', 'HPCC', 'DCQCN', 'DCTCP']#, 'HPCC+SFQ',]
spine_Tor= [0, 6.5, 9.98, 12.44]#, 4.5]
ToR_spine = [0, 0.0, 0.33, 0.0]#, 0.0]

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

rects2 = ax.bar(x - width/2, spine_Tor, width, label='Core->ToR', hatch='\\\\')
rects1 = ax.bar(x + width/2, ToR_spine, width, label='ToR->Core', hatch='//')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('% of time paused', fontsize=19 )
#ax.set_title('Scores by group and gender')
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation='vertical')
ax.legend(bbox_to_anchor=(-0.15, 0.97, 1.23, 0.97), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)

fig.tight_layout()


fig, ax = plt.subplots(figsize=(4,3))
labels = ['BFC', 'HPCC', 'DCQCN', 'IdealFQ', 'DCTCP']#,'HPCC+SFQ',]
spine_Tor= [68,117.5, 132.5, 82, 87.8]#, 109.5]
ToR_spine = [95, 212, 357, 128, 151.4]#, 183]

x = np.arange(len(labels))  # the label locations
width = 0.16  # the width of the bars

rects2 = ax.bar(x - width/2, spine_Tor, width, label='Avg', hatch='\\\\')
rects1 = ax.bar(x + width/2, ToR_spine, width, label='99', hatch='//')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Incast\nFCT SlowDown', fontsize=19 )
#ax.set_title('Scores by group and gender')
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation='vertical')
ax.legend(bbox_to_anchor=(-0.15, 0.97, 1.23, 0.97), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)

fig.tight_layout()


#GOOGLE 65

plt.figure(figsize=(4,3))
plt.ylabel("FCT Slow Down", fontsize=17)
plt.xlabel("Flow Size (KB)", fontsize=17)
plt.xscale('log')
plt.yscale('log')
plt.gca().set_ylim(bottom=1)

Flow_Size = [1,2,4,8,16,64,256,1024,4096]
SlowDown = [1.1251842115744612, 1.2178571428571427, 1.3630841121495327, 1.648394495412844, 2.161217948717949, 3.671478873239437, 6.569094488188976, 8.836479591836735, 9.50988389626055]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='BFC')

SlowDown = [3.3950374936201952, 3.3667452830188678, 3.3864386792452832, 3.3836805555555554, 3.4396739130434781, 3.5637335526315788, 7.2695733532934135, 38.179823825503355, 55.93924660120846]
plt.plot(Flow_Size, SlowDown,  '-.', color='green', label='HPCC')

SlowDown = [5.5680991784268254, 5.3908333333333331, 5.3823113207547166, 5.3576388888888893, 5.2713983050847455, 5.0280075187969926, 4.7675480769230774, 6.4582838983050843, 35.664839307787389]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='DCQCN')

SlowDown = [1.1329463076555406, 1.2298809523809524, 1.3778301886792452, 1.6767201834862386, 2.2194327731092436, 3.770727848101266, 6.690982142857143, 9.191323138297872, 9.17022893772893]
plt.plot(Flow_Size, SlowDown, ':', color='black', label='IdealFQ')

#SlowDown = [2.6244971321596431, 2.6467857142857141, 2.6856132075471697, 2.8106818181818181, 3.0769957983193277, 3.7068877551020409, 9.1218658892128275, 41.835255960729313, 59.446952073991028]
#plt.plot(Flow_Size, SlowDown, '-.', color='brown', label='HPCC+SFQ')

SlowDown = [3.95550972304066, 3.8992857142857145, 3.9047169811320757, 3.8863425925925927, 3.8943750000000001, 3.8832908163265305, 4.9159254807692312, 12.054099678456591, 16.138358695652173]
plt.plot(Flow_Size, SlowDown, '--', color='orange', label='DCTCP')

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
plt.legend(bbox_to_anchor=(-0.1, 1.02, 1.1, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(4,3))
plt.ylabel("CDF", fontsize=17)
plt.xlabel("Buffer Occupancy (MB)", fontsize=17)
plt.ylim([0.8,1.03])
plt.xlim([0,3])

CDF = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99, 1.0]
Buffer_Size = [5304,12668,18360,23332,27540,31200,34680,37740,40800,43860,46327,49006,52011,54060,56534,59160,61200,63365,65629,68064,70380,72520,74757,77064,79560,81600,83762,85928,88381,90780,93123,95880,98047,100646,103020,105898,108429,111233,114240,117300,120360,123420,126480,129601,132976,136537,139894,143841,147900,151980,156173,160467,165113,169694,174420,179090,183848,188700,193697,198251,203231,208080,213180,217593,222815,227713,232964,237723,242760,247560,252489,257599,262842,267889,272765,277802,282662,287796,293016,298197,303729,309185,314957,320424,326966,333540,340315,347184,354320,362100,370583,379514,389028,399318,412296,427380,445740,471240,511727,854099]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/1e6, CDF, '-', color='blue', label='BFC')

Buffer_Size = [2621,5791,8858,11755,14558,17226,19818,22353,24828,27262,29484,31814,34006,36184,38334,40440,42510,44595,46694,48810,50921,52981,55049,57094,59091,61085,63082,65117,67092,69056,71064,73030,75053,77088,79144,81176,83216,85200,87291,89345,91390,93440,95485,97588,99745,101866,104044,106226,108353,110505,112769,115044,117360,119686,122000,124399,126814,129319,131834,134371,136992,139583,142214,144939,147816,150642,153538,156469,159575,162705,165930,169296,172656,176097,179680,183443,187427,191434,195738,199987,204516,209251,214130,219467,224976,230821,237116,243674,250579,258378,266967,276409,286915,299136,313552,330003,351094,380713,428231,900491]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/1e6, CDF, '-.', color='green', label='HPCC')

Buffer_Size = [1020,4080,7140,10854,14555,18396,22333,26270,30303,34290,38264,42066,45990,50152,54188,58007,62096,66078,70086,73912,77801,81694,85535,89306,93163,97056,100903,104882,109238,113292,117290,121384,125526,129378,133497,137425,141781,146056,150066,154065,158407,162805,167105,171512,175701,180333,184776,189163,193638,198265,203085,207763,212621,217576,222658,227569,232861,238098,243226,248610,253977,259353,265339,271205,276852,283184,289421,296379,302788,309934,316433,323383,330443,337610,345044,353021,361444,369415,377895,387119,396596,407090,417899,428561,440851,452250,464781,478626,493001,508176,525123,543678,564181,589637,617804,652983,699471,756228,856110,1677952]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/1e6, CDF, '--', color='red', label='DCQCN')

Buffer_Size = [1276,5266,10200,16320,22440,28560,34803,41400,47879,54060,60180,66300,72541,78661,84660,90780,96217,102000,107438,113220,118510,124440,129540,135044,140973,146880,152396,158100,163613,169320,174862,180665,186540,191894,197880,204000,209287,215220,221158,226570,232560,238099,244030,249944,256020,262140,268207,274509,281417,287764,294702,301166,308040,314647,322028,329310,336053,343505,350488,357491,365416,373320,381837,390260,398259,406980,415606,425138,434130,443311,452456,461426,471611,481680,492910,504003,516764,528521,541966,554880,569654,584460,600063,617063,634639,653984,675361,697357,722160,748031,778386,810878,845960,885387,931430,991569,1067203,1157827,1302726,2130058]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/1e6, CDF, ':', color='black', label='IdealFQ')

#Buffer_Size=[2180,4360,6540,8720,10900,13080,15260,17440,19620,21561,23534,25526,27493,29515,31496,33297,35234,37138,39044,40810,42709,44681,46443,48242,50140,51922,53796,55626,57506,59316,61141,62982,64800,66666,68519,70342,72231,74113,75987,77840,79719,81639,83519,85468,87392,89342,91278,93223,95223,97243,99312,101386,103550,105707,107928,110124,112359,114597,116821,119174,121560,123996,126409,128948,131603,134307,137038,139818,142745,145707,148730,151816,155030,158315,161661,165140,168805,172544,176374,180313,184448,188771,193377,198316,203444,208694,214439,220604,227166,234282,242293,250674,260344,271323,284361,299577,319333,345773,388123,770619]
#Buffer_Size = np.array(Buffer_Size)
#plt.plot(Buffer_Size/1e6, CDF, '-.', color='brown', label='HPCC+SFQ')

Buffer_Size=[2253,6288,10426,14251,18209,22103,25904,29595,33149,36704,40158,43481,46779,49992,53270,56526,59650,62772,65964,69025,72094,75053,78113,80997,83852,86693,89619,92462,95317,98160,101020,103837,106699,109565,112458,115291,118165,121086,123970,126886,129761,132648,135646,138687,141694,144711,147702,150747,153821,156884,160009,163114,166305,169550,172782,176049,179381,182813,186295,189781,193253,196806,200489,204244,208109,212022,215953,219929,224136,228344,232648,237094,241797,246616,251624,256750,262220,267556,273081,278971,284929,291433,298083,305030,312477,320327,328691,337626,346847,356829,367940,380078,393417,408684,426799,448590,476051,512393,574883,1082165]
Buffer_Size = np.array(Buffer_Size)
plt.plot(Buffer_Size/1e6, CDF, '--', color='orange', label='DCTCP')

ax = plt.axes()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(14)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(14)
plt.legend(bbox_to_anchor=(-0.1, 1.02, 1.1, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)
plt.tight_layout()


#FB65 + Incast

plt.figure(figsize=(4,3))
plt.ylabel("FCT Slow Down", fontsize=17)
plt.xlabel("Flow Size (KB)", fontsize=17)
plt.xscale('log')
plt.yscale('log')
plt.gca().set_ylim(bottom=1)

Flow_Size = [3,12,48,192,768,3072,12288]
SlowDown = [9.431223180189757, 11.410630841121495, 37.67939189189189, 42.98262614678899, 37.55050623052959, 16.928660669665167, 11.916141836464673]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='BFC')

SlowDown = [65.612663670119218, 62.340771028037381, 48.514212328767123, 43.872933070866139, 54.530007530120479, 53.76351893095768, 44.550896421706341]
plt.plot(Flow_Size, SlowDown,  '-.', color='green', label='HPCC')

SlowDown = [102.05339083589405, 101.15580357142858, 73.936034482758615, 61.418912337662334, 51.953263157894739, 52.609372995509943, 48.73350513488657]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='DCQCN')

SlowDown = [1.8357190347686652, 7.93536036036036, 33.62179054054054, 46.5646408839779, 37.80108024691358, 17.576265450264863, 13.25542191992922]
plt.plot(Flow_Size, SlowDown, ':', color='black', label='IdealFQ')

#SlowDown = [4.9908333333333337, 4.942708333333333, 8.7454861111111111, 54.817959770114939, 73.351117886178855, 57.3434036939314, 48.290261809547616]
#plt.plot(Flow_Size, SlowDown, '-.', color='brown', label='HPCC+SFQ')

SlowDown = [85.374285714285719, 77.400877192982449, 60.229051724137932, 56.950907821229052, 62.861604361370716, 36.228673861620344, 25.960575391964724]
plt.plot(Flow_Size, SlowDown, '--', color='orange', label='DCTCP')

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
plt.legend(bbox_to_anchor=(-0.1, 1.02, 1.1, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(4,3))
plt.ylabel("FCT Slow Down", fontsize=17)
plt.xlabel("Flow Size (KB)", fontsize=17)
plt.xscale('log')
plt.yscale('log')
plt.gca().set_ylim(bottom=1)

#FB65

Flow_Size = [3,12,48,192,768,3072,12288]
SlowDown = [1.1479761904761905, 1.7425438596491227, 4.078298611111111, 6.254166666666666, 9.43569587628866, 10.530746336996337, 9.637086563307493]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='BFC')

SlowDown = [2.634918775382693, 2.6974299065420562, 3.2298013245033115, 4.0952674897119339, 16.330216881594374, 37.763711890243904, 35.777601135557134]
plt.plot(Flow_Size, SlowDown,  '-.', color='green', label='HPCC')

SlowDown = [4.5543899162320214, 4.5517523364485983, 4.2536458333333336, 4.3237664473684214, 5.1780400572246066, 16.866340152565879, 30.282063220310672]
plt.plot(Flow_Size, SlowDown, '--', color='red', label='DCQCN')

SlowDown = [1.1558371568705008, 1.792146017699115, 4.8103741496598635, 6.940213815789473, 10.565740740740742, 12.57158573596358, 12.158759736045003]
plt.plot(Flow_Size, SlowDown, ':', color='black', label='IdealFQ')

#SlowDown = [2.1066972042331384, 2.3795833333333332, 3.380536912751678, 4.2059834123222748, 18.442021276595746, 38.617090592334492, 36.913010301411674]
#plt.plot(Flow_Size, SlowDown, '-.', color='brown', label='HPCC+SFQ')

SlowDown = [3.4244465738423027, 3.5284722222222222, 3.7558277027027027, 4.2114718614718614, 8.2120098039215694, 14.97517523364486, 13.071036216085272]
plt.plot(Flow_Size, SlowDown, '--', color='orange', label='DCTCP')

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
plt.legend(bbox_to_anchor=(-0.1, 1.02, 1.1, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)
plt.tight_layout()

plt.figure(figsize=(4,3))
plt.ylabel("FCT Slow Down", fontsize=17)
plt.xlabel("Flow Size (KB)", fontsize=17)
plt.xscale('log')
plt.yscale('log')
plt.gca().set_ylim(bottom=1)

Flow_Size = [3,12,48,192,768,3072,12288]
SlowDown = [9.431223180189757, 11.410630841121495, 37.67939189189189, 42.98262614678899, 37.55050623052959, 16.928660669665167, 11.916141836464673]
plt.plot(Flow_Size, SlowDown, '-', color='blue', label='BFC')

#SlowDown = [37.339306872037916, 44.950000000000003, 24.021232876712329, 23.926445578231291, 32.546551724137935, 41.574526515151518, 35.05040255796834]
#plt.plot(Flow_Size, SlowDown, '--', color='red', label='HPCC+InfBuf')

SlowDown = [65.612663670119218, 62.340771028037381, 48.514212328767123, 43.872933070866139, 54.530007530120479, 53.76351893095768, 44.550896421706341]
plt.plot(Flow_Size, SlowDown,  '-.', color='green', label='HPCC+PFC')

SlowDown = [36.847081243335047, 45.123967889908258, 24.057619863013699, 24.06639344262295, 35.409131355932203, 42.810354573484069, 35.726523323615162]
plt.plot(Flow_Size, SlowDown, ':', color='black', label='HPCC+Retr.')
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
plt.legend(bbox_to_anchor=(-0.22, 1.02, 1.24, 1.02), loc=3, ncol=2, mode="expand", borderaxespad=0., prop={'size': 15}, frameon=False)
plt.tight_layout()

plt.show()