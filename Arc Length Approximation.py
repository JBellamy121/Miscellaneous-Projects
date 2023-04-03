# -*- coding: utf-8 -*-
"""
Author: Jack Bellamy
Date: 3/04/23
Task: Arc Length Approximation
"""

#Modules Used
import math
import matplotlib.pyplot as plt


def arcApprox():
    
    sampleMax = 100000
    
    arcLengths = []
    for i in range(2,sampleMax):
        
        length = arcLength(i)
        arcLengths.append(length)
    
    # print(arcLengths)
    arcDifference = []
    xAxis = []
    finalLength = arcLengths[len(arcLengths)-1]
    
    for j in range(0,len(arcLengths)):
        
        diff = abs(finalLength - arcLengths[j]) / finalLength
        arcDifference.append(diff)
        xAxis.append(j)
    
    #Plot of percentage error
    plt.plot(xAxis,arcDifference)
    plt.grid()
    plt.title("Percentage Error as sample amount approachs 'sampleMax'")
    
    print('Final Arc Length Approximation: ',str(round(finalLength,6)))
    
    
#Function calculates Arc Length of curve defined in function 'fx()'
def arcLength(samples):
    
    xA = -1 #Initial point of arc 
    xB = 1 #End point of arc 
    xDelta = abs(xB - xA) / samples #Step size between samples
    
    points = [] #List of sample points
    while xA < xB:
        
        y = fx(xA) #Value of f(x) evaluated x = xA
        
        points.append([xA,y]) #Appending point to points list
        xA += xDelta
        
    arcLength = 0 #Arc length variable used in loop below
    for i in range(0,len(points) - 1):
        
        arcLength += dist(points[i],points[i+1]) #Adding distances between samples to calculate Arc Length   
    
    # print(arcLength) #Prints the arc Length estimated to user
    return arcLength
    

#The curve that will have its arc length approximated
def fx(x):
    
    y = math.sqrt(1 - math.pow(x,2)) #The curve/function 
    return y


#Calculates distance between point 'p1' and 'p2'
def dist(p1,p2):
    
    x0 = p1[0] ; y0 = p1[1]
    x1 = p2[0] ; y1 = p2[1]
    
    distance = math.sqrt((math.pow(x1 - x0,2) + math.pow(y1 - y0,2)))
    return distance