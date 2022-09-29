import pyfiglet
from sys import exit, stdout
from random import randint
from time import sleep

def main():
    print(pyfiglet.figlet_format("Animate Typing"))
    print("Welcome to the Animate Typing Terminal Utility!")
    data = input("Enter what you want the computer to type: ")
    Comptype(data)


def Comptype(userinput):
    length_of_user_input = len(userinput)
    if userinput.replace(" ","").lower() == 'exit': 
        exit()
    else:
        for i in range(length_of_user_input):
            random_time_gap = randint(1,6)
            stdout.write(f"\r{userinput[:i+1]}")
            sleep(0.05*random_time_gap)
        print()


if __name__ == '__main__':
    while True:
        main()