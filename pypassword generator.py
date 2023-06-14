#PYPASSWORD GENERATOR
import random
def fun():
    numbers = ('1 2 3 4 5 6 7 8 9 0').split()
    alphabets = ('a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z').split()
    symbols = ('! @ # $ % ^ & * ( ) _ - + = . , < >').split()
    password = []
    num_count = int(input("How many numbers you want in your password:"))
    alpha_count = int(input("How many alphabets you want in your password:"))
    sym_count= int(input("How many symbols you want in your password:"))
    for i in range(0, num_count):
        password+= random.choice(numbers)
    for i in range(0,alpha_count):
        password+=random.choice(alphabets)
    for i in range(0,sym_count):
        password+=random.choice(symbols)
    random.shuffle(password)
    a =""
    for i in password:
        a+=i
    print(a)
fun()
again = input("Do you want to generate another password?(yes/no):")
while again!="no":
    fun()
    again = input("Do you want to generate another password?(yes/no):")
else:
    print("Thank you!")
    
