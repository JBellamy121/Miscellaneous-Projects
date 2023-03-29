# -*- coding: utf-8 -*-
"""
Author: Jack Bellamy
Date: 29/03/23
Task: Custom Statistic Functions
"""

#Modules Used
import random
import statistics

#Test data sets
xData = [5, 1, 8, 4, 7, 0, 0, 4, 5, 2, 6, 2, 10, 1, 10, 8, 2, 4, 8, 1, 2, 5, 6, 10, 5, 7, 9, 0, 10, 0, 3, 7, 6, 5, 9, 6, 4, 5, 3, 6, 10, 10, 8, 2, 4, 1, 1, 9, 3, 0, 0, 7, 10, 0, 9, 10, 0, 1, 5, 6, 10, 9, 5, 4, 8, 3, 4, 2, 8, 7, 0, 8, 4, 5, 2, 0, 10, 1, 4, 8, 2, 5, 2, 7, 5, 9, 9, 7, 3, 8, 10, 6, 4, 9, 5, 8, 4, 10, 3, 10]
yData = [10, 8, 2, 5, 0, 2, 2, 10, 5, 10, 2, 7, 4, 4, 4, 1, 1, 3, 10, 10, 10, 1, 3, 3, 6, 1, 9, 7, 5, 9, 4, 6, 1, 8, 0, 3, 2, 8, 3, 9, 1, 2, 4, 1, 10, 9, 7, 5, 2, 10, 9, 4, 4, 3, 6, 10, 3, 7, 0, 1, 1, 9, 5, 9, 3, 2, 0, 7, 5, 1, 6, 0, 1, 8, 10, 10, 10, 10, 8, 2, 4, 1, 7, 10, 1, 5, 0, 8, 8, 8, 8, 3, 2, 10, 8, 1, 1, 8, 0, 3]


########################
### Averages

#Arithmetic Mean of data set
def mean(data):
    
    dataSum = sum(data)
    dataNum = len(data)
    dataMean = dataSum / dataNum
    return dataMean

#Fast approximation of arithmetic mean
def fastMean(data):
    
    p = 0
    

#Geometric Mean of Data set
def geoMean(data):
    
    dataLen = len(data)
    dataMult = 0
    for i in range(0,dataLen):
        dataMult *= data[i]
    gMean = dataMult ** (1/dataLen)
    
    return gMean

#Harmonic Mean of Data set
def harMean(data):
    
    dataLen = len(data)
    dataSum = 0
    for i in range(0,dataLen):
        dataSum += (1/data[i])
    hMean = dataLen / dataSum
    
    return hMean
    

########################
### Variances

#Population Variance
def variance(data):
    
    dataMean = mean(data)
    dataLen = len(data)
    varSum = 0
    
    for i in range(0,dataLen):
        varSum += (data[i] - dataMean)**2
    var = varSum / dataLen
    
    return var

#Sample Variance
def sampleVar(data):
    
    dataMean = mean(data)
    dataLen = len(data)
    varSum = 0
    
    for i in range(0,dataLen):
        varSum += (data[i] - dataMean)**2
    var = varSum / (dataLen - 1)
    
    return var

########################
### Standard Deviations

#Sample Standard Deviation
def sampleStd(data):
    
    sVar = sampleVar(data)
    sStd = sVar ** 0.5
    
    return sStd

#Population Standard Deviation      
def stdev(data):
    
    var = variance(data)
    std = var ** 0.5
    
    return std

########################
### Correlations

def pearsons(xData,yData):
    
    p=0
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    