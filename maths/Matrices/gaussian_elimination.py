from fractions import Fraction
import rref


def myparse(chars, st):
    res = []
    astr = ""
    for a in st:
        if a in chars:
            res.append(astr)
            astr = ""
        elif a == "-":
            res.append(astr)
            astr = "-"
        else:
            astr += a
    res.append(astr)
    return res


def replace_zeroes(vars, m):
    for row in m:
        if set(row.keys()).issubset(vars) and set(row.keys()) != vars:
            for var in vars:
                if var not in list(row.keys()):
                    row[var] = 0
    return m


def keysort(m):
    res = []
    for a in m:
        ite = a.items()
        b = sorted(ite)
        res.append({key: Fraction(value) for (key, value) in b})
    return res


def real_augmatrix(m):
    real_augm = []
    the_order = list(m[0].keys())
    for entry in m:
        real_augm.append(list(entry.values()))
    return real_augm, the_order



def equations_valid(m):
    zeroes = False
    for row in m:
        inf = True
        for val in range(len(row)):
            if inf and val == len(row)-1:
                zeroes = True
            if row[val] != 0:
                inf = False
    if inf:
        print("The equations have infinite solutions.")
        return False
    if zeroes:
        print("The equations have no solutions.")
        return False
    return True


def substitution(rrefm, the_order):
    res = dict()
    for i in range(len(rrefm)):
        res[the_order[i]] = rrefm[i][-1]
    return res


def display_results(res):
    print("++++++++\nResults:\n++++++++\n")
    for (key, value) in res:
        print(str(key) + " = " + str(value))




def main():
    print("Uses gaussian elimination to solve n equations in n unknowns.")
    msg = "Enter a linear equation or press enter to exit.\n"
    vars = {"zz"}
    augmatrix = []
    while True:
        inp = input(msg)
        if not inp:
            break
        elif inp:
            if not inp.count("="):
                print("Not an equation")
                continue
            cur = set(a for a in inp if a.isalpha())
            vars = vars.union(cur)
            terms = myparse(["+", "="], inp)
            eqdict = dict()
            for a in terms:
                if len(a) == 2 and a[0] == "-" and a[1].isalpha():
                    eqdict[a[1]] = -1
                elif len(a) > 1 and a[-1].isalpha():
                    eqdict[a[-1]] = Fraction(a[:-1])
                elif len(a) == 1 and a.isnumeric():
                    eqdict["zz"] = Fraction(a)
                elif not a.isalpha() and a:
                    eqdict["zz"] = Fraction(a)
                elif a:
                    eqdict[a] = 1
            augmatrix.append(eqdict)
    augmatrix = replace_zeroes(vars, augmatrix)
    augmatrix = keysort(augmatrix)
    elim, the_order = real_augmatrix(augmatrix)
    elim = rref.rref(elim)
    if not equations_valid(elim):
        return False
    else:
        res = substitution(elim, the_order)
        display_results(res.items())
        return True

if __name__ == "__main__":
    main()