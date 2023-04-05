# -*- coding: utf-8 -*-
"""
Author: Jack Bellamy
Date: 5/04/23
Task: Arc Length Approximation
"""

#Modules Used
import math
import matplotlib.pyplot as plt
import time
import scipy.integrate as integrate



#Comparison of Methods used to generate arc length of a function
def approxComparison():
    
    firstTime = []
    secondTime = []
    firstResult = []
    secondResult = []
    xAxis = []
    
    intervals = [10*2**i for i in range(1,17)] #Generate logarithmically spaced points
    for i in range(0,len(intervals)):
        
        sampleSize = intervals[i] #Choose sample amount from list
        
        #Statisitics for first method: arcLengthDistance()
        timeFirst = time.time()
        resultFirst = arcLengthDistance(sampleSize)
        timeFirst = time.time() - timeFirst
        #Statisitics for second method: arcLengthIntegral()
        timeSecond = time.time()
        resultSecond = arcLengthIntegral(sampleSize)
        timeSecond = time.time() - timeSecond
        #Appending results to respective lists
        firstTime.append(timeFirst)
        secondTime.append(timeSecond)  
        firstResult.append(resultFirst)
        secondResult.append(resultSecond)
        xAxis.append(sampleSize)

    #Plotting for time results of two methods
    plt.plot(xAxis,firstTime,c='blue',label='Distance Method')
    plt.plot(xAxis,secondTime,c='red',label='Integral Method')
    plt.title('Times of First Method')
    plt.grid()
    plt.legend()
    plt.show()
    plt.clf()

    #Plotting for arc length result of two methods
    plt.plot(xAxis,firstResult,c='blue',label='Distance Method')
    plt.plot(xAxis,secondResult,c='red',label='Integral Method')
    plt.title('Results of First Method')
    plt.grid()
    plt.legend()
    plt.show()


##########################################################################################
##########################################################################################
##########################################################################################

#Function calculates Arc Length of curve defined in function 'fx()'
def arcLengthDistance(samples):
    
    xA = 0 #Initial point of arc 
    xB = 100 #End point of arc 
    xDelta = abs(xB - xA) / samples #Step size between samples
    
    points = [] #List of sample points
    while xA < xB:
        
        y = fx(xA) #Value of f(x) evaluated x = xA
        
        points.append([xA,y]) #Appending point to points list
        xA += xDelta
        
    arcLength = 0 #Arc length variable used in loop below
    for i in range(0,len(points) - 1):
        
        arcLength += math.dist(points[i],points[i+1]) #Adding distances between samples to calculate Arc Length   
    
    # print(arcLength) #Prints the arc Length estimated to user
    return arcLength


###################

#Function calculates arc length using numerical integration.
def arcLengthIntegral(samples):

    x = 0 #Initial point of arc 
    xB = 100 #End point of arc 
    xDelta = abs(xB - x) / samples #Step size between samples
    
    yValues = []
    while x < xB:

        y = math.sqrt(1 + math.pow(dfx(x),2))       
        yValues.append(y)
        x += xDelta
        
    areaSum = 0
    for i in range(1,len(yValues) - 1):
        areaSum += 2 * yValues[i]
         
    area = 0.5 * xDelta * (yValues[0] + yValues[len(yValues)-1] + areaSum)
    return area 


#Function calculates arc length using numerical integration.
def arcLengthIntegral2():

    xA = 0 #Initial point of arc 
    xB = 100 #End point of arc 

    integral = integrate.quad(arcFunc,xA,xB)
    
    print(integral[0])
    
#Formula for arc length
def arcFunc(x):   
    
    L = math.sqrt(1 + math.pow(dfx(x),2))
    return L

##########################################################################################
##########################################################################################
##########################################################################################

#The curve that will have its arc length approximated
def fx(x):
    
    y = math.sqrt(15*x) * ((math.pow(x,2)*math.cos(x))/math.exp(x))
    return y

#Derivative of fx()
def dfx(x):
    
    dy1 = -0.5 
    dy2 = ((math.sqrt(15)*(x**3/2)*math.exp(-x)))  
    dy3 = ((2*x*math.sin(x)) + ((2*x - 5)*(math.cos(x))))
    dy = dy1 * (dy2 * dy3)
    return dy
