"""
QUESTÃO 2
Erro absoluto e erro relativo
Author: João Pedro Simões
Created: 18/02/2025

"""

import math

p = [2**PI, math.sqrt(5), E**10, math.factorial(5)]
pa = [8.8341,2.235,22000, np.sqrt(18*PI)*((9/E)**9)]


absol_erro = []
rela_erro = []

for i in range(len(p)):
    absol_erro.append(abs(p[i]-pa[i]))

for i in range(len(p)):
    rela_erro.append(absol_erro[i]/p[i])


for i in range(len(p)):
    print("-----\np  = {}\np* = {}\nErro absoluto: {}\nErro relativo: {}".format(p[i],pa[i],absol_erro[i],rela_erro[i]))