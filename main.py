try:
    from modules import *
    from colorama import *
    import colorama
    import time
except Exception as e:
    print(f'{e}')
while(1):
    
    print(Fore.BLACK+Fore.GREEN,"\t \t RouterExpolit")
    print("\n \t\t By RessurectedBird")
    print("\t 1.Arduino \t 2.Router")
    print("\t 3. Rasberrypi\t 4. ")
    print("\n")
    option=int(input(">>>>>\t"))
    if option==1:
        print("I'm in the If else")
    if option==2:
        print("I'm in the else condiont")
    if option==3:
        print(" I'm in the third option ")
    if option==5:
        time.sleep(1)
        break
