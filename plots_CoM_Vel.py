import numpy as np
import matplotlib.pyplot as plt
import sys

#skips first line as first line of input file is blank
file = open(sys.argv[1], 'r')
data = file.readlines()[1:]
file.close()

Timedata = []
CoMxdata = []
CoMydata = []


for line in data:
    if line.startswith ("t"):
        tokens = line.split(" ") # splits data into 5 seperates floats
        Timedata.append(float(tokens[2])) #creates Temperature data as a float
        CoMxdata.append(float(tokens[3])) #creates Energy data as a float
        CoMydata.append(float(tokens[4]))
    else :
        pass
    
coeff, sqres, _, _, _ = np.polyfit(Timedata, CoMydata, 1, full=True)

plt.subplot(1,2,1)
axes = plt.gca()

axes.set_ylim([0,50])

plt.plot(Timedata[0:-1:10],CoMxdata[0:-1:10], 'c+',label = "X CoM") 
plt.plot(Timedata[0:-1:10],CoMydata[0:-1:10], 'r+',label = "Y CoM") 
#ax1.plot(fitx, fit, label='fit')
plt.suptitle(" Game of Life - CoM Against Time",fontsize=14, fontweight = 'bold')
plt.xlabel("Number of Sweeps",fontsize=12, fontweight = 'bold')
plt.ylabel("CoM position",fontsize=12, fontweight = 'bold')
plt.legend(loc = 0)
#plt.savefig(" Game of Life - Number of Active Sites Against Time.png")
#plt.show() 
#plt.close()



coeffx, sqresx, _, _, _ = np.polyfit(Timedata[93:273:10], CoMxdata[93:273:10], 1, full=True)
coeffy, sqresy, _, _, _ = np.polyfit(Timedata[93:273:10], CoMydata[93:273:10], 1, full=True)

fitx = np.linspace(112, 291, 1000)
fitCoMx = coeffx[0]*fitx+coeffx[1]
fitCoMy = coeffy[0]*fitx+coeffy[1]

plt.subplot(1,2,2)
axes.set_ylim([0,50])

plt.plot(Timedata[93:273:10],CoMxdata[93:273:10], 'c+',label = "X CoM") 
plt.plot(Timedata[93:273:10],CoMydata[93:273:10], 'r+',label = "Y CoM") 
plt.plot(fitx, fitCoMx, label='CoM x fit')
plt.plot(fitx, fitCoMy, label='CoM y fit')
#plt.title(" Game of Life - CoM Against Time",fontsize=14, fontweight = 'bold')
plt.xlabel("Number of Sweeps",fontsize=12, fontweight = 'bold')
#plt.ylabel("CoM position",fontsize=12, fontweight = 'bold')
plt.legend(loc = 0)
#plt.savefig(" Game of Life - Number of Active Sites Against Time.png")
plt.tight_layout()
plt.show() 
print("CoM x coefficients: ", coeffx)
print("For CoM x, sum of squared residuals =", sqresx[0])
print("CoM y coefficients: ", coeffy)
print("For CoM y, sum of squared residuals =", sqresy[0])
velocity = np.sqrt(coeffx[0]**2 + coeffy[0]**2)
print("The velocity of the glider is: " + str(velocity) + ' Lattice Points/Sweep')
plt.close()



