#Machine Problem 3 (Experimental Points)
import numpy as np
#Defining the Function
def MachineProblem3(matx):
    length = len(matx)
    for i in range(length):
        coefficients = np.polyfit(matx[:,0], matx[:,1], i)
        normy = np.linalg.norm(matx[:,1]-np.polyval(coefficients, matx[:,0]))
        vec = [i,normy]
        if i == 0: 
            vec1 = vec        
        elif vec1[1] >= vec[1]: 
            vec2 = vec[0]         
    #Getting the best fit Values
    coefficients = np.polyfit(matx[:,0], matx[:,1], vec2)
    print ('The Coefficient/s Are: ', coefficients)