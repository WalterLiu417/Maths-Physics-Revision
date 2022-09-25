import math
from .helperfuncs import *
import numpy as np
from .Matrices.rref import rref
from fractions import Fraction
import random
import sympy
from scipy import optimize

FORCES = ["friction", "air resistance", "drag", "mechanical resistance"]
EASY_PERCENTAGES = [10,20,50, -10, -20, -50]

def save_radicals_question(filepath):
    perfsq = abs(random.choice(EASY_SQUARES_NO_ZERO))**2
    r1 = random.choice(prime_factors(perfsq))
    r2 = int(perfsq / r1)
    fop = random.randint(0,1)
    q = "Simplify\n" + "$"
    ans2sf = 0
    if fop == 0:
        q += r"\left(\sqrt{" + str(r1) + r"} + \sqrt{" + str(r2) + r"}\right)^2"
        q += r" - \left(\sqrt{" + str(r1) + r"} - \sqrt{" + str(r2) + r"}\right)^2"
        ans2sf = round_sfs((r1**(1/2) + r2**(1/2))**2 - (r1**(1/2) - r2**(1/2)) ** 2, 2)
    else:
        q += r"\frac{\left(\sqrt{" + str(r1) + r"} + \sqrt{" + str(r2) + r"}\right)}{\left(\sqrt{" + str(r1) + r"} - \sqrt{" + str(r2) + r"}\right)}"
        ans2sf = round_sfs((r1**(1/2) + r2**(1/2)) / (r1**(1/2) - r2**(1/2)), 2)
    q += "$"
    save_text(q, filepath)
    return ans2sf, q

def save_proportion_question(filepath):
    vars = random.randint(1,3)
    forces = random_x(FORCES, vars)
    percents = []
    props = []
    q = f"The speed of a {random.choice(OBJECTS)} is "
    for var in range(vars):
        doi = random.randint(0,1)
        if doi:
            props.append(random.randint(2,3))
            q += f"directly proportional to the power {props[var]} of the {forces[var]} "
        else:
            props.append(random.randint(-3,-2))
            q += f"inversely proportional to the power {props[var]} of the {forces[var]} "
        if var < vars-1:
            q += "and "
        else:
            q += ".\n"
    q += "Find the percentage change in speed if "
    for force in range(len(forces)):
        percents.append(random.choice(EASY_PERCENTAGES))
        q += f"the {forces[force]} is changed by {percents[force]}% "
    q += "to 1 significant figure."
    ans = 1
    for perc in range(len(percents)):
        ans *= (1+percents[perc]/100)**(props[perc])
    ans *= 100
    save_text(q, filepath)
    return round_sfs(ans, 1), q

def save_equation_curve_unknown_question(filepath):
    name_vars = random_x(VARIABLES, 2)
    pts = []
    q = "A curve has equation $f(x) = "
    for var in range(2):
        q += f"{name_vars[var]}x^{2-var} + "
    q = q[:-3]
    q += "$.\n The curve passes through"
    for var in range(2):
        random_point = (random.randint(-10,10), random.randint(-10,10))
        while random_point in pts:
            random_point = (random.randint(-10,10), random.randint(-10,10))
        q += f"the points {random_point} and "
        pts.append(random_point)
    q = q[:-5]
    q += ".\n Find the sum of the unknowns."
    matrix = []
    for point in pts:
        row = []
        for var in range(2):
            row.append(Fraction(point[0]**(2-var)))
        row.append(Fraction(point[1]))
        matrix.append(row)
    print(matrix)
    rr = rref(matrix)
    ans = []
    for row in rr:
        ans.append(row[-1])
    print(q)
    save_text(q, filepath)
    return sum(ans), q

