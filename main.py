try:
    from modules import *
    from colorama import *
    import colorama
    import time
except Exception as e:
    print(f'{e}')
while(1):
    try:
        modules.check()
        print()
        print(Fore.BLACK+Fore.GREEN,"\t \t RouterExpolit")
        print("\n \t\t By RessurectedBird")
        print("\t1.Arduino \t2.Router")
        print("\t3. Rasberrypi\t4.Exit ")
        print("\n")
        option=int(input(">>>>>\t"))
        if option==1:
            print("I'm in the If else")
        if option==2:
            print("I'm in the else condiont")
        if option==3:
            print(" I'm in the third option ")
        if option==4:
            time.sleep(1)
            break
    except Exception as e :
        print(f"Unexpected Error {e}")
