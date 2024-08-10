import random
num=['1','2','3','4','5','6','7','8','9']
letters=['a','b','c','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['!','@','#','$','%','^','&','*','(',')','?']
numbers=int(input("How many numbers would you like in your password :"))
letter=int(input("How many letters would you like in your password :"))
symbol=int(input("How many symbols would you like in your password :"))
password=[]
for i in range(1,numbers+1):
    char=random.choice(num)
    password.append(char)
for i in range(1,letter+1):
    char=random.choice(letters)
    password.append(char)      
for i in range(1,symbol+1):
    char=random.choice(symbols)
    password.append(char)
#print(password)     
random.shuffle(password)    
#print(password)
wanted_password=""
for i in password:
    wanted_password+=i
    
print(f"PASSWORD:  {wanted_password}")   