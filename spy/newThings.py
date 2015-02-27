import scipy as s, numpy as n

# create vectors
vec=s.r_[0,[5]*7,-2:3:15j]
s.c_[[13,22,14],3:8:3j]

# coordinates
s.mgrid[0:3,0:3]
s.ogrid[0:3,0:3]

# polynomial can manipulated in algebraic expressions, integrated, differentiated, and evaluated
p1=s.poly1d([3,4,1])
# p**2, p.integrate(k=10), p.derive(), p.r, p(p.r), p(0.5), p.c
p2=s.poly1d([1,2,3], variable='z')
# use external $ pip install sympy for multivariate algebra
s.vectorize #to make functions operate on vectors for convenience, not performance
#iscomplex, iscomplexobj, isscalar; np.cast["f"](n.pi) ou np.cast["f"](np.array(100))
# s,factorial 
from scipy.misc import factorial
from scipy.misc import comb
#s.select
#s.misc.central_diff_weights # para derivadas em funcao discreta
from scipy import special as sp # bessel kevin gamma etc
from scipy import integrate as inte
result = inte.quad(lambda x: sp.jv(2.5,x), 0, 4.5)
def integrand(t, nn, x):
    return n.exp(-x*t) / t**nn
def expint(nn, x):
    return inte.quad(integrand, 1, n.Inf, args=(nn, x))[0]
vec_expint = s.vectorize(expint)
foo=vec_expint(3,n.arange(1.0,4.0,0.5))
bar=sp.expn(3,n.arange(1.0,4.0,0.5))
print(foo,bar,sep="\n")
result2 = inte.quad(lambda x: expint(3, x), 0, n.inf)
def f(x, y):
    return x*y
def bounds_y():
    return [0, 0.5]
def bounds_x(y):
    return [0, 1-2*y]
result3=inte.nquad(f, [bounds_x, bounds_y])
# inte.fixed_quad inte.quadrature
# scipy.optimize optimization like least squares, roots, 
# scipy.interpolate interpolation
# scipy.fftpack e scipy.signal for windows, such as blackman, and convolution and filters
# scipy.linalg allways, as it has more algs and is always compiled with BLAS/LAPACK
word_list = open('/usr/share/dict/words').readlines()
word_list = map(str.strip, word_list)
word_list = [word for word in word_list if len(word) == 3]
word_list = [word for word in word_list if word[0].islower()]
word_list = [word for word in word_list if word.isalpha()]
word_list = list(map(str.lower, word_list))
word_list = [i.replace("é","e").encode("ascii") for i in word_list]
#wl=[]
#for w in word_list:
#    print(w)
#    wl.append(w.encode("ascii"))
print(len(word_list))
word_list = n.asarray(word_list)
print(word_list.dtype)
word_list.sort()
word_bytes = n.ndarray((word_list.size, word_list.itemsize),
                         dtype='int8',
                         buffer=word_list.data)
print(word_bytes.shape)
from scipy.spatial.distance import pdist, squareform
from scipy.sparse import csr_matrix
hamming_dist = pdist(word_bytes, metric='hamming')
graph = csr_matrix(squareform(hamming_dist < 1.5 / word_list.itemsize))

i1 = word_list.searchsorted('ape')
i2 = word_list.searchsorted('man')
from scipy.sparse.csgraph import dijkstra
distances, predecessors = dijkstra(graph, indices=i1,
                                   return_predecessors=True)
print(distances[i2])
path = []
i = i2
while i != i1:
    path.append(word_list[i])
    i = predecessors[i]
path.append(word_list[i1])
print(path[::-1])
from scipy.sparse.csgraph import connected_components
N_components, component_list = connected_components(graph)
print(N_components)

#scipy.spatial can compute triangulations, Voronoi diagrams, and convex hulls of a set of points
#scipy.stats ks_2samp para testes de kolmogorov-smirnov
#scipy.ndimage
#scipy.io.wavfile para arquivos wave, tb Matlab e Weka
#weave para código C inline, mas só Python 2.6 e 2.7, a recomendação é usar Cython





