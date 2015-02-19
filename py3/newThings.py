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

# print com end não newline:
for i in range(10):
    print(i,i**2,i**3,end=" ")
