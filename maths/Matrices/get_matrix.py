from fractions import Fraction

def get():
    matrix = []
    while True:
        inp = input("Input a row of a matrix seperated by spaces or press enter to finish:\n")
        if not inp:
            break
        else:
            matrix.append([Fraction(a) for a in inp.split(" ")])
    return matrix