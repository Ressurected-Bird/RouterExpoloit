try:
    from modules import *
    from colorama import *
    import colorama
except Exception as e:
    print(f'{e}')
print(Fore.BLACK+Fore.GREEN,"\t \t RouterExpolit")
print("\n \t\t By RessurectedBird")
print("\t 1.Arduino \t 2.Router")
print("\t 3. Rasberrypi\t 4. ")
option=int(input(">>>"*5))
if option==1:
    print("I'm in the If else")
if option==2:
    print("I'm in the else condiont")
if option==3:
    print(" I'm in the third option ")
