from copy import deepcopy
from fractions import Fraction

from .rref_logger import RREF_Steps as Steps
from .get_matrix import get

steplogger = Steps()

def rref(m):
    global steplogger
    steplogger.addstep("Variables ordered in alphabetical order.\nStarting matrix:", deepcopy(m))
    col = 0
    row = 0
    while (col < len(m[0])) and (row < len(m)):
        pivot = None
        for findpivotincolumn in range(row, len(m)):
            if m[findpivotincolumn][col] != 0:
                pivot = m[findpivotincolumn][col]
                break
        if findpivotincolumn != row and pivot:
            m[findpivotincolumn], m[row] = m[row], m[findpivotincolumn]
            steplogger.addstep(f"Swapped row {findpivotincolumn+1} with row {row+1}", deepcopy(m))
            findpivotincolumn = row
        if pivot and pivot != 1:
            for item in range(len(m[findpivotincolumn])):
                m[findpivotincolumn][item] *= Fraction(1/pivot)
            steplogger.addstep(f"R{findpivotincolumn+1} = R{findpivotincolumn+1} * {1/pivot}", deepcopy(m))
        if pivot:
            for elimrow in range(len(m)):
                if elimrow == findpivotincolumn:
                    continue
                else:
                    mulfactor = m[elimrow][col]
                    for elimitem in range(len(m[elimrow])):
                        m[elimrow][elimitem] -= (m[findpivotincolumn][elimitem]*mulfactor)
                    if mulfactor != 0:
                        steplogger.addstep(f"R{elimrow+1} = R{elimrow+1} - R{findpivotincolumn+1} * {mulfactor}", deepcopy(m))
            row += 1
        col += 1
    print(f"{len(steplogger.steplist)} steps done.")
    if input("Enter 0 to show steps or press enter to continue   "):
        steplogger.display()
    return m


def main():
    global steplogger
    print("Converts a matrix into its Reduced Row Echelon Form.")
    matrix = get()
    res = rref(matrix)
    print("++++++++\nResults:\n++++++++")
    for a in res:
        for b in a:
            print(b, end=" ")
        print()
    return True

if __name__ == "__main__":
    main()
