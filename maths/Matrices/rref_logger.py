class Step:
    def __init__(self, name, matrix):
        self.name = name
        self.matrix = matrix

    def display(self):
        print(self.name)
        print("Matrix now:")
        for row in self.matrix:
            for entry in row:
                print(entry, end=" ")
            print()


class RREF_Steps:
    def __init__(self):
        self.steplist = []
        
    def addstep(self, name, matrix):
        self.steplist.append(Step(name, matrix))

    def display(self):
        for step in self.steplist:
            step.display()
            print()