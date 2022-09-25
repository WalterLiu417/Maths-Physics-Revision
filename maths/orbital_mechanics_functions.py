'''Python functions for orbital mechanics'''
import sys, re, time, math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def input_and_format():
    vec1 = input("Enter vector 1 in ijk form eg. 1i+1j+1k:   ")
    vec1 = [int(ch) for ch in re.split("[ijk]", vec1)[:-1]]
    vec2 = input("Enter vector 2 in ijk form:   ")
    vec2 = [int(ch) for ch in re.split("[ijk]", vec2)[:-1]]
    return vec1, vec2


def crossproduct(vec1, vec2):
    return ((vec1[1]*vec2[2]-vec1[2]*vec2[1]),(vec1[2]*vec2[0]-vec1[0]*vec2[2]),(vec1[0]*vec2[1]-vec1[1]*vec2[0]))


def dotproduct(vec1, vec2):
    print(vec1, vec2)
    return sum([vec1[i]*vec2[i] for i in range(len(vec1))])


def simplify(vecs):
    return [[sum(vecs[j][i]) for j in range(len(vecs))] for i in range(len(vecs[0]))]

def ready_plot(func, a, b):
    formats = set(re.findall("sin|cos|tan|sinh|cosh|tanh|asin|acos|atan|asinh|acosh|atanh|log|e|pi", func))
    for fun in formats:
        func = func.replace(fun, "math." + fun)
    x_real, y_real = [], []
    count = 0
    while float(a)+count<float(b):
        x_real.append(float(a)+count)
        actual = func.replace("x", "(" + str(x_real[-1]) + ")")
        y_real.append(eval(actual))
        count += ((float(b)-float(a))/100)
    return x_real, y_real


def runge_kutta_classical():
    print("Obtains numerical solutions of expressions of the format (dy/dx) = f(x,y) by the classical RK4 method.\n")
    expr = input('''Enter python formatted function f(x,y).
Please include multiplication symbols eg. 2*x instead of 2x.
Exponentation should be entered as a**b -> a to the power b.
Inverse trig functions should be entered as asin, acosh etc.
Don't use cosec, cot etc.
Include brackets where possible.\n''')
    formats = set(re.findall("sin|cos|tan|sinh|cosh|tanh|asin|acos|atan|asinh|acosh|atanh|log|e|pi", expr))
    for func in formats:
        expr = expr.replace(func, "math." + func)
    a = input("Enter lower bound:   ")
    b = input("Enter upper bound:   ")
    y_i = float(input(f"Enter value for the solution at x = {a}:   "))
    h = float(input("Enter step size:   "))
    intermediate = input("Enter 0 if you want the intermediate values or 1 if not:   ")
    if intermediate == "0":
        intermediate = True
    else:
        intermediate = False
    t_count = float(a)
    A = [0, 0.5, 0.5, 1]
    B = [[0,0,0],[0.5,0,0],[0,0.5,0],[0,0,1]]
    C = [1/6, 1/3, 1/3, 1/6]
    x, y = [], []
    if str(t_count).find(".") != -1:
        decs = len(str(t_count)[str(t_count).find(".")+1:])
    if str(h).find(".") != -1:
        decs2 = len(str(h)[str(h).find(".")+1:])
    elif str(h).find("e"):
        decs2 = int(str(h)[str(h).find("e")+2:])
    max_decs = max(decs, decs2)
    thetime = time.time()
    while round(t_count, max_decs) <= float(b) - h:
        x.append(t_count)
        y.append(y_i)
        t = []
        for a_coeff in A:
            t.append(round(t_count + a_coeff * h, max_decs + 1))
        eval_expr_f1 = expr.replace("x", f"({t[0]})").replace("y", "(" + str(y_i) + ")")
        f_1 = eval(eval_expr_f1)
        eval_expr_f2 = expr.replace("x", f"({t[1]})").replace("y", "(" + str(y_i + 0.5 * h * f_1) + ")")
        f_2 = eval(eval_expr_f2)
        eval_expr_f3 = expr.replace("x", f"({t[2]})").replace("y", "(" + str(y_i + 0.5 * h * f_2) + ")")
        f_3 = eval(eval_expr_f3)
        eval_expr_f4 = expr.replace("x", f"({t[3]})").replace("y", "(" + str(y_i + h * f_3) + ")")
        f_4 = eval(eval_expr_f4)
        y_i += h * (C[0] * f_1 + C[1] * f_2 + C[2] * f_3 + C[3] * f_4)
        if intermediate:
            print(f"Value of solution at {round(t_count + h, max_decs)} = {y_i}")
        t_count += h
    if not intermediate:
        print(f"Value of solution at {round(t_count, max_decs)} = {y_i}")
    print(f"Time taken = {time.time()-thetime}")
    x.append(t_count)
    y.append(y_i)
    plot = input("Enter 0 to exit or 1 to plot the function:   ")
    if plot == "1":
        real = input("Enter 0 if the exact solution is known or 1 to continue:   ")
        if real == "0":
            expr_real = input("Enter the exact solution as a function in x:\n")
            x_real, y_real = ready_plot(expr_real)
        ball = mpatches.Patch(color = "blue", label="RK4 approximation")
        if real == "0":
            plt.plot(x_real, y_real, "r")
            ball_real = mpatches.Patch(color = "red", label="Actual solution")
            plt.legend(handles=[ball_real, ball])
        else:
            plt.legend(handles=[ball])
        plt.plot(x, y)
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.title("Close window to continue...")
        plt.show()


