import tkinter as tk
import random

def new_question():
    global a, b
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    num1_label.config(text=str(a).rjust(4))
    num2_label.config(text="+ " + str(b).rjust(1))
    result_label.config(text="")
    answer_entry.delete(0, tk.END)

def check_answer(event=None):
    user_ans = answer_entry.get()

    if int(user_ans) == a + b:
        result_label.config(text="Very good", fg="green")
        win.after(1000,new_question)
    else:
        result_label.config(text="Try again", fg="red")
    answer_entry.delete(0,tk.END)
# main window
win = tk.Tk()
win.title("Addition App")
win.bind("Return>",check_answer)
num1_label = tk.Label(win, text="", font=("bold", 30))
num1_label.pack()

num2_label = tk.Label(win, text="", font=("bold", 30))
num2_label.pack()

line = tk.Label(win, text="------", font=("bold", 30))
line.pack()

answer_entry = tk.Entry(win, font=("bold", 20))
answer_entry.pack(pady=10)

check_btn = tk.Button(win, text="Check", command=check_answer)
check_btn.pack()



result_label = tk.Label(win, text="", font=("bold", 30))
result_label.pack()

new_question()

win.mainloop()