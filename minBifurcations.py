import matplotlib.pyplot as plt

#This program calculates the minimum number of bifurcations needed to reach ideal diffusion velocity in the lung. It does this by iterating diameter/velocity for a fractal landscape, using various tree exponents, until the peclet number is less than 1(indicating ideal oxygen diffusion is possible). 


finalIndex = 0
index = 0
finalDiameter = 0
initDiameter = 1.8 #in centimeters. Same trachea diameter used in the paper.
initVelocity = 51 #in cm/s. Also provided by the paper.
velRatio = 0

ductInfo = [[2.05,2.1,2.15,2.2,2.25,2.3,2.35,2.4,2.45,2.5,2.55,2.6,2.65,2.7,2.75,2.8,2.85,2.9,2.95,3.0],[],[],[]]
#Stores data on each fractal landscape:Tree diameter exponent, final # of bifurcations, final/init velocity ratio, and diameter of final generation. 


def duct(d, v, i, t): #Diameter, velocity, index, and (global) tree exponent are inputs. 
    global initDiameter
    global initVelocity 
    peclet = ((initDiameter*initVelocity)/0.24)*pow(2,((-i*(t-1))/t))  #Using D=0.24cm^2/s. 
    if peclet > 1:
        newD = pow(2,(-1/t))*d
        newV = pow(2,(-(t-2)/t))*v
        i += 1
        duct(newD,newV,i,t)
    else: #Exit condition of the function. Once peclet condition is met, breaks the loop and exports the relevant data. 
        global finalIndex
        global finalDiameter
        global velRatio
        finalIndex = i+1 #Records the final number of bifurcations needed after tree completes. Adds 1 to include generation 0. 
        velRatio = v/initVelocity
        finalDiameter = d



for treeExponent in ductInfo[0]: #Simulates the bronchial tree with each tree exponent, and stores the # of bifurcations, final velocity ratio, and final tube diameter. 
    duct(initDiameter,initVelocity,index,treeExponent)
    ductInfo[1].append(finalIndex)
    ductInfo[2].append(velRatio)
    ductInfo[3].append(finalDiameter)

print(ductInfo)

plt.subplot(2,2,1) #Plot for figure 2
plt.plot(ductInfo[0], ductInfo[1])
plt.grid(b=True, which='both', axis='both')
plt.title("Number of Bifurcations Needed for Optimal Diffusion Across Fractal Dimensions")
plt.ylabel("Minimum # of bifurcations for optimal diffusion")
plt.xlabel("Tree Diameter Exponent (fractal dimension)")

plt.subplot(2,2,2) #Plot for figure 3
plt.plot(ductInfo[0], ductInfo[2],)
plt.grid(b=True, which='both', axis='both')
plt.title("Final Reduction in Flow Velocity versus Fractal Dimension, with varied # of Bronchial Generations ")
plt.ylabel("Final Velocity / Initial Velocity")
plt.xlabel("Tree Diameter Exponent (fractal Dimension)")
plt.show()

plt.subplot(2,2,3)
plt.plot(ductInfo[3], ductInfo[3]) #Plot for figure 4
plt.grid(b=True, which='both', axis='both')
plt.title("Final Diameter of Bronchial Tube across Fractal Dimensions")
plt.xlabel("Tree Diameter Exponent (fractal dimension)")
plt.ylabel("Diameter of Final Tube Generation, cm")
plt.show()
