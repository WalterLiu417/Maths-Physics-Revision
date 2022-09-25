from copy import deepcopy
def dotproduct(v1, v2):
    res = 0
    for i in range(len(v1)):
        res += v1[i]*v2[i]
    return res

def normsquared(v):
    res = 0
    for i in range(len(v)):
        res += v[i]**2
    return res

def scalarmul(s, v):
    for i in range(len(v)):
        v[i] *= s
    return v

def vecsubtract(v1, v2):
    res = []
    for i in range(len(v1)):
        res.append(v1[i]-v2[i])
    return res

def gram_schmidt(m):
    onbasis = list()
    for i in range(len(m)):
        resv = m[i]
        for j in range(i):
            dot = dotproduct(m[i], onbasis[j])
            leng = normsquared(onbasis[j])
            sub = scalarmul(dot/leng, onbasis[j])
            resv = vecsubtract(resv, sub)
        onbasis.append(deepcopy(resv))
    return onbasis

def normalize(m):
    removed = 0
    for i in range(len(m)):
        if normsquared(m[i-removed]) == 0:
            m.remove(m[i-removed])
            removed += 1
            continue
        m[i-removed] = scalarmul(1/(normsquared(m[i-removed]))**(1/2), m[i-removed])
    return m


def main():
    print("Gram-Schmidt Process for finding an orthonormal basis")
    matrix = []
    while True:
        inp = input("Input a vector seperated by spaces or press enter to finish:\n")
        if not inp:
            break
        else:
            matrix.append([float(a) for a in inp.split(" ")])
    res = gram_schmidt(matrix)
    print(res)
    orthonorm = normalize(res)
    print("++++++++\nResults:\n++++++++")
    for i in range(len(orthonorm)):
        print(f"Vector {i+1}:")
        for j in range(len(orthonorm[i])):
            print(orthonorm[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()