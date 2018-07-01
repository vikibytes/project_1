print("            CAN YOU GUESS THE NUMBER!!!          ")
import random
b = input("Enter the lower limit of the range in which u want to guess the numbers")
c = input("Enter the upper limit of the range in which u want to guess the numbers")
a = "YES"
b = int(b)
c = int(c)
while a == "YES":
    number = random.randint(b, c)
    x = input("Enter your guess ")
    x = int(x)
    if x == number:
        print("Congrats ur guess is right and that too in the first try!!!")
    elif x > number:     
        print("the number you entered is greater than the golden number") 
    else:
        print("the number you entered is lesser than the golden number")
    count = 1    
    while x != number:
        x = input("Enter your guess")
        count = count + 1
        x =int(x)
        if abs(number-x)>=500:
            print("the guess is way off target")
        elif 200<abs(number - x)<500:    
            print("the guess is off target")
        elif 50<abs(number - x)<=200:
            print("the guess is slightly off target")
        elif 10<abs(number - x)<=50:
            print("You are close")
        elif 3<abs(number - x)<=10:
            print("You are very close")
        elif 0<abs(number - x)<=3:
            print("come on almost there")                
        elif x == number:
            print("Congrats ur guess is right and the number of guesses u took were", count)
        else:
            print("try again")
    if 15<count:
        print("U R Below Average")
    elif 10<=count<15:
        print("U R at par with pther users")
    elif 5<=count<10:
        print("U R Above Average")
    elif 1<count<=5:
        print("U R a genius!!!")
    else:
        print("U R extraordinary!! and 1 in 100000 people who played this game")
        
    a = input("Do u wanna play again if yes then type 'YES'")
    
    
            
                    
                
    
            
    