def save_cubic_unknown_derivative_question(filepath):
    name_vars = random_x(VARIABLES, 3)
    pts = []
    q = f"The curve $f(x) = x^3 + {name_vars[0]}x^2 + {name_vars[1]}x + {name_vars[2]}$ has "
    for i in range(2):
        pt = ((random.randint(-10,0) if i==0 else random.randint(1,10)),0)
        q += f"a local {'maximum' if i==0 else 'minimum'} at x = {pt[0]} and "
        pts.append(pt)
    q = q[:-5]
    which = random.randint(0,1)
    q += f".\n Find {name_vars[which]}."
    mat = []
    for pt in pts:
        row = [Fraction(pt[0]*2), 1, Fraction(-3 * (pt[0]**2))]
        mat.append(row)
    rr = rref(mat)
    save_text(q, filepath)
    return rr[which][-1], q

def save_expand_radical_question(filepath):
    radical = random.choice([2,3,5,10])
    pwr = random.randint(2,4)
    pom = "+" if random.randint(0,1) else "-"
    latex_expr = r"\frac{1}{(" + f"1{pom}" + r"\sqrt{" + f"{radical}" + "}" + f")^{pwr}" + "}"
    symp_expr = f"1/(1{pom}sqrt({radical}))^{pwr}"
    un_normal = str(sympy.expand(symp_expr))[3:-1].split(f"*sqrt({radical})")
    if not un_normal[1]:
        if un_normal[0].count("-"):
            a, b = Fraction(un_normal[0].split("-")[0]), -Fraction(un_normal[0].split("-")[1])
        else:
            a, b = Fraction(un_normal[0].split("+")[0]), Fraction(un_normal[0].split("+")[1])
    else:
        b,a = Fraction(un_normal[0]), Fraction(un_normal[1][2:])
    aob = random.randint(0,1)
    q = "The expression " + "$" + latex_expr + "$" + r"can be simplified to $a + b\sqrt{" + str(radical) + "}$.\n"
    ans = 0
    if aob:
        q += "Find a as a fraction."
        ans = Fraction(a / (Fraction(a**2) - Fraction((b**2)*radical)))
    else:
        q += "Find b as a fraction."
        ans = Fraction(-b / (Fraction(a**2) - Fraction((b**2)*radical)))
    save_text(q, filepath)
    return ans, q

def save_similar_question(filepath):
    r1, r2 = random_randints((2,10), 2)
    factor = random.randint(4,20)
    obj = random.choice(SMALL_OBJS)
    q = f"Two {obj}s are mathematically similar. "
    known, unknown = random_randints((1,3),2)
    stuff = ["length", "surface area", "volume"]
    q += f"The ratio of the {stuff[known-1]} of the first {obj} to the second {obj} is {r1**known} : {r2**known}.\n"
    q += f"The {stuff[unknown-1]} of the first object is {factor*(r1**unknown)}. What is the {stuff[unknown-1]} of the second object?"
    ans = factor*(r2**unknown)
    save_text(q, filepath)
    return ans, q

def save_arithmetic_sum_question(filepath):
    a = random.randint(-10,10)*10
    d = random.randint(1,5)*random.choice([-1,1])
    step = random.randint(1,6)*5
    s1 = sum([a + d*i for i in range(step)])
    s2 = sum([a + d*i for i in range(step, step*2)])
    q = f"The first {step} terms of an arithmetic sequence have sum {s1}.\nThe next {step} terms have sum {s2}.\n"
    aod = random.randint(0,2)
    if aod == 0:
        q += "Find the first term."
        ans = a
    elif aod == 1:
        q += "Find the common difference."
        ans = d
    else:
        q += f"What is the sum of the first {step*3} terms?"
        ans = sum([a + d*i for i in range(step*3)])
    save_text(q, filepath)
    return ans, q

def save_different_geometric_infinitesum_question(filepath):
    base_int = random.choice([-5,-4,-3,-2,2,3,4,5])
    conv1, conv2 = sorted([_*2 for _ in random_randints((1,3),2)])
    firstterm = base_int ** (conv2 - random.randint(-2,2))
    cd1, cd2 = Fraction(1, base_int), -Fraction(1, base_int)
    t1 = firstterm * cd1 ** conv1
    t2 = firstterm * cd2 ** conv2
    q = "P and Q are two different geometric series.\n"
    q += f"The {conv1+1}th term of both series is {t1}.\nThe {conv2+1}th term of both series is {t2}.\n"
    q += "What is the modulus of the difference of the sum to infinity of both series?\nGive your answer in a fraction."
    ans = abs(firstterm/(1 - cd1) - firstterm/(1 - cd2))
    save_text(q, filepath)
    return ans, q

