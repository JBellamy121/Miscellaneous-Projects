# -*- coding: utf-8 -*-
"""
Author: Jack Bellamy
Date: 31/03/23
Task: Weierstrass Function
"""

#Modules used
import math
import matplotlib.pyplot as plt


#Generates graph of Weierstrass Function
def weierstrass():
    
    sumMax = 30 #Maximum interations of weierstrass fourier function
    sums = 0 #Inital variable for outer most loop below
    
    sampleStart = -1 #Minimum x value of weierstrass function plot
    sampleEnd = 1 #Maximum x value of weierstrass function plot
    sampleSteps = 500 #How many steps between sampleStart and sampleEnd for inner most loop below
    stepSize = abs(sampleEnd - sampleStart) / sampleSteps #Calculate delta x
    
    # 'b' has to be an odd integer, 0 < a < 1, and a * b > 5.72
    a = 0.75 #Parameter for Weierstrass Function below
    b = 13 #Parameter for Weierstrass Function below   
    
    if a * b < 5.72 or a < 0 or a > 1: #Check if paramters are within allowed range
        print("Values for 'a' and 'b' are invalid")
        
    else: #If parameters are within allowed range
        xCoords = [] #List of x-ordinates of weierstrass function
        yCoords = [] #List of y-ordinates of weierstrass function
        
        while sums < sumMax: #Loop of interation amount of Weierstrass function
            x = sampleStart #x value of weierstrass function
            pos = 0 #Variable to track list position
            while x < sampleEnd: #Loop of calculating W(x) from x = sampleStart to x = sampleEnd, with a delta of stepSize
                
                fx = (a**sums) * math.cos((b**sums)  * math.pi * x) #Weierstrass Function    
                
                if sums == 0: #If first interation through loop
                    xCoords.append(x)
                    yCoords.append(fx)
                else: #If not first interation through loop
                    yCoords[pos] += fx
            
                pos += 1 #Variable to track list position
                x += stepSize #delta x
                
            sums += 1 #Variable for interation amount
            

        ##Display graph of points generated  
        plt.plot(xCoords,yCoords,linewidth = 0.7)
        plt.title('Weierstrass Function, a='+str(a)+', b='+str(b))
    
    
#Function evaluates Weierstrass function at x, with parameter a and b, a*b > 5.72
def W(x,a,b):

    if a * b < 5.72 or a < 0 or a > 1: #Check if paramters are within allowed range
        print("Values for 'a' and 'b' are invalid")
        
    else: #If paramters are within allowed range
        sumMax = 150 #How many interations of weierstrass fourier summation, if set too high can cause errors
        sums = 0 #Initial amount for loop below, and variable for interation amount
        
        result = 0 #Variable to store the result of W(x)
        results = [] #List of cummaltive results for plotting
        interations = [] #List of interation amounts for plotting
        
        while sums < sumMax: #Loop to calculate W(x)

            #Weierstrass Fourier Summation
            fx = (a**sums) * math.cos(math.pow(b,sums) * math.pi * x)
            
            result += fx #Creating W(x) from many interations of function
            results.append(result) #Appending to list for plotting
            interations.append(sums) #Appending to list for plotting
                
            sums += 1 #Variable for interation amount
            
        print('Final result: '+str(round(result,6)))
        
        ##Plot of W(xn) result approaching 'true' value of W(x)
        # plt.plot(interations,results)
        # plt.grid()
        # plt.title('Weierstrass result at x='+str(x)+', as sums of W('+str(x)+') approachs '+str(sumMax))    
    