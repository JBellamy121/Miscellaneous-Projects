# -*- coding: utf-8 -*-
"""
Author: Jack Bellamy
Date: 29/03/23
Task: Fourier Approximation of Sawtooth and Square Waves
"""

#Modules used
import math
import matplotlib.pyplot as plt

#Sawtooth Wave Function    
def sawtoothWave():
    
    #Function parameters
    cycles = 3 #How many times should wave repeat
    stepSize = 2 * math.pi / 2000 #step difference between x values
    termAmount = 150 #Amount of terms used in calculation
    
    #Lists for results
    yResults = []
    xResults = []

    #Calculating individual term results
    for n in range(1,termAmount+1):
        x = 0 #Initial x point
        pos = 0 #Postion value for yResults list, used in loop below
        
        while x <= (2 * math.pi * cycles):
            
            y = math.sin(n * x) / n
            
            if n == 1: #Check if its first pass through
                xResults.append(x)
                yResults.append(y)
            else: #Any succesive past through
                yResults[pos] += y #Sum corresponding y values with current result
                
            pos += 1
            x += stepSize

    #Matplotlib Plots    
    plt.plot(xResults,yResults)
    plt.title('Sawtooth Wave Approximation')
    plt.grid()
    
    
    
#Square Wave Function
def squareWave():
    
   #Function parameters
   cycles = 3 #How many times should wave repeat
   stepSize = 2 * math.pi / 2000 #step difference between x values
   termAmount = 150 #Amount of terms used in calculation
   
   #Lists for results
   yResults = []
   xResults = []

   #Calculating individual term results
   for n in range(1,termAmount+1):
       if n % 2 != 0:
           x = 0 #Initial x point
           pos = 0 #Postion value for yResults list, used in loop below
           
           while x <= (2 * math.pi * cycles):
               
               y = math.sin(n * x) / n
               
               if n == 1:
                   xResults.append(x)
                   yResults.append(y)
               else:
                   yResults[pos] += y
                   
               pos += 1
               x += stepSize
       
        
   #Matplotlib Plots    
   plt.plot(xResults,yResults)
   plt.title('Square Wave Approximation')
   plt.grid()
     
   
#Triangle Wave Function
def triangleWave():
    
   #Function parameters
   cycles = 3 #How many times should wave repeat
   stepSize = 2 * math.pi / 2000 #step difference between x values
   termAmount = 150 #Amount of terms used in calculation
   
   #Lists for results
   yResults = []
   xResults = []

   turn = 1
   #Calculating individual term results
   for n in range(1,termAmount+1):
       
       if n % 2 != 0:
           x = 0 #Initial x point
           pos = 0 #Postion value for yResults list, used in loop below
           
           while x <= (2 * math.pi * cycles):
               
               if turn % 2 != 0:
                   y = (math.sin(n * x) / (n**2))
               else:
                   y = -1 * (math.sin(n * x) / (n**2))
               
                
               if n == 1:
                   xResults.append(x)
                   yResults.append(y)
               else:
                   yResults[pos] += y
            
               pos += 1
               x += stepSize
           turn += 1
       
        
   #Matplotlib Plots    
   plt.plot(xResults,yResults)
   plt.title('Square Wave Approximation')
   plt.grid()
    
    
        
    