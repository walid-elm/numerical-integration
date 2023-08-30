#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[38]:


# Integral Universal Function

class Integral:
    """
    Integral is a function that allows you to calculate the area under any given function f(), in any interval [a,b].
    
    Choose between four different integration numerical methods:
    
        1.Trapezoid Method
        2.Mid Point Method
        3.Simpsons Method
        4.Monte Carlo Method
    
    """
    
    def __init__(self,f,a,b,n):
        """
        args:
        
            f is the function to be integrtated
            a is the lower bound of the integration interval
            b is the upper bound of the integration interval
            n is the number of intervals of approximation
        
        """
        self.h=abs(b-a)/n
        self.a=a
        self.b=b
        self.n=n
        self.f=f
        self.xs=np.arange(self.a,self.b+self.h,self.h)
        
    def trapezoidal(self,):
        res=0
        for i in range(self.n):
            res=res+(self.f(self.xs[i+1])+self.f(self.xs[i]))*(self.h/2)
        return res
    
    def midpoint(self,):
        res=0
        for i in range(self.n):
            res=res+self.h*self.f(self.a+self.h/2+i*self.h)
        return res
    
    def simpson(self,):
        res=0
        for i in range(1,self.n+1):
            res=res+self.h/6*(self.f(self.a+i*self.h-self.h)+4*self.f(self.a+i*self.h-self.h/2)+self.f(self.a+i*self.h))
        return res
    
    def montecarlo(self,N):
        self.ys=self.f(self.xs)
        up=max(self.ys)
        low=min(self.ys)
        self.p1=0
        self.tot_area=abs(up-low)*abs(self.b-self.a)
        
        for i in range(N):
            x=np.random.uniform(self.a, self.b)
            y=np.random.uniform(low,up)
            if y<=self.f(x):
                self.p1=self.p1+1
            else:
                None
        self.p1=self.p1/N
        res=self.p1*self.tot_area
        return res
    
    


# In[49]:


# Example

def g(x):
    return x**2

g_Integral=Integral(g,0,2,1000)

act=8/3 #actual integral value, found analitically
a1=g_Integral.trapezoidal()
a2=g_Integral.midpoint()
a3=g_Integral.simpson()
a4=g_Integral.montecarlo(10000)

results=pd.DataFrame()
results["Metrics"]=["result","error"]
results["Trapezoid"]=[a1,abs(act-a1)]
results["Mid Point"]=[a2,abs(act-a2)]
results["Simpson"]=[a3,abs(act-a3)]
results["Mone Carlo"]=[a4,abs(act-a4)]
results=results.set_index("Metrics")

results


# In[ ]:




