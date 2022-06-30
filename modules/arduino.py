try:
    import colorama as c
    from colorama import *
    import arduino-python3 as ar
    import time as t
except Exception as e :
    print("Please install the Missing Library  ")

def banner():
    print(Back.BLACK + Fore.GREEN, "Welcome to the Arduino Expoilt")

