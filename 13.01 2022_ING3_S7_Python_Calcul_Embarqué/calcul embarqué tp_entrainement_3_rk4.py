import numpy as np
import matplotlib.pyplot as plt
import math 

def fx_y(x,y):
    return -5*y+5*math.exp(-x)

def rk4(h,xn,yn):
    k1=fx_y(xn,yn)
    k2=fx_y(xn+h/2,yn+h*k1/2)
    k3=fx_y(xn+h/2,yn+h*k2/2)
    k4=fx_y(xn+h/2,yn+h*k3/2)
    return yn+h*(k1+2*k2+2*k2+k4)/6
                    
h=0.01
y0=float(input('y0 initial : '))

nb_points=100

t=np.linspace(0,nb_points,nb_points)
xn=np.linspace(0,h*nb_points,nb_points)

yn=np.linspace(0,0,nb_points)
solution=np.linspace(0,0,nb_points)

yn[0]=y0


for i in range(1,nb_points):
    yn[i]=rk4(h,xn[i-1],yn[i-1])
    solution[i]=1.25*math.exp(-xn[i])-0.25*math.exp(-5.*xn[i])
    
plt.plot(t, yn,solution)
plt.show() 


