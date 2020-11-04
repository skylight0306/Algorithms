#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
'''
Algorithm Project 
V.Grid Puzzle

'''
# scanf Puzzle
a,b,c = input('輸入第一排3個數字').split()
d,e,f = input('輸入第二排3個數字').split()
g,h,i = input('輸入第一排3個數字').split()
floor1 = [a,b,c]
floor2 = [d,e,f]
floor3 = [g,h,i]

route = 0
case = "0"


# In[2]:


'''
location:
  1,2,3        floor1[0] [1] [2]
  4,5,6   =>   floor2[0] [1] [2]
  7,8,9        floor3[0] [1] [2]
    
'''

def ShowMap() :
    print(floor1)
    print(floor2)
    print(floor3)
#ShowMap()


def Initial(floor1,floor2,floor3,route) :
    floor1[0] = a
    floor1[1] = b
    floor1[2] = c
    floor2[0] = d
    floor2[1] = e
    floor2[2] = f
    floor3[0] = g
    floor3[1] = h
    floor3[2] = i

    route = 0
    case = "0"

def Process(num,floor1,floor2,floor3,route,case) :
    print("Start : ")
    ShowMap()
    print("Route = ", route, "\n")

    print("Step1 : ")
    route, case = Step1(num,floor1,floor2,floor3)
    ShowMap()
    print("Route = ", route, "\n")

    print("Step2 : ")
    route = Step2(floor1,floor2,floor3,route,case)
    ShowMap()
    print("Route = ", route, "\n")

    print("Step3 : ")
    route = Step3(floor1,floor2,floor3,route,case)
    ShowMap()
    print("Route = ", route, "\n")

    print("Step4 : ")
    route = Step4(floor1,floor2,floor3,route,case)
    ShowMap()
    

        
def ShowProcess() :
    if MinSum == case1 :
        Process(1,floor1,floor2,floor3,route,case)
    elif MinSum == case2 :
        Process(2,floor1,floor2,floor3,route,case)
    elif MinSum == case3 :
        Process(3,floor1,floor2,floor3,route,case)
    elif MinSum == case4 :
        Process(4,floor1,floor2,floor3,route,case)
    elif MinSum == case5 :
        Process(5,floor1,floor2,floor3,route,case)
    else :
        Process(6,floor1,floor2,floor3,route,case)
        


# In[3]:


'''
Step1
  0,x,x
  x,x,x   at the first time
  x,x,1

  Right x 2
  Down x 2
  4!/2!2! = 6

  Find the shortest route
  o is the route which was pass
Case:
1.       2.
  0,o,o    0,o,x
  x,x,o    x,o,x
  x,x,1    x,o,1
  
3.       4.
  0,o,x    0,x,x
  x,o,o    o,o,o
  x,x,1    x,x,1
  
5.       6.
  0,x,x    0,x,x
  o,o,x    o,x,x
  x,o,1    o,o,1

'''
def Step1(num,floor1,floor2,floor3):
    one = int(floor1[1]) + int(floor1[2]) + int(floor2[2]) + 1     #Case1 RRDD   CaseA
    two = int(floor1[1]) + int(floor2[1]) + int(floor3[1]) + 1     #Case2 RDDR   CaseB
    three = int(floor1[1]) + int(floor2[1]) + int(floor2[2]) + 1   #Case3 RDRD   CaseA
    four = int(floor2[0]) + int(floor2[1]) + int(floor2[2]) + 1    #Case4 DRRD   CaseA
    five = int(floor2[0]) + int(floor2[1]) + int(floor3[1]) + 1    #Case5 DRDR   CaseB
    six = int(floor2[0]) + int(floor3[0]) + int(floor3[1]) + 1     #Case6 DDRR   CaseB
    
    #shortest = min(one, two, three, four, five, six)
    if num == 1 or num == 3 or num == 4 :
        case = "A"
    else :
        case = "B"
    
    #Switch
    if num == 1 :
        floor1[0] = floor1[1]
        floor1[1] = floor1[2]
        floor1[2] = floor2[2]
        floor2[2] = floor3[2]
        floor3[2] = "0"
        return one, case
    elif num == 2 :
        floor1[0] = floor1[1]
        floor1[1] = floor2[1]
        floor2[1] = floor3[1]
        floor3[1] = floor3[2]      
        floor3[2] = "0"
        return two, case
    elif num == 3 :
        floor1[0] = floor1[1]
        floor1[1] = floor2[1]
        floor2[1] = floor2[2]
        floor2[2] = floor3[2]   
        floor3[2] = "0"
        return three, case
    elif num == 4 :
        floor1[0] = floor2[0]
        floor2[0] = floor2[1]
        floor2[1] = floor2[2]
        floor2[2] = floor3[2]   
        floor3[2] = "0"
        return four, case
    elif num == 5 :
        floor1[0] = floor2[0]
        floor2[0] = floor2[1]
        floor2[1] = floor3[1]
        floor3[1] = floor3[2]       
        floor3[2] = "0"
        return five, case
    else :
        floor1[0] = floor2[0]
        floor2[0] = floor3[0]
        floor3[0] = floor3[1]
        floor3[1] = floor3[2]    
        floor3[2] = "0"
        return six, case
        
