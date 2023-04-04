# -*- coding: utf-8 -*-
"""
Author: Jack Bellamy
Date: 5/04/23
Task: Pi Approximations
"""

#Modules Used
import math
import random
import time
import matplotlib.pyplot as plt
import itertools


#Compare each approximation based on time and accuracy, then present graphs of results, and print which method is 'best' overall
def approxComparison():
    
    #Running approximation functions, generating time to run and pi approximation
    timeNewton = time.time()
    newtonResult = round(newton(),15)
    timeNewton = time.time() - timeNewton
    
    timeGauss = time.time()
    gaussResult = round(gauss(),15)
    timeGauss = time.time() - timeGauss
    
    timeLeibniz = time.time()
    leibnizResult = round(leibniz(),15)
    timeLeibniz = time.time() - timeLeibniz
    
    timeNumericalIntegration = time.time()
    numericalIntegrationResult = round(numericalIntegration(),15)
    timeNumericalIntegration = time.time() - timeNumericalIntegration
    
    timeChudnovsky = time.time()
    chudnovskyResult = round(chudnovsky(),15)
    timeChudnovsky = time.time() - timeChudnovsky
    
    timeArcLength = time.time()
    arcLengthResult = round(arcLength(),15)
    timeArcLength = time.time() - timeArcLength
    
    timeMonteCarlo = time.time()
    monteCarloResult = round(monteCarlo(),15)
    timeMonteCarlo = time.time() - timeMonteCarlo
    
    #Collation of Results
    times = [timeNewton,timeGauss,timeLeibniz,timeNumericalIntegration,timeChudnovsky,timeArcLength,timeMonteCarlo]
    approxs = [newtonResult,gaussResult,leibnizResult,numericalIntegrationResult,chudnovskyResult,arcLengthResult,monteCarloResult]
    names = ['Newton','Gauss','Leibniz','Numerical Integration','Chudnovsky','Arc Length','Monte Carlo']
    
    #Calculation of percent error of each approximation
    approxDiff = []
    Pi = 3.14159265358979323
    for i in range(0,len(approxs)):
        diff = (abs(Pi - approxs[i]) / Pi) * 100
        approxDiff.append(diff)
    
    
    #Time Graph
    plt.bar(names,times)
    plt.xticks(rotation=45, ha='right')
    plt.title('Times of Each Approximation')
    plt.ylabel('Run time')
    plt.xlabel('Method of Approximation')
    plt.grid()
    plt.show()
    plt.clf()
    
    #Accuracy Graph
    plt.bar(names,approxDiff)
    plt.xticks(rotation=45, ha='right')
    plt.title('Percent Error of each Approximation')
    plt.ylabel('Percent Error')
    plt.xlabel('Method of Approximation')
    plt.grid()
    plt.show()
    
    
    #Ranking Logic
    ranks = []
    rankTime = [] ; rankApprox = []
    timeNames = names.copy() ; approxNames = names.copy()
    for i in range(0,len(names)):
        
        ranks.append([names[i]])
        
        bestTime = min(times)
        bestTimeMethod = timeNames[times.index(bestTime)]
        rankTime.append([bestTimeMethod,bestTime])
        times.pop(times.index(bestTime))
        timeNames.remove(bestTimeMethod)
        
        bestApprox = min(approxDiff)
        bestApproxMethod = approxNames[approxDiff.index(bestApprox)]
        rankApprox.append([bestApproxMethod,bestApprox])
        approxDiff.pop(approxDiff.index(bestApprox))
        approxNames.remove(bestApproxMethod)
        
    rankList = [rankTime,rankApprox]    
    for i in range(0,2):
        for j in range(0,len(rankList[0])):
            name = rankList[i][j][0]
            for k in range(0,len(ranks)):
                if name == ranks[k][0]:
                    if i == 0:
                        ranks[k].append(j+1)
                    else:
                        ranks[k][1] += j+1
    
    rankName = []
    rankValue = []
    for i in range(0,len(ranks)):
        rankName.append(ranks[i][0])
        rankValue.append(ranks[i][1])
        
    bestMethod = min(rankValue)
    bestName = rankName[rankValue.index(bestMethod)]
    
    
    print('---------------------------')
    print('Best Method:',bestName)
    print('Rank List:',ranks)
    

###############################################################################
#####################   Methods of Approximation   ############################
###############################################################################
    

#Newton / Euler Convergence Transformation
def newton():

    samples = 50
    
    newtonSum = 0
    for i in range(0,samples):
        newtonSum += math.factorial(i) / doublefactorial((2*i)+1)
        
    newtonSum = newtonSum * 2
    return newtonSum

#Used in newton() function
def doublefactorial(n):
     if n <= 0:
         return 1
     else:
         return n * doublefactorial(n-2)


#Gauss–Legendre algorithm to approximate Pi
def gauss():
    
    samples = 3
    
    #Initial condition parameters for algorithim
    a0 = 1
    b0 = 1 / math.sqrt(2)
    t0 = 1 / 4
    p0 = 1
    
    ints = 0
    while ints < samples:
        #
        an = (a0 + b0) / 2
        bn = math.sqrt(a0 * b0)
        tn = t0 - (p0 * math.pow(a0 - an,2))
        pn = 2 * p0
        #Update initial variables
        a0 = an ; b0 = bn ; t0 = tn ; pn = p0
        
        ints += 1
        
    piApprox = math.pow(a0 + b0,2) / (4 * t0)
    return piApprox
        

#Leibniz algorithm to approximate Pi
def leibniz():
    
    samples = 40000000
    
    leibnizSum = 0
    for i in range(0,samples):
        
        term = 1 / ((2 * i) + 1)
        
        if i % 2 == 0:
            leibnizSum += term
        else:
            leibnizSum -= term
      
    leibnizSum = 4 * leibnizSum
    return leibnizSum


#Numerical integration of semi-circle function to approximate pi
def numericalIntegration():

    samples = 10000000
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
    
    samples = 2
    piApprox = 0
    
    for i in range(0,samples):
        
        chudNum = math.pow(-1,i) * math.factorial(6*i) * (13591409 + 545140134*i) #Numerator of Chudnovsky algorithim 
        chudDen = math.factorial(3*i) * math.pow(math.factorial(i),3) * math.pow(640320, (3*i)+(3/2)) #Denominator of Chudnovsky algorithim 
        piApprox += chudNum / chudDen
    
    piApprox = 1 / (12 * piApprox)
    return piApprox
        

#Calculating Pi through a numerical approximation of the arc length of a semi circle
def arcLength():
    
    samples = 1000000
    
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
    
    samples = 10000000
    
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
