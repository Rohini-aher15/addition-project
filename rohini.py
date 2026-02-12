import random

def generate_question():
    
    a = random.randint(1, 9)
    b= random.randint(1, 9)
    return a, b

def ask_question():
    a, b = generate_question()
    correct_answer = a + b

    while True:
        
        print("  {a}")
        print("+ {b}")
        print("----")

        try:
            student_answer = int(input("Your answer: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if student_answer == correct_answer:
            print("Very good! ")
            break
        else:
            print("Hey! Try again ")
        
def main():
    print("Welcome to Addition Practice!")
    print("Solve the problems. Press Ctrl+C to exit.\n")

    while True:
        ask_question()

if __name__ == "__main__":

    main()
