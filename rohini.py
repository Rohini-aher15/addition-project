import random

while True:
    num1 = random.randint(1, 9)
    num2 = ranpdom.randint(1, 9)
    
    correct_answer = num1 + num2("\n")

    print("  {num1}")
    print("+ {num2}")
    print("----")


    while True:
        try:
            answer = int(input("Your answer: "))
            
            if answer == correct_answer:
                print("Very good!\n")
                break   
            else:
                print("Hey! Try again.\n")
        
        except ValueError:
            print("Please enter a valid number.\n")
