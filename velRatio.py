import matplotlib.pyplot as plt

bifurcationLimit = 14
index = 0
bifurcationInfo = [[],[],[]] #List that stores index, diameter, and velocity for every bifurcation index. Rewitten every iteration of duct. 
finalDiameter = 0
finalVelocity = 0

def duct(d, v, i, t): #Diameter, velocity, index, and (global) tree exponent are inputs. 
    global bifurcationLimit
    newD = pow(2,(-1/t))*d
    newV = pow(2,(-(t-2)/t))*v

    if i < bifurcationLimit: #Checks if the tree has hit generation 14. Records index, velocity, and diameter for each generation. 
        if i not in bifurcationInfo[0]:
            bifurcationInfo[0].append(i)
            bifurcationInfo[1].append(newD)
            bifurcationInfo[2].append(newV)
        i += 1
        duct(newD, newV, i, t)
    else: #Exit condition for function loop. Once 14 generations reached, final diameter and velocity are exported. 
        global finalDiameter
        global finalVelocity
        finalDiameter = d
        finalVelocity = v

initDiameter = 1.8 #in centimeters. Same trachea diameter used in the paper. 
initVelocity = 51 #in cm/s. Also provided by the paper. 

multiDucts = [[2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0],[]] 
#Stores final vfinal/vinit ratio for each value of t

for treeExponent in multiDucts[0]: #Simulates a bronchial tree for each tree exponent, and records the velocity ratio.
    duct(initDiameter,initVelocity,index,treeExponent)
    multiDucts[1].append((finalVelocity/initVelocity))

print(multiDucts)



plt.plot(multiDucts[0], multiDucts[1]) #Matplotlib plot information. 
plt.title("Final Reduction in Flow Velocity versus Fractal Dimension of Bronchial Tree")
plt.grid(b=True, which='both', axis='both')
plt.ylabel("Final Velocity/Initial Velocity")
plt.xlabel("Tree Diameter Exponent")
plt.show()
