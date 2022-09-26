from flask import Flask, request, render_template
from maths.questions import QUESTIONS
from maths.helperfuncs import *
from fractions import Fraction
import random
from PIL import Image

app = Flask(__name__)

import time


@app.route("/")
def root():
    with open("times.txt", "w") as file:
        file.write(str(time.time()) + "\n0\n0\n0\n0")
    return render_template("index.html")



@app.route("/question", methods=["POST", "GET"])
def question():
    with open("answer.txt","r") as file:
        the_answer = file.read().strip()
    msg = ""
    if the_answer.find("/"):
        the_answer = Fraction(the_answer)
    else:
        the_answer = int(the_answer)
    print(the_answer, "start ans")
    print(request, "a request")
    if request.method == "POST":
        correct = None
        answ = request.form["ans"]
        print(answ, "unput")
        try:
            b = Fraction(answ)
            print(answ, the_answer, Fraction(answ) == the_answer)
        except:
            correct= False
        if correct is None:
            if type(the_answer) == int:
                if int(answ) == int(the_answer):
                    msg=["The answer was correct!"]
                    correct = True
                else:
                    correct = False
            elif type(the_answer) == Fraction:
                if Fraction(answ) == the_answer:
                    msg=["The answer was correct!"]
                    correct = True
                else:
                    correct = False
        with open("times.txt", "r") as file:
            thetime, firsttime, num_questions, ans_time, correct_time = file.read().split("\n")
            thetime = float(thetime)
            num_questions = int(num_questions)
            ans_time = float(ans_time)
            correct_time = float(correct_time)
        if firsttime == "0":
            num_questions += 1
            ans_time = ans_time * (num_questions - 1) / num_questions + (time.time() - float(thetime)) / num_questions
            firsttime = "1"
        if not correct:
            with open("times.txt", "w") as file:
                st = str(thetime) + "\n" + firsttime + "\n" + str(num_questions) + "\n" + str(ans_time) + "\n" + str(correct_time)
                file.write(st)
            return render_template("question.html", msg=["The answer was incorrect!", f"Your average answer time: {ans_time}"])
        elif correct:
            correct_time = correct_time * (num_questions - 1) / num_questions + (time.time() - float(thetime)) / num_questions
            if firsttime == "0": ans_time = ans_time * (num_questions - 1) / num_questions + (time.time() - float(thetime)) / num_questions
            msg.append("This answer took " + str(time.time()-thetime) + " seconds!")
            msg.append(f"Your average answer time: {ans_time}")
            msg.append(f"Your average time to answer correctly: {correct_time}")
            msg.append("Number of questions: " + str(num_questions))
            with open("times.txt", "w") as file:
                st = str(thetime) + "\n" + firsttime + "\n" + str(num_questions) + "\n" + str(ans_time) + "\n" + str(correct_time)
                file.write(st)
            
            

    quest = random.choice(QUESTIONS)
    ans, q = quest("static/assets/foo.png")
    img = Image.open("static/assets/foo.png")
    height, width, _ = np.shape(img)
    with open("test2.html", "r") as file:
        data = file.read()
        start = data.find("<img")
        data = data[:start+40] + str(width/3) + data[start+40:start+50] + str(height/3) + data[start+50:]
    with open("templates/question.html", "w") as file:
        file.write(str(data))
    print(ans)
    with open("answer.txt", "w") as file:
        file.write(str(ans))
    with open("times.txt", "r") as file:
        data = file.read().split("\n")
    with open("times.txt", "w") as file:
        data[0] = str(time.time()) + ""
        data[1] = "0"
        file.write("\n".join(data))
    return render_template("question.html", msg=msg)




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)