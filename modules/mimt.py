try:
    from submodules.mimfun import * 
    import cowsay
    import colorama as c
    from colorama import *
    #import arduino-python3 as ar
    import time as t
    import os as s
except Exception as e :
    print("Please install the Missing Library  ")

def banner():
    message="Welcome to MAN IN THE MIDDLE ATTACK"
    cowsay.cow(message)

s.system("clear");
banner();
print("\n")

