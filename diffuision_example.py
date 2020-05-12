"""Create sequence of random numbers and plot with matplotlib.pyplot

Instructions:  to get true random numbers, you should import "numpy",
a number-crunching package on which visual is based.  Numpy has several
subpackages including "linalg" for doing linear algebra and "random"
for doing random number generation. To access high quality random
numbers you want to add
   import numpy.random

Here I am only using uniform float random numbers on the interval [0,1),
so I only import the routine "random_sample"  It can be used to generate
a single random number or a whole series of them.

Antonio Cancio
Phys 336/536
March 17, 2020
"""
import numpy
import matplotlib.pyplot as plt
from numpy.random import random_sample

pointTarget = 1000

# Doing this one step at a time would be slow, but possible
print("Scalar method of generating random number sequence")
print("Uniform distribution")

integerList = []
randomNumberList = []
for i in range(pointTarget):
    x = random_sample()
    integerList.append(i)
    randomNumberList.append(x)
    #print (i, x)

plt.plot(integerList, randomNumberList, color="red", label="list", linestyle="None", marker=".")

# generate sequence that is pointTarget long and store in an array
print("Array method of generating random number sequence")
print("Uniform distribution")

integerArray = numpy.arange(0, pointTarget, 1)
randomNumberArray = random_sample(pointTarget)

plt.plot(integerArray, randomNumberArray, color="blue", label="array", linestyle="None", marker="x")

plt.xlabel("i")
plt.xlabel("Number")
plt.legend()
plt.show()

######## Playing around -- delete for lab
#second_plot = gdisplay(xtitle='x_i+1',
#                       ytitle='x_i',
#                       width=500, height=500)
#crazy_correlations = gdots(color=color.green)
#
#for i in range(pointTarget-1):
#    rate(10000)
#    #print(randomNumberArray[i], randomNumberArray[i+1])
#    crazy_correlations.plot( pos=(randomNumberArray[i], randomNumberArray[i+1]) )
#
#print (numpy.average(randomNumberArray))
#print (numpy.var(randomNumberArray))
