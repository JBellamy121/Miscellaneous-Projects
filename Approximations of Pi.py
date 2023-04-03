# -*- coding: utf-8 -*-
"""
Author: Jack Bellamy
Date: 3/04/23
Task: Pi Approximations
"""

#Modules Used
import math
import random

#Numerical integration of semi-circle function to approximate pi
def numericalIntegration():

    samples = 1000
    xDelta = 1 / samples
    x = 0
    
    yValues = []
    while x < 1:
        y = math.sqrt(1 - math.pow(x,2))
        yValues.append(y)
        x += xDelta
        
    areaSum = 0
    for i in range(1,len(yValues) - 1):
        areaSum += 2 * yValues[i]
         
    area = 2 * xDelta * (yValues[0] + yValues[len(yValues)-1] + areaSum)
    return area
        
    
#Chudnovsky algorithim approximation of Pi
def chudnovsky():
    
    samples = 16
    piApprox = 0
    
    for i in range(0,samples):
        
        chudNum = math.pow(-1,i) * math.factorial(6*i) * (13591409 + 545140134*i) #Numerator of Chudnovsky algorithim 
        chudDen = math.factorial(3*i) * math.pow(math.factorial(i),3) * math.pow(640320, (3*i)+(3/2)) #Denominator of Chudnovsky algorithim 
        piApprox += chudNum / chudDen
    
    piApprox = 1 / (12 * piApprox)
    return piApprox
        

#Calculating Pi through a numerical approximation of the arc length of a semi circle
def arcLength():
    
    samples = 10000
    
    x=-1
    xDelta = 2 / samples #Step size between samples
    
    points = [] #List of sample points
    while x <= 1:
        
        y = math.sqrt(1 - math.pow(x,2)) #Value of f(x) evaluated x = xA
        
        points.append([x,y]) #Appending point to points list
        x += xDelta
        
    arcLength = 0 #Arc length variable used in loop below
    for i in range(0,len(points) - 1):
        
        arcLength += math.dist(points[i],points[i+1]) #Adding distances between samples to calculate Arc Length   
    
    return arcLength

#Monte Carlo approximation of Pi
def monteCarlo():
    
    samples = 100000
    
    circleCount = 0
    squareCount = 0
    
    while circleCount + squareCount <= samples:
        
        x = random.random()
        y = random.random()
        
        if math.dist([x,y],[0,0]) <= 1:
            circleCount += 1
        
        squareCount += 1
          
    piApprox = (circleCount / squareCount) * 4
    return piApprox
