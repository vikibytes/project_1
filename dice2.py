import random

def throw_dice():
   return (random.randint(1, 6))

a = []
sum = 0
for i in range(0, 10000):
    a = a + [throw_dice()]

def p_num(n):
    return (a.count(n)/10000)   

for i in range(1, 7):
   print(f"the probability of getting {i} is", p_num(i))
   sum = sum + p_num(i)


print(f"The probility is as expected {sum}")
print(a)
   
   




    
