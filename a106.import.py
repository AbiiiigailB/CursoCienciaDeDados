import math as m
from pandas import dateframe

raiz = m.sqrt(9)
print(f"a raiz quadrada é{raiz}")

print(m.ceil(6.3))            

dados = {'nome': ['alice','beto','carlos'],'idade':[25,30,35]}
DadosFormatados = dateframe(dados)
print(DadosFormatados)