def get_equation(num):
    try:
        print("\n" + equations[num][0] + "\n\n" + equations[num][1] + "\n")
        return True
    except:
        print("No such equation (yet)")
        return False


def search_equation(word):
    c = 0
    for eq in equations:
        if set(word.lower().split(" ")).issubset(set(re.split("[ |(|)|'|-]", equations[eq][0].lower()))):
            print(eq + "\n" + equations[eq][0])
            c += 1
            time.sleep(0.6/c)
    if not c:
        inp = input("Nothing found. Enter 0 for a deep search or 1 to exit.")
        if inp == "0":
            for eq in equations:
                equ = equations[eq][0]
                for w in word.split(" "):
                    if equ.count(w):
                        print(eq + "\n" + equations[eq][0])
                        c += 1
                        time.sleep(0.6/c)
            print(c)
            if not c:
                print("Still nothing found...")
        



def display_equations_by_chapter(chap):
    c = 0
    for eq in equations:
        if chap.split(".") == eq.split(".")[:len(chap.split("."))] and len(eq.split(".")) <= len(chap.split("."))+1:
            print(eq + "\n" + equations[eq][0])
            c += 0.2
            time.sleep(0.3/c)
    if not c:
        print("Nothing found.")
    print()

def main():
    msg = '''0. Exit
1. Cross product
2. Dot product
3. Simplify
4. Classical Runge-Kutta method for numerical integration (RK4)
5. Get equation
6. Search for equation
7. Display equations by topic\n'''
    inp = input(msg)
    if inp == "0":
        print("Bye!")
        sys.exit()
    elif inp == "1":
        vec1, vec2 = input_and_format()
        print(crossproduct(vec1, vec2))
    elif inp == "2":
        vec1, vec2 = input_and_format()
        print(dotproduct(vec1, vec2))
    elif inp == "3":
        count = 1
        vecs = []
        while True:
            vec = input(f"Enter vector {count} in ijk form eg. 1i+1j+1k:   ")
            vec = [int(ch) for ch in re.split("[ijk]", vec)[:-1]]
            vecs.append(vec)
            if input("Press enter to continue or 0 to finish:   "):
                break
            count += 1
        print(simplify(vecs))
    elif inp == "4":
        runge_kutta_classical()
    elif inp == "5":
        get_equation(input("Enter equation number:   "))
    elif inp == "6":
        search_equation(input("Enter search keyword:   "))
    elif inp == "7":
        display_equations_by_chapter(input("Enter chapter number:   "))
    return True


def mainloop():
    while True:
        if main():
            a = input("0. Exit\n1. Continue\n")
            if a != "1":
                print("Bye!")
                break
        

#a, b=ready_plot("sin(7*x)-2*(e**x)+5", 0, 2)
#print(len(a), len(b))
#plt.plot(a,b)
#plt.show()  


if __name__ == "__main__":
    with open(r"C:\Users\walte\AppData\Local\Programs\Python\Python39\Data/orbital_mechanics_equations.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
        equations = {data[i].strip():[data[i+1].strip(),data[i+2].strip()] for i in range(0, len(data), 3)}
    mainloop()


