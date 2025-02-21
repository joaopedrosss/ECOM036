"""
QUESTÃO 6
Plotagem de gráfico
Author: João Pedro Simões
Created: 20/02/2025
"""
import matplotlib.pyplot as plt
import numpy as np

# Considere que o b > a

def f(x):
    return (-5)*(x**3) + 6

def getX(a,b,n):
    unit = (b-a)/(n-1)

    x = []
    for i in range(n):
        x.append(a + unit*i)
    
    return x

def solve(f,a,b,n):
    x = getX(a,b,n)
    y = [f(i) for i in x]

    #print(x)
    #print(y)

    #plt.plot(x,y,'bo')

    plt.plot(x,y) #normal
    plt.show()


#print(getX(0,10,10))

solve(f,-10,10,10)