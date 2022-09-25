import matplotlib.pyplot as plt
from random import choice
from copy import deepcopy as cp
import numpy as np
import math
import os

plt.switch_backend('agg')

PYTHS = [[3,4,5],[5,12,13],[8,15,17],[7,24,25],[9,40,41]]
FLUIDS = ["water", "custard", "caramel", "air", "oxygen", "honey"]
NAMES = ["Andrew", "Kelly", "John", "Joseph", "Marco", "Fanny", "Billy", "Thomas", "Henry", "Will"]
BARS = ["ladder", "bar", "plank"]
OBJECTS = ["car", "bike", "plane", "person", "boat", "truck"]
SMALL_OBJS = ["cup", "bowl", "bag", "stick", "box"]
VARIABLES = ["a", "b", "p", "q", "m", "n", "k", "c"]
VERY_EASY_INTS = [-3,-2,-1,0,1,2,3]
VERY_EASY_INTS_NO_ZERO = [-3,-2,-1,1,2,3]
EASY_INTS = [-10,-8,-5,-4,-2,-1,0,1,2,4,5,8,10]
EASY_SCIENTIFIC_INTS = [-8,-5,-4,-2,-1,0,1,2,4,5,8]
EASY_SCIENTIFIC_INTS_NO_ZERO = [-8,-5,-4,-2,-1,1,2,4,5,8]
EASY_INTS_NO_ZERO = [-10,-8,-5,-4,-2,-1,1,2,4,5,8,10]
EASY_SQUARES = [-30,-20,-16,-15,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,15,16,20,30]
EASY_EVEN_SQUARES = [-30,-20,-16,-12,-10,-8,-6,-4,-2,0,2,4,6,8,10,12,16,20,30]
EASY_EVEN_SQUARES_NO_ZERO = [-30,-20,-16,-12,-10,-8,-6,-4,-2,2,4,6,8,10,12,16,20,30]
EASY_ODD_SQUARES = list(set(EASY_SQUARES)-set(EASY_EVEN_SQUARES))
EASY_ODD_SQUARES_NO_ZERO = list(set(EASY_ODD_SQUARES) - set({0}))
EASY_SQUARES_NO_ZERO = cp(EASY_SQUARES)
EASY_SQUARES_NO_ZERO.remove(0)
SIMPLE_PRIMES = [2,3,5,7]
ELECTRICS = ["lamp", "heater", "boiler", "stove", "iron"]
METALS = ["copper", "iron", "gold", "silver", "titanium", "zinc"]
g = 9.81
easy_g = 10

def lcm(*args):
    return np.lcm(*args)

def longest_line(st):
    ls = st.split("\n")
    maxl, maxlen = "", 0
    for l in ls:
        if len(l) > maxlen:
            maxlen = len(l)
            maxl = l
    return maxlen, maxl

def save_text(text, filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    print("removed")
    ax = plt.axes([0,0,0.3,0.3]) #left,bottom,width,height
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')
    plt.text(0.4,0.4,'%s' %text,size=50,color="green")
    plt.savefig(filepath, bbox_inches='tight')
    plt.close()


def round_sfs(i, n):
    try:
        i = float(i)
    except TypeError:
        i = float(i.mag)
    return float('{:g}'.format(float('{:.{p}g}'.format(i, p=n))))

def random_x(lst, no):
    l = []
    for n in range(no):
        l.append(choice(lst))
        lst.remove(l[n])
    return l

def random_randints(rang, no):
    l = [_ for _ in range(rang[0], rang[1]+1)]
    return random_x(l, no)

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def factors(n):
    i = 1
    facs = []
    while i <= n:
        if n%i == 0:
            facs.append(i)
        i += 1
    return facs

def no_prime_factors(n, unallowed):
    pfs = prime_factors(n)
    for _ in unallowed:
        if _ in pfs:
            return False
    return True

def combination(n, k):
    return math.factorial(n)/(math.factorial(n - k)*math.factorial(k))
