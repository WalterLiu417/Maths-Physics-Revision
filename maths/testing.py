for i in range(10):
    with open("test.txt", "a+") as file:
        file.write(str(i))