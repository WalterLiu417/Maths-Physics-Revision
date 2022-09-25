from rref import rref
from get_matrix import get

def inv(m):
    newm = []
    for i in range(len(m)):
        row = []
        for j in range(len(m)):
            if j == i:
                row.append(1)
            else:
                row.append(0)
        print(list(m[i]) + row)
        newm.append(list(m[i]) + row)
    newm = newm
    res = rref(newm)
    print(res)
    inv = []
    for a in res:
        inv.append(a[len(m):])
    return inv
    
def main():
    print("Finds the inverse of a square matrix.")
    matrix = get()
    res = inv(matrix)
    print("++++++++\nResults:\n++++++++")
    for a in res:
        for b in a:
            print(b, end=" ")
        print()
    return True
