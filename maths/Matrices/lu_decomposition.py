from get_matrix import get

def upper(m):
    elems = []
    for i in range(len(m)):
        pivot = m[i][i]
        for j in range(i+1, len(m)):
            if j == i or pivot == 0:
                continue
            else:
                mul = -m[j][i]/pivot
                mat = []
                for a in range(len(m)):
                    row = []
                    for b in range(len(m[0])):
                        if a == b:
                            row.append(1)
                        elif a == j and b == i:
                            row.append(-mul)
                        else:
                            row.append(0)
                    mat.append(row)
                elems.append(mat)
                for k in range(len(m[j])):
                    m[j][k] += m[i][k]*mul
    return m, elems


def superimpose(invelems):
    res = []
    for a in range(len(invelems[0])):
        row = []
        for b in range(len(invelems[0][0])):
            if a == b:
                row.append(1)
            else:
                row.append(0)
        res.append(row)
    for elem in invelems:
        for a in range(len(elem)):
            for b in range(len(elem[0])):
                if a != b and elem[a][b] != 0:
                    res[a][b] = elem[a][b]
    return res




def main():
    print("Decomposes a matrix by the equation A = LU, where L is a lower triangular matrix and U is an upper triangular matrix.")
    matrix = get()
    u, invelems = upper(matrix)
    l = superimpose(invelems)
    print("++++++++\nResults:\n++++++++")
    print("The lower triangular matrix:")
    for a in l:
        for b in a:
            print(b, end=" ")
        print()
    print("The upper triangular matrix:")
    for a in u:
        for b in a:
            print(b, end=" ")
        print()
    return True

if __name__ == "__main__":
    main()