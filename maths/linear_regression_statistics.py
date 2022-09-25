# Finds the best fit line using statistical formulae
# By Walter Liu

import statistics
from matplotlib import pyplot as plt
def line_of_best_fit(x, y):
	xbar = statistics.mean(x)
	ybar = statistics.mean(y)
	x2bar = statistics.mean([i**2 for i in x])
	y2bar = statistics.mean([i**2 for i in y])
	xybar = statistics.mean([x[i]*y[i] for i in range(len(x))])
	Vx = x2bar - xbar**2
	Vy = y2bar - ybar**2
	cov = xybar - xbar*ybar
	m = cov/Vx
	c = ybar - m*xbar
	r = cov/((Vx*Vy)**(1/2))
	return m, c, r**2


def get_x_and_y(data):
	xy = data.split(None)
	x = [float(xy[a]) for a in range(len(xy)) if a%2 == 0]
	y = [float(xy[a]) for a in range(len(xy)) if a%2 == 1]
	return x, y


def get_input_x_and_y():
	x, y = [], []
	while True:
		xy = input("Enter x,y in this form or press enter to exit:   ")
		if not xy:
			break
		else:
			xi, yi = int(xy.split(",")[0]), int(xy.split(",")[1])
			x.append(xi)
			y.append(yi)
	return x, y




def main():
	select = input('''[0] Exit
[1] Use file
[2] Input data
''')
	if select == "0":
		return False
	elif select == "1":
		filename = repr(input("Enter full file path:   "))
		with open(filename, "r") as file:
			data = file.read()
		x, y = get_x_and_y(data)
	elif select == "2":
		x, y = get_input_x_and_y()

	m, c, r2 = line_of_best_fit(x, y)
	sign = "+" if c>0 else "-"
	print(f"Line: y = {round(m,3)}x {sign} {abs(round(c, 3))}\nR^2 value: {round(r2, 5)}")

if __name__ == "__main__":
	main()
