# -*- coding: utf-8 -*-
"""
Author: Jack Bellamy
Date: 31/03/23
Task: Sierpinski Triangle - Chaos Game
"""

import random
import matplotlib.pyplot as plt

#Generate sierpenski triangle using chaos game
def sierpinski(pointAmount):
       
    vert = [[0,0],[100,0],[50,100]] #Verticies of Triangle
    v0 = randomPoint() #Initial random point
    
    pointsX = [vert[0][0],vert[1][0],vert[2][0],v0[0]] #List of x-ordinate of points
    pointsY = [vert[0][0],vert[1][0],vert[2][0],v0[1]] #List of y-ordinate of points
    
    ints = 0 #Initial interations amount
    while ints < pointAmount:
        
        randVert = vert[random.randint(0,2)] #Select random verticie of triangle
        newV = midpoint(v0,randVert) #Find midpoint of random verticie and random point
        
        pointsX.append(newV[0]) #Append midpoint x-ordinate to list
        pointsY.append(newV[1]) #Append midpoint y-ordinate to list
        
        v0 = newV #Use temp value for new point
        
        ints += 1
        
    plt.scatter(pointsX,pointsY,s=5) #Generate plot of points
    plt.title('Sierpinski Triangle from Chaos Game')
   

#Generate random point with bounds (0 < x < xMax) and (0 < y < yMax)
def randomPoint():
    
    xMax = 100 #Max bound for xValue
    yMax = 100 #Max bound for yValue
    
    x = random.random() * xMax #Random uniform value for x-ordinate
    y = random.random() * yMax #Random uniform value for y-ordinate
    
    point = [x,y]
    
    return point


#Generate midpoint of p1 and p2
def midpoint(p1,p2):

    xMid = (p1[0] + p2[0]) * 0.5 #Calculates x-ordinate of midpoint
    yMid = (p1[1] + p2[1]) * 0.5 #Calculates y-ordinate of midpoint
    
    return [xMid,yMid]

