from random import *
import os
u_pwd = input("Enter a password")
pwd=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1',
'2','3','4','5','6','7','8','9','0']

password=""
while(password!=u_pwd):
	password=""
	for letter in range(len(u_pwd)):
	    guess_pwd = pwd[randint(0,17)]
	    password=str(guess_pwd)+str(pw)
	    print(password)
	    print(Please wait!!!)
	    os.system("cls")
print("UR Password is :",password)