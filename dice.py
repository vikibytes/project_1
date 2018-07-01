print("Would u like to roll the dice!")
print("If yes then type YES otherwise type NO")
import random
a = "YES"
while a == "YES":
    a = input()
    if (a == "YES"):
        print(random.randint(1, 6))
        print("Would u like to roll the dice one more time")
        print("If yes then type YES otherwise type NO")
        b = input()
        if (b == "YES"):
            print(random.randint(1, 6))
        else:
            print("Okay no problem , Have a good day!") 
    else: 
        print("Okay no problem , Have a good day!")

    

    
    
    
