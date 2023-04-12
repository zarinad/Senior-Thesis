"""
This program is free software. You can use, copy, distribute, modify and/or redistribute
it under the terms of the MIT/Expat License. See the file LICENSE for more details.
(c) 2021 Sandro Sousa
Citation:
S. Sousa, V. Nicosia
"Quantifying ethnic segregation in cities through random walks"

-----------------------------------------------------------------------------
The Class Coverage Time (CCT) is the expected number of steps required by a random 
walk to visit a certain fraction c of all the classes present in the system 
when starting from a generic node.

Compute the CCT as a function of c fractions of classes
Values correspond to the number of unique classes seen
at time t averaged over <num> iterations. The time series Y(t) shows
the time evolution of the classes seen for each node.
<edges> reported as DIRECTED, no self-loops, no multiple edges.
<prop> count of each group per area, at MxC matrix format
<num> number of walk repetitions for computing the average for each node
<idx> range of nodes or single id to compute, e.g.: 1, 0-10

> output:
    node
    list: [avg trajectory (n classes seen) at each fraction c]
-----------------------------------------------------------------------------
"""

#%%
#Import necessary packages
import numpy as np
import random
from itertools import zip_longest
import sys
from sys import exit


#%%
#This ensures that you add the correct arguments when running the file. 
#It needs at least 6 (wdir, <edges>, <prop>, <num>. <idx>, \n)
#Will throw an error if missing information
if len(sys.argv) < 5:
    print("Usage: %s <edges> <prop> <num> <idx> \n" % sys.argv[0])
    exit(1)


#This creates a dictionary with neighbors for a given node i
def compute_neighbours(edges):
    E = dict()
    for i, j in edges:
        if i in E:
            E[i].append(j)
        else:
            E[i] = [j]
    return E

#Creating ethnicity count
def fill_empty_classes(i, idxs):
    #Find ethnicities not represented in city, update with 1
    obs = classes[i]
    for n in idxs:
        # set group count to 1
        obs[n] = 1
    return obs


#Creating the walk function
def walk(i, obs):
    nc = []  #Number of classes seen on the walk
    while 0 in obs:
        #Selects one of i's neighbours at random
        j = random.choice(neigh_dict[i])
        obs = obs + classes[j]
        #Get the current number of classes seen
        non_z = int(np.count_nonzero(obs) - len(idxs))
        nc.append(non_z)
        i = j
    return nc #Returns the number of classes seen on the walk


# %%
#Initialize dictionary with neighbours
neigh_dict = compute_neighbours(np.loadtxt(sys.argv[1], dtype='int'))

#Load population data and set variables
prop = np.loadtxt(sys.argv[2], dtype='int')
classes = prop[:, 1:]

#Total number of classes at the city level:
classes_sum = classes.sum(axis=0)
#Total number of classes in the system:
C = (classes_sum >= 1).sum()

#Index of missing groups at the city level
idxs = np.where(classes_sum == 0)[0]

#Process range or single node from parameter
if "-" in sys.argv[4]:
    start, end = [int(x) for x in sys.argv[4].split('-')]
else:
    start, end = [int(sys.argv[4]), int(sys.argv[4])+1]
num = int(sys.argv[3])

avg_array = []

#Loop over all nodes given in the initial input
for node in range(start, end):
    #Fill empty classes
    if len(idxs) > 0:
        obs = fill_empty_classes(node, idxs)
    else:
        obs = classes[node]
    avg_series = []
    #Repeat "num" iterations for each node
    for n in range(num):
        series = walk(node, obs)
        #Check if is first trajectory
        if len(avg_series) == 0:
            avg_series = series
            continue
        len_avg = len(avg_series)
        len_sr = len(series)
        #Concatenate series with avg and fill missing values
        if len_avg < len_sr:
            summed = [sum(x) for x in zip_longest(avg_series, series, fillvalue=C*n)]
        elif len_avg > len_sr:
            summed = [sum(x) for x in zip_longest(avg_series, series, fillvalue=C)]
        else:
            summed = [sum(x) for x in zip(avg_series, series)]
        #Update avg_series with trajectories summed
        avg_series = summed

    #Compute the average over all trajectories
    #Time until it overtakes a certain threshhold
    avg_series = [nc/num for nc in avg_series]
     #print("Length of Average Series:" , len(avg_series))
    #Compute the avg time to find each ratio of classes in [0,1]
    th_values = []
    for t in range(1, 101):
        #th = int(np.ceil((t*C)/100))
        th = (t*C) // 100  # threshold value
        time = 0
        # check only series w/ first elem > th
        for s in avg_series:
            if s >= th:
                time += 1
                break
            else:
                time += 1
        # time for each th per node (series)
        th_values.append(time)
    # dump node id and class coverage profile (time for each fraction)
    #Number of steps needed to see threshold values
    print("Node:", node, "Threshold values:", *th_values)
    avg_array.append(th_values)
avg_array=np.asarray(avg_array)
np.set_printoptions(suppress=True)
print("Average of all nodes", np.average(avg_array, axis=0))
