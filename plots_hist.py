import numpy as np
import matplotlib.pyplot as plt
import sys

#skips first line as first line of input file is blank
file = open(sys.argv[1], 'r')
#file = open('Data 2 for GoL Equilibrate Time.txt', 'r')
data = file.readlines()[1:]
file.close()

Timedata = []




for line in data:
    if line.startswith ("t"):
        tokens = line.split(" ") # splits data into 5 seperates floats
        Timedata.append(float(tokens[2])) #creates Temperature data as a float
    else :
        pass
    

#plots various graphs with error bars: Average energy against Temperature, Average absolute Magnetisation against Temperature, Specific Heat Capacity against Temperature and Suseptability against Temperature

plt.hist(Timedata,bins = 50,density =True, fill=False,ec="r") 
plt.title(" Game of Life - Time Required to Equilibrate for Random Initial Conditions",fontsize=14, fontweight = 'bold')
plt.xlabel("Time to Steady State/Absorption (sweeps)",fontsize=12, fontweight = 'bold')
plt.ylabel("Probability",fontsize=12, fontweight = 'bold')
#plt.savefig("Intial Histogram.png")
plt.show() 
plt.close()
