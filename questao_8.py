"""
QUESTÃO 8
Colormaps
Author: João Pedro Simões
Created: 21/02/2025
"""
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return (x**3 - 7*x + 1)


def getX(a,b,n):
    unit = (b-a)/(n-1)

    x = []
    for i in range(n):
        x.append(a + unit*i)
    
    return x

# Considere que o b > a
def solve(f,a,b,n,titulo,xb,yb):
    x = getX(a,b,n)
    y = [f(i) for i in x]

    #print(x)
    #print(y)

    #plt.plot(x,y,'bo')

    plt.plot(x,y) #normal

    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True,linestyle='--')

    btm = -1 # -4 - to see more - -0.1
    up = 1 # 4 to see more

    
    xmin = -max(xb)
    xmax = max(xb)
    ymin = -max(yb)
    ymax = max(yb)
        
    plt.xlim(xmin,xmax)  # Set x-axis limits from 2 to 4
    plt.ylim(ymin,ymax)  # Set y-axis limits from 12 to 18

    #small = 0.2
    #plt.xticks(np.arange(btm, up, small))
    #plt.yticks(np.arange(btm, up, small))
    colors = [i for i in range(1,len(xb)+1)]
    #colors.reverse()

    colorgrad = plt.colormaps["autumn"]
    colorgrad = colorgrad.reversed()
    
    plt.scatter(xb,yb, c=colors,cmap=colorgrad)
    
    plt.title(titulo)
    plt.colorbar().set_label("MAIS INTESA COR = MAIS RECENTE")
    plt.show()

# METODO DA BISSECÇÃO
x_biss= [1.0, 0.5, 0.25, 0.125, 0.1875, 0.15625, 0.140625, 0.1484375, 0.14453125, 0.142578125, 0.1435546875, 0.14306640625, 0.143310546875, 0.1431884765625, 0.14324951171875, 0.143280029296875, 0.1432647705078125, 0.14327239990234375, 0.14327621459960938, 0.1432781219482422, 0.14327716827392578]

y_biss = [f(i) for i in xb]

"""-
xmin = -max(xb) # -max(xb)
xmax = max(xb) # max(xb)
ymin = -max(yb) # -max(yb)
ymax = max(yb) # max(yb)
"""

solve(f,-10,10,1000, "Método da Bissecção",x_biss,y_biss)

# METÓDDO DE NEWTON
x_new = [2, 3.0, 2.65, 2.574675670872579, 2.5712086539558507, 2.5712014225795534, 2.5712014225481217]
y_new = [f(i) for i in xn]

solve(f,-10,10,1000,"Método de Newton",x_new,y_new)


