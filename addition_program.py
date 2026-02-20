import tkinter as tk
import random

score = 0
time_left = 30
correct_answer = 0
time_up = True   

def new_question():
    global correct_answer

    if time_up:
        return

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(["+", "-", "*"])

    if operator == "+":
        correct_answer = num1 + num2
    elif operator == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    question_label.config(text=f"{num1} {operator} {num2} = ?")
    answer_entry.delete(0, tk.END)
    result_label.config(text="")
    
def check_answer():
    global score

    if time_up:
        return

    try:
        user_answer = int(answer_entry.get())

        if user_answer == correct_answer:
            score += 1
            score_label.config(text=f"Score: {score}")
            result_label.config(text="Correct!", fg="green")
            root.after(500, new_question)
        else:
            result_label.config(text="Wrong!", fg="red")
            answer_entry.delete(0, tk.END)

    except:
        result_label.config(text="Enter number!", fg="red")

def countdown():
    global time_left, time_up

    if not time_up:
        if time_left > 0:
            time_left -= 1
            timer_label.config(text=f"Time left: {time_left}")
            root.after(1000, countdown)
        else:
            result_label.config(text="Time's up!", fg="orange")
            answer_entry.config(state="disabled")
            time_up = True

def start_game():
    global time_up

    if not time_up:
        return

    time_up = False
    answer_entry.config(state="normal")
    new_question()
    countdown()

def restart_game():
    global score, time_left, time_up

    score = 0
    time_left = 30
    time_up = False

    score_label.config(text="Score: 0")
    timer_label.config(text="Time left: 30")
    result_label.config(text="")
    answer_entry.config(state="normal")

    new_question()
    countdown()
    
root = tk.Tk()
root.title("Math Practice")

score_label = tk.Label(root, text="Score: 0", font=("bold", 20))
score_label.pack(pady=5)

timer_label = tk.Label(root, text="Time left: 30", font=("bold", 20), fg="blue")
timer_label.pack(pady=5)

question_label = tk.Label(root, text="Click Start", font=("bold", 30))
question_label.pack(pady=10)

answer_entry = tk.Entry(root, font=("Arial", 30), state="disabled")
answer_entry.pack(pady=10)

check_button = tk.Button(root, text="Check", font=("bold", 14), command=check_answer)
check_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("bold", 25))
result_label.pack(pady=10)

start_button = tk.Button(root, text="Start", font=("bold", 14), bg="green", fg="white", command=start_game)
start_button.pack(pady=5)

restart_button = tk.Button(root, text="Restart", font=("bold", 14), bg="orange", fg="white", command=restart_game)
restart_button.pack(pady=5)


root.mainloop()
