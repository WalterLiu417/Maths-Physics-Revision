from copy import deepcopy

from get_matrix import get

def determinant(m):
    sign = [1, -1]
    if len(m) == 1:
        return m[0][0]
    else:
        dets = []
        for fri in range(len(m[0])):
            them = deepcopy(m[1:])
            for row in them:
                row.pop(fri)
            dets.append(determinant(them))
        det = 0
        for fri in range(len(m[0])):
            det += (m[0][fri]*sign[fri%2]*dets[fri])
        return det


def main():
    print("Finds the determinant of a matrix.")
    matrix = get()
    for m in matrix:
        if len(matrix) != len(m):
            print("Not a square matrix.")
            return False
    det = determinant(matrix)
    print(f"Determinant = {det}")
    return True

if __name__ == "__main__":
    main()