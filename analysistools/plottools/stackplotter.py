from os import listdir
from os.path import isfile, join
import sys 
from root_pandas import read_root 
from pandas import  DataFrame, concat, Series 
import numpy as np
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
matplotlib.pyplot.hist

inputfilepath="rootfile_del"
filenameList = listdir(inputfilepath)
FullfileList = [join(inputfilepath,ifile) for ifile in filenameList]
#print FullfileList

'''
 tutorials: 

https://stackoverflow.com/questions/11328958/save-the-plots-into-a-pdf
https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.hist.html

https://stackoverflow.com/questions/50404913/how-to-change-the-color-palette-for-stackplot-matplotlib

draw error: https://stackoverflow.com/questions/12957582/plot-yerr-xerr-as-shaded-region-rather-than-error-bars
and 
https://stackoverflow.com/questions/35390276/how-to-add-error-bars-to-histogram-diagram-in-python/35390509

anf 
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

data = np.random.normal(size=10000)

# plt.hist gives you the entries, edges 
# and drawables we do not need the drawables:
entries, edges, _ = plt.hist(data, bins=25, range=[-5, 5])

# calculate bin centers
bin_centers = 0.5 * (edges[:-1] + edges[1:])

# draw errobars, use the sqrt error. You can use what you want there
# poissonian 1 sigma intervals would make more sense
plt.errorbar(bin_centers, entries, yerr=np.sqrt(entries), fmt='r.')

plt.show()


https://matplotlib.org/gallery/lines_bars_and_markers/errorbar_limits_simple.html#sphx-glr-gallery-lines-bars-and-markers-errorbar-limits-simple-py
https://matplotlib.org/1.2.1/examples/pylab_examples/errorbar_demo.html
https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/bar_stacked.html
https://www.w3resource.com/graphics/matplotlib/barchart/matplotlib-barchart-exercise-14.php

'''

df = [read_root(FullfileList[i],  't_dm_wenucr', columns="*") for i in range(len(FullfileList)) ]
#print len(df)
#print df[0]

names_ =  df[0].dtypes

variableNames = df[0].columns

eta_bins = np.linspace(-4.5, 4.5, 19)

print eta_bins

var0_0 = df[0][variableNames[0]]
var0_1 = df[1][variableNames[0]]
var0_2 = df[2][variableNames[0]]

weight_0 =  df[0]['weight']
weight_1 =  df[1]['weight']
weight_2 =  df[2]['weight']

p = plt.figure()
plt.hist([var0_0,var0_1,var0_2], eta_bins, weights=[weight_0, weight_1, weight_2], stacked=True, color=["red", "blue", "violet"]); plt.legend({"one": "red", "two": "blue", "three": "violet"}) 
plt.show()

p.savefig("foo.pdf", bbox_inches='tight')

#plt.hist([x1,x2,x3], bins, stacked=True, color=["red", "blue", "violet"], normed = True); plt.legend({label1: "red", label2: "blue", label3: "violet"}) 

#plt.stackplot(eta_bins, hist0, hist1, hist2) 
