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

# formatação com {}:
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; '
      'Dcab: {Dcab:d}'.format(**table))

# vars() retorna um dicionário das variáves definidas até o momento

# para formatação com o %, ñ é mais necessário a tupla
import math
print('The value of PI is approximately %5.3f.' % math.pi)
print('The value of PI is approximately %5.3f.' % (math.pi,))

with open('workfile.txt', 'r') as f:
    read_data = f.read()
print(f.closed, read_data)

# JSON
import json
x=[1,"simple","list"]

with open('jsonfile.txt', 'w') as f:
    json.dump(x,f)
with open('jsonfile.txt', 'r') as f:
    x2=json.load(f)
print(x,x2,json.dumps(x))

try:
    asoidj
except:
    print("info sobre o que tah rolando")
    #raise
    print("error is:", sys.exc_info())

try:
    a=1
except:
    print("error is:", sys.exc_info())
else:
    print("nada errado no try!")

try:
   raise Exception('spam', 'eggs')
except Exception as inst:
   print(type(inst))    # the exception instance
   print(inst.args)     # arguments stored in .args
   print(inst)          # __str__ allows args to be printed directly,
                        # but may be overridden in exception subclasses
   x, y = inst.args     # unpack args
   print('x =', x)
   print('y =', y)

# In real world applications, the finally clause is useful for releasing 
# external resources (such as files or network connections),
# regardless of whether the use of the resource was successful.
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    #raise
    print("error is:", sys.exc_info())
finally:
    print("alway execute his clause")

import __main__
dir(__main__) # libera uma relação de objetos definidos na sessão

def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

class MyClass:
    def myFunction(self):
        pass
mc=MyClass()
print(mc.myFunction,type(mc.myFunction),MyClass.myFunction, type(MyClass.myFunction))

class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)

# a iteração sobre o dicionário entrega as chaves:
for i in {"ak": 4, 5:2}:
    print(i)

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char)

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)

import shutil, glob
import getopt, argparse
import math, random
import timeit, profile, pstats
print("timeit x=10",timeit.Timer("x=10").timeit(),"timeit x=10",timeit.Timer("x=10").timeit(),"timeit x=1000",timeit.Timer("x=1000").timeit(),"\n---> timeit x=10",timeit.Timer("x=10").repeat(),)
import doctest, unittest
import reprlib, pprint, textwrap

# The principal challenge of multi-threaded applications is coordinating threads that share data or other resources. To that end, the threading module provides a number of synchronization primitives including locks, events, condition variables, and semaphores.
import threading, queue

# para fazer o logfile certinho, não ficar printando tudo no meio do escrito para manter 
# registro do que acontece
import logging

import weakref, gc

from array import array
a = array('H', [4000, 10, 700, 22222])

import bisect
import decimal

#what if you can’t install packages into the global site-packages directory? For instance, on a shared host.
# In all these cases, virtual environments can help you. pyvenv

# https://github.com/pypa/sampleproject/blob/master/setup.py
# http://docutils.sourceforge.net/docutils/statemachine.py
# https://packaging.python.org/en/latest/distributing.html#creating-your-own-project
