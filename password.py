#imports
from time import sleep
#info
print("Hi! and welcome to my first programm!\n-Created by Exsite-")
#variables
x = 1
chances = 3 # You can edit this to how many times you can have your password wrong.
pas = "cookie" # You can edit this to whatever you want, this is your password

while True:
    ww = input("Password:")
    if ww == pas:
        break
    print("Wrong! \nYou've still got %s chances" % (chances))
    if chances == 0:
        print("Programm is closing...")
        sleep(1.5)
        exit()
    chances = chances - 1
print("You're now in your programm!")
sleep(1)
#You can write You're code down here!