def save_log_rootproduct_question(filepath):
    base = random.randint(2,9)
    r1, r2 = random.choice(EASY_INTS_NO_ZERO), random.choice(EASY_INTS_NO_ZERO)
    inside_pwr = abs(random.choice(VERY_EASY_INTS_NO_ZERO))
    coeff1 = (r1+r2)*(inside_pwr**2)
    coeff2 = -(r1*r2*(inside_pwr**2))
    q = f"The product of the real roots of the equation\n"
    q += f"$"+ r"(\log_" + f"{base}" + r"({x^" + f"{inside_pwr}" + "}))^2 "
    if coeff1 != 0:
        if coeff1 > 0:
            q += "-"
        else:
            q += "+"
        coeff1 = abs(coeff1)
        q += f" {coeff1}\log_{base}(" + r"{x}) = " + f"{coeff2}$"
    else:
        q += f"= {coeff2}$"
    q += f"\ncan be expressed as ${base}^a$\nFind a."
    save_text(q, filepath)
    return r1+r2, q

def save_no_soln_trigs_question(filepath):
    combs=[]
    terms = []
    safe_sines = [[0,2,-1],[1,2,-1],[1,0,-1],[2,0,-1],[0,2,1],[1,2,1],[1,0,1],[2,0,1]]
    safe_cos = [[2,0,-1],[2,1,-1],[0,1,-1],[0,2,-1],[2,0,1],[2,1,1],[0,1,1],[0,2,1]]
    for i in range(4):
        for j in range(4):
            for s in range(2):
                if i+j == 1 or i+j == 3:
                    if s == 0:
                        combs.append([i,j,-1])
                    else:
                        combs.append([i,j,1])
    scs = 0
    for i in range(3):
        if scs == 1:
            what = random.choice(safe_cos)
            while what in terms:
                what = random.choice(safe_cos)
            terms.append(what + [random.randint(1,5)])
        elif scs == 2:
            what = random.choice(safe_sines)
            while what in terms:
                what = random.choice(safe_sines)
            terms.append(what + [random.randint(1,5)])
        else:
            what = random.choice(combs)
            while what in terms:
                what = random.choice(combs)
            if set((3,0)).issubset(set(what)):
                scs = 2
            elif set((0,3)).issubset(set(what)):
                scs = 1
            terms.append(what + [random.randint(1,5)])

    def trig_func(val, terms):
        res = 0
        for term in terms:
            res += (np.sin(val)**term[0])*(np.cos(val)**term[1])*term[2]*term[3]
        return res

    #terms = [[3,0,1,3],[2,0,1,1],[2,0,1,9]]
    
    guess = 0
    rts = set()
    while guess < 2*math.pi:
        r = optimize.root(trig_func, guess,args=terms).x[0]
        if (0 <= r <= 2*math.pi) and abs(trig_func(r, terms)) < 10**-5:
            rts.add(round(r,4))
        guess += math.pi/10

    
    for t in terms:
        if t[2] == 1:
            t[2] = "+"
        elif t[2] == -1:
            t[2] = "-"
    
    q = "Find the number of real roots of\n$"
    expr = ""
    for i in range(3):
        expr += f"{terms[i][2]}{terms[i][3]}sin^{terms[i][0]}(x)cos^{terms[i][1]}(x)"
    if terms[0][2] == "+":
        expr = expr[1:]
    q += expr + "$"
    q += "\nFrom 0 <= x <= 2π."
    save_text(q, filepath)
    
    return len(rts), q

