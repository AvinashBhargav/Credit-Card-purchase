#Credit Card Purchase
A =input("Enter Your Full Name:")
B =int(input("Enter Your Card Number:"))
C =int(input("Enter YOur Password:"))
D =10000 #Balance 
print('{}is your name Your card number is {}  and Your amount is {}'.format(A,B,D))

apple = 50
mango = 30
Ban  = 10

print ('Welcome to my super market')
cost = 0

a = int(input('How many Apples Your need:'))
b = int(input('How many Mango you need :'))
c = int(input('How many Ban you want :'))
cost = 50*a + 30*b + 10*c 


def trans(D):
    card =int(input('Enter Your card number'))
    if(card == B):
        pas = int(input("enter pass : "))
        if(pas == C):
            print(D)
            print(cost)
            D = D-cost
            print("Your cuurent balance : {}".format(D))
            print("Thanks for shoppping...")
            print("Apple : {} Mangoes : {} Banana : {}".format(a,b,c))
            print("---------------------------------------------------")
        else:
            trans(D)
        
    else:
        print("Card is invalid")
        trans(D) 

  
trans(D)
