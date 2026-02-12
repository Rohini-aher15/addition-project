import random
while True:

    a = random.randint(0,9)
    b = random.randint(0,9)

 
    sum = a + b
    print(" ",a)
    print("+",b)
    print("----")

    ans = int(input("Answer:"))

    if ans == sum:
        print("very good")
        
    else:
        print("Hey! Try again")
        