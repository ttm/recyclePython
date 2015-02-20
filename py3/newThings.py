# string methods

# range(x) returns an iterable, not a list:
it_range=range(10)
list_range=list(range(10))

# for and while have else clauses:
for i in range(10):
    print(i,i**2,i**3)
else:
    print('acabou com', i)

# break sai do loop mais extremo
# continue vai para a próxima iteração

# aprendido do *args e **kargs em funcoes:
def afun(*ar,**kar):
    print(ar)
    print(ar[3])
    print(kar)
afun(1,3,5,17,you="me",they="them",this="that")

# print com end não newline:
for i in range(10):
    print(i,i**2,i**3,end=" ")

# append é mais eficiente que list+[]

# argumentos mutáveis sofrem alterações permanentes:
def f(a,L=[]):
    L.append(a)
    return L
print(f(1))
print(f(10))
print(f(12))
def F(a,L=[]):
    L.append(a)
    print(L)
F(1)
F(10)
F(12)
# mas o inteiro parece ser reavaliado:
def A(a=2,b=None):
    if b!=None:
        a=b
    print(a)
A()
A(b=7)
A()

# desempacoando lista de argumentos
things={"t1":"thingy","t2":"big thing","t3":"another thing"}
def T(t1,t2="that all",t3="nothing"):
    print(t1,t2,t3,sep=", ")
T(**things)

pairs=[(3,"three"),(12,"twelve"),(9,"nine"),(15,"fifteen")]
pairs.sort(key=lambda x:x[1])
print(pairs)
pairs.sort(key=lambda x:len(x[1]))
print(pairs)

# docstrings começam com uma linha de sumário com letra maiúscula e ponto final.
# pula linha para especificar o resto, quando necessário.

# function annotations!!
def anotFun(a: "any value", b:int=42,c:12="twelve") -> "returns some stuff":
    """A functin to test annotations"""
    print(a,b,c)
    print(anotFun.__annotations__)
anotFun(100)

# lista é boa pilha mas má fila, para tal, usar deque:
from collections import deque
queue=deque([10,100,"tqueue","this"])
queue.append("one more")
queue.append("another")
print(queue.popleft()) # pops 10
print(queue.popleft()) # pops 100

comb=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
combs=[(x,x**2,y,y/3) for x in [1,2,3,4] for y in [34,21] if y%x==0]

vec=[[1,4,6],[4,12,67,9],[5,1,0]]
avec=[num for ele in vec for num in ele]

# tuplas sao imutáveis mas podem possuir elementos mutáveis
v=([2,3,4],[4,5,6])
v[0][2]=99
print(v)

# notação para conjuntos
cesta={"boo",14,34,27,11} # ou set()
# e set comprehensions
acesta={x for x in "abracadabra" if x not in "abc"}
# operações -, |, &, ^

# dict.keys() retorna uma interador, para ter a lsita precisa usar list()
dic={1:100,4:200,"aqui":"ali"}
del dic[1] #deletando elemento
dic2=dict([(1,100),(4,200),("aqui","ali")])
dic3=dict(oi=100,tchau=1,onde="ali")
dic4={x:x**3 for x in range(95,100)}

# n esquecer do enumerate
for i,v in enumerate(["tic","tac","toe"]):
    print(i,v)

# sorted() mantem o original
for i in sorted(["me","you","them","that","iii"]):
    print(i)

# chained comparrison:
print(3<4==2*2)

# this imports all names except those starting with _
from fibo import *

import fibo
# para recarregar um modulo depois de importado:
import imp; imp.reload(fibo)
# caso contrário o módulo nao é recarregado

# sys.ps1 e sys.ps2 contem os >>> e ... do prompt
import sys
print(sys.ps1,sys.ps2)

dir() # exibe todos os nomes do namespace, para alem do %whos

# from Package import specific_submodule é o formato recomendado
# __init__.py faz com que o diretório seja considerado um pacote
# pode também conter código para inicialização
# e o __all__=["modulo1","modulo2"] etc

# dentro do pacote, o import usa caminhos absolutos import xxx.yyy.zzz
# caminhos relativos também funcionam from ..yyy import zzz,
# mas dão problema em algumas situações
