"""
QUESTÃO 4
Erro absoluto e erro relativo
Author: João Pedro Simões
Created: 19/02/2025

"""

option = 1

def t3(number):
    if option == 1: #truncamento com 3 digitos
        return Decimal(number).quantize(Decimal('.001'),rounding=ROUND_DOWN)
    else:
        return Decimal(number).quantize(Decimal('.001'),rounding=ROUND_HALF_UP) #não ROUND_UP


def erro_absoluto(p,pa):
    erro = []
    for i in range(len(p)):
        #erro.append(abs(p[i]-pa[i]))
        #print(p[i],pa[i])
        #print(abs(Decimal('{}'.format(p[i])) - pa[i] ))
        erro.append(abs(Decimal('{}'.format(p[i])) - pa[i] ))
        
        #print("{}".format(Decimal('{}'.format(p[i]))))
    return erro

def erro_relativo(p,pa):
    erro = []
    for i in range(len(p)):
        #erro.append(abs(p[i]-pa[i]))
        #print(p[i],pa[i])
        #print( abs((Decimal('{}'.format(p[i])) - pa[i] ) / Decimal('{}'.format(p[i]) )))
        erro.append(abs((Decimal('{}'.format(p[i])) - pa[i] ) / Decimal('{}'.format(p[i]) )))
        #print("{}".format(Decimal('{}'.format(p[i]))))
    return erro

      
#print(t3(121.63499))
#option = 0
#print(t3(121.63499))
#option = 1
#print(t3(121.63499))

PI = pi
E = e

#print(PI,E)
#a)

exato = [ (121-119)-0.327, -10*(PI) + 6*E - 3/62, (2/9)*(9/7)]


option = 1
truncado = [ t3(t3( t3(121)-t3(119) ) - t3(0.327)) , t3( t3(-10*t3(PI)) + 6*t3(E) - t3(3/62) ), t3( t3(2/9)*t3(9/7) )]

option = 0
#print(t3(121.2319))

#print(Decimal(0.3271).quantize(Decimal('.001'),rounding=ROUND_HALF_UP))
#print( t3(t3(t3(121)-t3(119)) - t3(0.327)))

arrendondado =  [ t3(t3( t3(121)-t3(119) ) - t3(0.327)) , t3( t3(-10*t3(PI)) + 6*t3(E) - t3(3/62) ), t3( t3(2/9)*t3(9/7) ) ]

#print(exato)
#print(truncado)
#print(arrendondado)

#truncado

erro_absol_t = erro_absoluto(exato,truncado)
erro_rela_t =  erro_relativo(exato,truncado)

#print(erro_absol,erro_rela)


#arredondado

erro_absol_a = erro_absoluto(exato,arrendondado)
erro_rela_a =  erro_relativo(exato,arrendondado)

print("----Resultados com Truncamento de 3 digitos----")
for i in range(len(exato)):
    print("Resultado exato: {}\nErro absoluto: {}\nErro relativo: {}\n~~".format(exato[i],erro_absol_t[i],erro_rela_t[i]))
print("")
print("----Resultados com Arredondamento de 3 digitos----")
for i in range(len(exato)):
    print("Resultado exato: {}\nErro absoluto: {}\nErro relativo: {}\n~~".format(exato[i],erro_absol_a[i],erro_rela_a[i]))
    

#print(erro_absol,erro_rela)

#print("{}\n{}".format(erro_absol,erro_rela))