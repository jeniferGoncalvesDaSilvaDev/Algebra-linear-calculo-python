from sympy import limit, symbols
import numpy as np
#calcular o limite de V(t) =Vr+ (Vp-Vr
#) (1-e**(-t/tau))
#com tau= 5
t = symbols('t')
vr = -70
vp= 30
#t tende a infinito
tau =5
#constante de Euler
e = 2.72
limite_funcao=limit(vr+(vp-vr) *(1-e**(-t/tau)), t, 0)
print(limite_funcao)
#no teorema de compressão,ou teorema de sanduíche,mostra no comportamento de uma função,tal valor se aproxima de valores extremos,sendo limites ou valores fixos. Neste exemplo, é calculado o potencial de membrana de um neurônio,quando o tempo tende ao infinito com o valor do potenciail em repouso é -70mv e o potencial em despolarização é 30mv
#com array de valores de potencial de repouso e despolarização respectivamente
vr_array= np.array([-30, -45,-60,-70, -90])
vp_array= np.array([30, 45,50,60, 80])

limite_funcao_array = []
for i in range(len(vr_array)):
    limite_funcao_array.append(limit(vr_array[i]+(vp_array[i]-vr_array[i]) *(1-e**(-t/tau)), t, 0))
print(limite_funcao_array)
