from math import *
import random
from .helperfuncs import *
from fractions import Fraction

def save_identical_springs_diff_weights_question(filepath):
    k = abs(random.choice(EASY_INTS_NO_ZERO))
    x1, x2 = random_x([abs(_) for _ in EASY_INTS_NO_ZERO], 2)
    w1, w2 = k*x1, k*x2
    x = abs(random.choice(EASY_INTS_NO_ZERO))
    q = f"Two identical springs in equilibrium each have a mass hung under it.\nThe springs are both in equilibrium.\nThe mass of the load on the first spring is {w1/10} kg and the mass of the load on the second spring is {w2/10} kg.\n"
    q += f"The difference in extensions of the two springs are {abs(x2-x1)} m."
    pos = random.randint(0,1)
    if pos: q += f"The springs are now hung in parallel with a load of {k*x/10} kg.\n"
    else: q += f"The springs are now hung in series with a load of {k*x/10} kg.\n"
    eox = random.randint(0,2)
    if eox == 0:
        q += "What is the total strain energy in the springs in joules?"
        ans = k*(x**2)
    elif eox == 1:
        q += "What is the strain energy in one of the springs in joules?"
        ans = k*(x**2)/2
    else:
        q += "What is the extension of the springs in meters?"
        if pos: ans = x/2
        else: ans = x*2
    save_text(q, filepath)
    return ans, q

def save_cylinder_pressure_question(filepath):
    h, d = abs(random.choice(EASY_INTS_NO_ZERO)), abs(random.choice(EASY_INTS_NO_ZERO))*100
    p1 = abs(random.choice(EASY_INTS_NO_ZERO))*1000
    p2 = p1 + h*d*10
    rand_const = abs(random.choice(EASY_INTS_NO_ZERO))
    v1, v2 = lcm(p1,p2)*rand_const/p1, lcm(p1,p2)*rand_const/p2
    print(lcm(p1,p2), v1,v2)
    tf, uf = random_x(FLUIDS, 2)
    q = f"A water-tight cylinder with a thin, freely moving piston contains {v1} $m^3$ of trapped {tf} at pressure {p1} Pa.\nWhen the cylinder is submerged in {uf} of constant density {d} kg $m^"+r"{-3}$"+f"the volume of the {tf} in the cylilnder decreases to {v2} $m^3$.\n The piston is at a depth h below the surface of the water and the water surface is open to the atmosphere.\nWhat is the depth h? Take g = 10 m/$s^"+r"{2}$, assume that the temperature if constant and the fluid is ideal."
    save_text(q, filepath)
    print(q)
    return h, q

def save_young_modulus_question(filepath):
    m = abs(random.choice(EASY_INTS_NO_ZERO))
    x = abs(random.choice(EASY_INTS_NO_ZERO))
    A = abs(random.choice(EASY_SCIENTIFIC_INTS_NO_ZERO))
    apwr = random.choice([-5,-6,-7])
    E = abs(random.choice(EASY_SCIENTIFIC_INTS_NO_ZERO))
    epwr = random.choice([10,11,12])
    dx = Fraction(m*10*x,int(E*(10**epwr)*A*(10**apwr)))
    energy = Fraction(1,2)*(m*10)*dx
    q = f"A light {random.choice(METALS)} wire of length {x} m and uniform cross-sectional area {A}*$10^"+r"{"+f"{apwr}"+r"}$ $m^2$" + "\n"
    q += f"supports a load of {m} kg.\n"
    q += f"The Young's Modulus of the wire is {E}*$10^" + r"{" + f"{epwr}" + "}$ Pa.\n"
    eod = random.randint(0,1)
    if eod == 0:
        q += "Find the strain energy in the wire as a fraction."
        ans = energy
    else:
        q += "Find the extension of the wire as a fraction."
        ans = dx
    q += "\nTake g = 10 m/$s^2$."
    save_text(q, filepath)
    return ans, q

    



if __name__ == "__main__":
    print(save_young_modulus_question("foo.png"))