#route, case = Step1(floor1,floor2,floor3)
#print(route)
#print(case)
#ShowMap()


# In[4]:


'''
Step2

CaseA     CaseB
  x,x,x     x,x,x
  x,x,1     x,x,x
  x,x,0     x,1,0

  Find the shortest route
  o is the route which was pass
CaseA     CaseB
  x,x,x     x,x,x
  x,o,1     x,o,o
  x,o,0     x,1,0
  
'''
def Step2(floor1,floor2,floor3,route,case):
    if case == "A" :    #CaseA
        shortest = int(floor2[1]) + int(floor3[1]) + 1
        #Switch
        floor3[2] = floor3[1]
        floor3[1] = floor2[1]   
        floor2[1] = floor2[2]
        floor2[2] = "0"
    else :              #CaseB
        shortest = int(floor2[1]) + int(floor2[2]) + 1
        #Switch
        floor3[2] = floor2[2]
        floor2[2] = floor2[1]
        floor2[1] = floor3[1]
        floor3[1] = "0"  
        
    return shortest+route
#route = Step2(floor1,floor2,floor3,route,case)
#print(route)
#ShowMap()


# In[5]:


'''
Step3

CaseA     CaseB
  x,x,x     x,x,x
  x,1,0     x,1,x
  x,x,x     x,0,x

  Find the shortest route
  o is the route which was pass
CaseA     CaseB
  x,o,o     x,x,x
  x,1,0     o,1,x
  x,x,x     o,0,x
  
'''
def Step3(floor1,floor2,floor3,route,case):
    if case == "A" :    #CaseA
        shortest = int(floor1[1]) + int(floor1[2]) + 1
        #Switch
        floor2[2] = floor1[2]
        floor1[2] = floor1[1]   
        floor1[1] = floor2[1]
        floor2[1] = "0"
    else :              #CaseB
        shortest = int(floor2[0]) + int(floor3[0]) + 1
        #Switch
        floor3[1] = floor3[0]
        floor3[0] = floor2[0]
        floor2[0] = floor2[1]
        floor2[1] = "0"  
        
    return shortest+route
#route = Step3(floor1,floor2,floor3,route,case)
#print(route)
#ShowMap()


# In[6]:


'''
Step4

CaseA     CaseB
  x,1,x     x,x,x
  x,0,x     1,0,x
  x,x,x     x,x,x

  Find the shortest route
  o is the route which was pass
CaseA     CaseB
  o,1,x     o,o,x
  o,0,x     1,0,x
  x,x,x     x,x,x
  
'''
def Step4(floor1,floor2,floor3,route,case):
    if case == "A" :    #CaseA
        shortest = int(floor1[0]) + int(floor2[0]) + 1
        #Switch
        floor2[1] = floor2[0]
        floor2[0] = floor1[0]   
        floor1[0] = floor1[1]
        floor1[1] = "0"
    else :              #CaseB
        shortest = int(floor1[0]) + int(floor1[1]) + 1
        #Switch
        floor2[1] = floor1[1]
        floor1[1] = floor1[0]
        floor1[0] = floor2[0]
        floor2[0] = "0"  
        
    return shortest+route
#route = Step4(floor1,floor2,floor3,route,case)
#print(route)
#ShowMap()


# In[7]:


'''
Step5
Write a function with all step

'''
def Simulate(num,floor1,floor2,floor3,route,case) :
    route, case = Step1(num,floor1,floor2,floor3)
    route = Step2(floor1,floor2,floor3,route,case)
    route = Step3(floor1,floor2,floor3,route,case)
    route = Step4(floor1,floor2,floor3,route,case)
    return route


# In[8]:


'''
Step6
Test the all possible case, and find the Minimum

'''
#ShowMap()
case1 = Simulate(1,floor1,floor2,floor3,route,case)
#ShowMap()
Initial(floor1,floor2,floor3,route)

case2 = Simulate(2,floor1,floor2,floor3,route,case)
#ShowMap()
Initial(floor1,floor2,floor3,route)


case3 = Simulate(3,floor1,floor2,floor3,route,case)
#ShowMap()
Initial(floor1,floor2,floor3,route)

case4 = Simulate(4,floor1,floor2,floor3,route,case)
#ShowMap()
Initial(floor1,floor2,floor3,route)


case5 = Simulate(5,floor1,floor2,floor3,route,case)
#ShowMap()
Initial(floor1,floor2,floor3,route)


case6 = Simulate(6,floor1,floor2,floor3,route,case)
#ShowMap()
Initial(floor1,floor2,floor3,route)

MinSum = min(case1,case2,case3,case4,case5,case6)
ShowProcess()
print("Minimum Sum of Costs = ", MinSum)


# In[ ]:




