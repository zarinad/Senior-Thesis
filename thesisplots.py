"""
Created on Thu Mar 23 11:34:39 2023

@author: Zarina Dhillon
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
#%%
la_data=np.asarray([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1.1,	1.1,	1.1,	1.2,	1.2,	1.2,	1.2,	1.3,	1.5,	1.5,	1.6,	1.9,	1.9,	2.2,	2.6,	2.6,	3.2,	3.2,	3.8,	4.6,	4.6,	5.6,	6.7,	6.7,	8,	9.5,	9.5,	11.2,	13.2,	13.2,	15.4,	15.4,	17.9,	20.9,	20.9,	24.2,	28,	28,	32.3,	37.3,	37.3, 43.1,	43.1,	49.9,	57.8,	57.8,	67.3,	78.5,	78.5,	92.1,	108.6,	108.6,	128.4,	152.9,	152.9,	183.4,	183.4,	221.6,	268.9,	268.9,	328.5,	402.8,	402.8,	497.2,	615.3,	615.3,	766,	766,	963,	1224.1,	1224.1,	1585.3,	2124.7,	2124.7,	2958.9,	4393.7,	4393.7,	7411.8, 	28068.2])
null_data=np.asarray([1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1.09,	1.09,	1.1,	1.17,	1.17,	1.22,	1.4,	1.4,	1.6,	1.81,	1.81,	2.19,	2.19,	2.64,	3.22,	3.22,	3.94,	4.81,	4.81,	5.84,	7.04,	7.04,	8.41,	10,	10,	11.86,	11.86,	13.96,	16.35,	16.35,	19.12,	22.28,	22.28,	25.89,	30.21,	30.21,	35.09,	34.09,	40.82,	47.63,	47.63,	55.88,	65.81,	65.81,	77.8,	92.6,	92.6,	111.07,	134.23,	134.23,	163.4,	163.4,	200.91,	249.17,	249.17,	310.53,	388.36,	388.36,	487.1,	613.86,	613.86,	773.84,	773.84,	980.31,	1246.27,	1246.27,	1599.03,	2089.72,	2089.72,	2784.13,	3882.67,	3882.67,	5960.92,	12802.76])
difference_la_null=np.asarray([0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.1,	0.1,	0.1,	0.2,	0.2,	0.11,	0.11,	0.2,	0.33,	0.33,	0.38,	0.5,	0.5,	0.6,	0.79,	0.79,	1.01,	1.01,	1.16,	1.38,	1.38,	1.66,	1.89,	1.89,	2.16,	2.46,	2.46,	2.79,	3.2,	3.2,	3.54,	3.54,	3.94,	4.55,	4.55,	5.08,	5.72,	5.72,	6.41,	7.09,	7.09,	8.01,	9.01,	9.08,	10.17,	10.17,	11.42,	12.69,	12.69,	14.3,	16,	16,	17.33,	18.67,	18.67,	20,	20,	20.69,	19.73,	19.73,	17.97,	14.44,	14.44,	10.1,	1.44,	1.44,	7.84,	7.84,	17.31,	22.17,	22.17,	13.73,	34.98,	34.98,	174.77,	511.03,	511.03,	1450.88,	15265.44])
difference_subnulls=np.asarray([0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0.02,	0.02,	0,	0.04666666667,	0.04666666667,	0.03555555556,	0,	0,	0,	0.02,	0.02,	0.02,	0.02,	0.05333333333,	0.03555555556,	0.03555555556,	0.07555555556,	0.08222222222,	0.08222222222,	0.07555555556,	0.09333333333,	0.09333333333,	0.1133333333,	0.1022222222,	0.1022222222,	0.09333333333,	0.09333333333,	0.1066666667,	0.1444444444,	0.1444444444,	0.1644444444,	0.2222222222,	0.2222222222,	0.2422222222,	0.3088888889,	0.3088888889,	0.3666666667,	2.308888889,	0.4177777778,	0.5,	0.5,	0.68,	0.8244444444,	0.8244444444,	1.111111111,	1.56,	1.56,	2.393333333,	3.086666667,	3.086666667,	3.804444444,	3.804444444,	5.522222222,	7.477777778,	7.477777778,	11.26888889,	15.67555556,	15.67555556,	22.49333333,	33.48888889,	33.48888889,	45.10222222,	45.10222222,	62.18,	87.32666667,	87.32666667,	117.3888889,	166.1422222,	166.1422222,	230.9888889,	345.0688889,	345.0688889,	542.1733333,	1920.213333])
#%%
# ORIGINAL PLOT
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
})
fig, ax=plt.subplots()
plt.ylim()
plt.xlim()
ax.plot(la_data, marker='.', label='Los Angeles', color='C9')
ax.plot(null_data, marker='.', label='Null Model', color='C3')
ax.legend(loc='upper left')
ax.set_xlabel('Percent of Classes seen')
ax.set_ylabel('Time (number of steps)')
plt.savefig('og_thesis_plot.png', dpi=600)
plt.show()
#%%
## EARLY ZOOMED IN PLOT
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
})
fig, ax=plt.subplots()
plt.ylim(0, 15)
plt.xlim(30, 50)
ax.plot(la_data, marker='.', label='Los Angeles', color='C9')
ax.plot(null_data, marker='.', label='Null Model', color='C3')
ax.legend(loc='upper left')
ax.set_xlabel('Percent of Classes seen')
ax.set_ylabel('Time (number of steps)')
plt.savefig('early_zoom_thesis_plot.png', dpi=600)
plt.show()
#%%
## LATE ZOOMED IN PLOT
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
})
fig, ax=plt.subplots()
plt.ylim(2000, 30000)
plt.xlim(95, 99)
ax.plot(la_data, marker='.', label='Los Angeles', color='C9')
ax.plot(null_data, marker='.', label='Null Model', color='C3')
ax.legend(loc='upper left')
ax.set_xlabel('Percent of Classes seen')
ax.set_ylabel('Time (number of steps)')
plt.savefig('zoom_thesis_plot.png', dpi=600)
plt.show()
#%%
## TIME BOUNDED ZOOMED IN PLOT
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
})
fig, ax=plt.subplots()
plt.ylim(2750, 4500)
plt.xlim(95, 97)
ax.plot(la_data, marker='.', label='Los Angeles', color='C9')
ax.plot(null_data, marker='.', label='Null Model', color='C3')
ax.legend(loc='upper left')
ax.set_xlabel('Percent of Classes seen')
ax.set_ylabel('Time (number of steps)')
plt.savefig('zoom_zoom_thesis_plot.png', dpi=600)
plt.show()
#%%
## LOG PLOT
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
})
fig, ax=plt.subplots()
plt.ylim()
plt.xlim()
ax.plot(np.log(la_data), marker='.', label='Los Angeles', color='C9')
ax.plot(np.log(null_data), marker='.', label='Null Model', color='C3')
ax.legend(loc='upper left')
ax.set_xlabel('Percent of Classes seen')
ax.set_ylabel('Log(Time)')
plt.savefig('log_thesis_plot.png', dpi=600)
plt.show()
#%%
# DIFFERENCE PLOT
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
})
fig, ax=plt.subplots()
plt.ylim()
plt.xlim()
ax.plot(np.log(difference_la_null), marker='.', label='Difference between LA County and null model', color='black')
ax.plot(np.log(difference_subnulls), marker='.', label='Average difference between sub-null models', color='grey')
ax.legend(loc='upper left')
ax.set_xlabel('Percent of Classes seen')
ax.set_ylabel('Log(Time)')
plt.savefig('diffs_log_thesis_plot.png', dpi=600)
plt.show()
invalid=np.where(difference_subnulls==0)
print(invalid)
#%%
## BOX PLOT
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
})
fig, ax=plt.subplots()
plt.ylim(9, 16)
plt.xlim(48.5, 51.5)
#ten_null_50=np.asarray([10, 10, 10, 9.8, 9.9, 10.1, 10.1, 10, 10, 10.1])
ax.plot(la_data, marker='.', label='Los Angeles', color='C9')
ax.plot(null_data, marker='.', label='Null Model', color='C3')
ax.axhspan(9.8, 10.1, xmin=0.156, xmax=0.51, alpha=0.1, color='C3')
ax.axhspan(11.7, 12, xmin=0.824, alpha=0.1, color='C3')
ax.legend(loc='upper left')
ax.set_xlabel('Percent of Classes seen')
ax.set_ylabel('Time (number of steps)')
plt.savefig('range_shaded_thesis_plot.png', dpi=600)
plt.show()
# print(la_data[50])
# print(null_data[50])
#10 sub-null models at [50]=[10, 10, 10, 9.8, 9.9, 10.1, 10.1, 10, 10, 10.1]
#%%
## DIFFERENCE BOX PLOT
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
})
fig, ax=plt.subplots()
plt.ylim()
plt.xlim(97, 99)
#ten_null_50=np.asarray([10, 10, 10, 9.8, 9.9, 10.1, 10.1, 10, 10, 10.1])
ax.plot(difference_la_null, marker='.', label='Difference between LA County and null model', color='black')
ax.plot(difference_subnulls, marker='.', label='Average difference between sub-null models', color='grey')
ax.axhspan(7.9, 867.3, xmin=0.45, xmax=0.55, alpha=0.1, color='grey')
ax.legend(loc='upper left')
ax.set_xlabel('Percent of Classes seen')
ax.set_ylabel('Log(Time) (number of steps)')
#plt.savefig('range_shaded_thesis_plot.png', dpi=600)
plt.show()
#%%
##SPATIAL HETEROGENIETY
sum_diff=abs(np.subtract(la_data, null_data))
sum_diff=np.sum(sum_diff)
sum_diff=sum_diff/100
print("Sum of difference between LA and null:", sum_diff)