def save_simplest_proportion_question(filepath):
    base = random.choice([2,4,5])
    up = random.randint(1,base-1)
    dire = random.choice([-1,1])
    sym = "+" if dire == 1 else ""
    pwr = random.choice([2,3])
    ori = random.randint(2,10)*(base**pwr)
    q = f"A {random.choice(SMALL_OBJS)} has {'surface area' if pwr==2 else 'volume'} {ori} $m^{pwr}$.\nThe radius is now changed by {sym}{100*(dire*up/base)}%.\nWhat is the new {'surface area' if pwr==2 else 'volume'}?"
    save_text(q, filepath)
    return int(ori*(1+dire*up/base)**pwr), q

def save_partial_fraction_question(filepath):
    a, b = random_randints((1,5),2)
    A, B, C = [random.randint(-5,5) for _ in range(3)]
    up1 = A+B
    up2 = -2*A*b - B*(a+b) + C
    up3 = A*(b**2)+B*a*b - C*a
    down1 = (a+b)
    down2 = a*b
    if up1 == 0:
        up1 = ""
    else:
        up1 = str(up1) + "x^2"
    if up2 > 0:
        up2 = "+" + str(up2) + "x"
    elif up2 == 0:
        up2 = ""
    else:
        up2 = str(up2) + "x"
    if up3 > 0:
        up3 = "+" + str(up3)
    elif up3 == 0:
        up3 = ""
    else:
        up3 = str(up3)
    upexpr = up1 + up2 + up3
    if down1 > 0:
        down1 = "-" + str(down1) + "x"
    elif down1 == 0:
        down1 = ""
    else:
        down1 = "+" + str(abs(down1)) + "x"
    if down2 > 0:
        down2 = "+" + str(down2)
    elif down2 == 0:
        down2 = ""
    else:
        down2 = "-" + str(down2)
    downexpr = "(x^2" + down1 + down2 + f")(x-{b})"
    q = f"The expression\n"
    q += r"$\frac{" + upexpr + "}{" + downexpr + "}$\n"
    q += "can be decomposed into the form\n"
    q += r"$\frac{A}{(x-a)} + \frac{B}{(x-b)} + \frac{C}{(x-b)^2}$" + "\n"
    pos = random.randint(0,1)
    if pos:
        q += "Find A*B*C."
        ans = A*B*C
    else:
        q += "Find A+B+C."
        ans = A+B+C
    save_text(q, filepath)
    return ans, q

def save_integral_binominal_question(filepath):
    a = random.randint(1,5)
    b = random.randint(1,5)
    pwr = random.randint(5,9)
    ask = random.randint(2, pwr-2)
    q = f"Let f(x) = $" + r"\int_{0}^{x}(" + f"{a}+{b}t)^{pwr}dt$\n"
    q += f"Find the coefficient of the $x^{ask}$ term."
    save_text(q, filepath) 
    ans = Fraction(1, ask) * combination(pwr, ask - 1) * (a ** (pwr - ask + 1)) * (b ** (ask - 1))
    return ans, q

def save_log_quadratic_question(filepath):
    base = random.randint(2,5)
    k = random.randint(0,2)
    a = random.randint(2,5)
    A = random.choice(prime_factors(a*(base**k)))
    B = a*(base**k) / A
    r1 = random.randint(1,6)
    r2 = random.randint(-6,-1)
    b = -(A*r2 + B*r1)
    c = r1*r2
    q = "The real root of the equation\n"
    q += "$"+f"{a} * {base}" + "^{2x"
    if k != 0:
        q += f"+{k}"
    q += "}"
    if b != 0:
        if b > 0:
            q += "+"
        q += f"{int(b)}" + "*" + f"{base}^x"
    q += str(c) + "$"
    q += "\nCan be expressed as\n"
    q += r"$\log_{" + f"{base}" + r"}{n}$" + "\n"
    q += "Find n as a fraction."
    save_text(q, filepath)
    return Fraction(r1, A), q
    

if __name__ == "__main__":
    print(save_log_quadratic_question("foo.png"))
    

