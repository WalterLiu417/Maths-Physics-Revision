from .helperfuncs import *
import random
from fractions import Fraction
from sympy import expand

def save_triangle_sides_unknown_question(filepath):
    triple = random.choice(PYTHS)
    x = random.randint(1,10)
    mulx = [random.randint(1,5) for _ in range(3)]
    const = [triple[i] - x*mulx[i] for i in range(3)]
    consts = []
    for i in range(3):
        if const[i] < 0:
            consts.append(str(const[i]))
        elif const[i] == 0:
            consts.append("")
        else:
            consts.append("+" + str(const[i]))
    q = f"A right-angled triangle has side lengths {mulx[0]}x{consts[0]} m, {mulx[1]}x{consts[1]} m with hypotenuse {mulx[2]}x{consts[2]} m.\n"
    aox = random.randint(0,1)
    if aox:
        q += "Find the area of the triangle."
        ans = int(triple[0]*triple[1]/2)
    else:
        q += "Find x."
        ans = x
    save_text(q, filepath)
    return ans, q

def save_rhombus_diagonals_question(filepath):
    d1, d2 = random_randints((1,15),2)
    ds = [d1,d2]
    area = Fraction(1,2)*d1*d2
    x = random.randint(1,10)
    mulx = [random.randint(1,3) for _ in range(2)]
    const = [ds[i] - x*mulx[i] for i in range(2)]
    consts = []
    for i in range(2):
        if const[i] < 0:
            consts.append(str(const[i]))
        elif const[i] == 0:
            consts.append("")
        else:
            consts.append("+" + str(const[i]))
    trips = False
    for trip in PYTHS:
        f = Fraction(sorted(ds)[0],sorted(ds)[1])
        if [f.numerator, f.denominator] == trip[:2]:
            trips = True
    q = f"A rhombus has diagonal lengths {mulx[0]}x{consts[0]} m and {mulx[1]}x{consts[1]} m.\nThe area of the rhombus is {area} $m^2$.\n"
    if trips: unk = random.randint(0,2)
    elif not trips: unk = random.randint(0,1)
    if unk == 0:
        q += "Find x."
        ans = x
    elif unk == 1:
        q += "Find the difference in lengths between the diagonals."
        ans = abs(d1-d2)
    elif unk == 2:
        q += "Find the length of one of the sides of the rhombus."
        ans = (d1**2 + d2**2)**(1/2)
    save_text(q, filepath)
    return ans, q

def save_cube_side_unknown_samax_question(filepath):
    combs = []
    for i in range(1,6):
        for j in range(1,6):
            if ((i+j)%2 == 0) and no_prime_factors(i+j, [3,7,11,13,17,19]):
                combs.append((i,j))
    a, b = random.choice(combs)
    c = random.randint(1,9)
    x = random.randint(1,5)
    V = 4*(a**2)*(b**2)*(x**3)/(2*(a+b))
    q = f"A cuboid has side lengths {a}x, {b}x and {c}y m. The volume of the cuboid is {V} $m^3$.\n"
    q += "The cuboid's surface area is minimised.\n"
    xya = random.randint(0,2)
    if xya == 0:
        q += "Find x."
        ans = x
    elif xya == 1:
        q += "Find y."
        ans = V/(a*b*c*(x**2))
    else:
        q += "Find the surface area."
        ans = 2*a*b*(x**2) + (2*V)/(a*x) + (2*V)/(b*x)
    print(q)
    print(x, V/(a*b*c*(x**2)))
    save_text(q, filepath)
    return ans, q

def save_tetrahedron_volume_question(filepath):
    roi = random.randint(0,1)
    q = "The volume of a tetrahedron with side length "
    if roi == 0:
        rx = random.choice([2,3,5,6,7,8])
        q += r"$\sqrt{"+f"{rx}"+r"}$ can be expressed as $a*\sqrt" + r"{b}$" + "\n"
        an = expand(f"(sqrt(2)*(sqrt({rx})^3))/12")
        a, b = an.as_coeff_mul()
        if not b:
            b = 1
        elif b:
            b = b[0]**2
        sop = random.randint(0,1)
        if sop == 0:
            q += "Find a + b."
            ans = a + b
        else:
            q += "Find a * b."
            ans = a * b
    else:
        rx = random.randint(1,9)
        q += f"{rx} can be expressed as $x * \sqrt" + r"{2}$" + ".\n"
        q += "Find x as a fraction."
        ans = Fraction((rx**3),12)
    save_text(q, filepath)
    return ans, q


if __name__ == "__main__":
    print(save_tetrahedron_volume_question("foo.png"))
            
