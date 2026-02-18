import tkinter as tk
import random

# function to generate new question
def new_question():
    global a, b
    a = random.randint(1, 9)
    b = random.randint(1, 9)

    num1_label.config(text=str(a))

    op = operation.get()

    if op == "addition":
        symbol = "+"

    elif op == "subtraction":
        symbol = "-"
    else:
        op == "multiplication"
        symbol = " * "

    
    num2_label.config(text=symbol + " " + str(b))
    result_label.config(text="")
    answer_entry.delete(0, tk.END)

# function to check answer
def check_answer():
    try:
        user_answer = int(answer_entry.get())
    except:
        result_label.config(text="Enter a valid number")
        return
    
    op = operation.get()

    if op =="addition":
        num2_label.config(text=" + " + str(b))
        correct = a + b 
    
    elif op =="subtraction":
        num2_label.config(text=" - " + str(b))
        correct = a - b 
    
    elif op == "multiplication":
        num2_label.config(text=" * " + str(b))
        correct = a * b 
    
    if user_answer == correct:
        result_label.config(text="Correct!", fg = "green")
        root.after(1000,new_question)
        
    else:
        result_label.config(text=f"Wrong! ", fg = "red")
        answer_entry.delete(0,tk.END)
    
# GUI setup
root = tk.Tk()
root.title("Math Practice")

# operation option
operation = tk.StringVar(value="addition")

tk.Radiobutton(root, text="Addition", variable=operation, value="addition", command=new_question).pack(side="left")
tk.Radiobutton(root, text="Subtraction", variable=operation, value="subtraction",command=new_question).pack(side="left")
tk.Radiobutton(root, text="Multiplication", variable=operation, value="multiplication", command=new_question).pack(side="left")

num1_label = tk.Label(root, text="", font=("Arial", 24),width=4,anchor="e")
num1_label.pack()

num2_label = tk.Label(root, text="", font=("Arial", 24),width=4,anchor="e")
num2_label.pack()

line_label = tk.Label(root, text="------", font=("Arial", 24),width=4,anchor="e")
line_label.pack()

answer_entry = tk.Entry(root, font=("Arial", 24))
answer_entry.pack()

check_button = tk.Button(root, text="Check", command = check_answer)
check_button.pack()


result_label = tk.Label(root, text="", font=("Arial", 18))
result_label.pack()

# first question
new_question()
root.mainloop()