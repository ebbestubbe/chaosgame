# -*- coding: utf-8 -*-
"""
Created on Wed May 10 00:27:52 2017

@author: stubb
"""

import numpy as np
import matplotlib.pyplot as plt

p = np.array([[0],[0]])

t1 = np.array([[0,0],[0,0.16]])
a1 = np.array([[0],[0]])
v1 = 0.01

t2 = np.array([[0.85,0.04],[-0.04,0.85]])
a2 = np.array([[0],[1.6]])
v2 = 0.85

t3 = np.array([[0.2,-0.26],[0.23,0.22]])
a3 = np.array([[0],[1.6]])
v3 = 0.07

t4 = np.array([[-0.15,0.28],[0.26,0.24]])
a4 = np.array([[0],[0.44]])
v4 =0.07
plt.close("all")
plt.figure()
n = 1000
#print(t4)
#print(a4)
for i in range(n):    
    #print(" ")
    plt.plot(p[0],p[1],'b.')
    r = np.random.random()
    #print(r)
    if(r<v1):
        t = t1
        a = a1
        #print(1)
    elif(r<v1+v2):
        t = t2
        a = a2
        #print(2)
    elif(r<v1+v2+v3):
        t = t3
        a = a3
        #print(3)
    else:
        t = t4
        a = a4
        #print(4)
#    t = t3
#    a = a3
    #print(" ")
    p = np.dot(t,p)+a
    #print(p)