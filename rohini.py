import random
a = random.randint(1,9)
b = random.randint(1,9)

sum = a + b
 
while True:
    print(a)
    print("+",b)
    ans = int(input("Answer:"))

    if ans == sum:
        print("very good")
        break
    else:
        print("Hey! Try again")
