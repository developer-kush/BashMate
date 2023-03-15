import os
import pickle

LINE = '\n\n-------------------------------------------------------------------------------------'

SYSTEM = 'Win' if os.name == 'nt' else 'Linux' if os.name == 'posix' else 'Unknown'
if SYSTEM == 'Unknown': print("\nOS not Supported\n"); quit()

if SYSTEM == 'Win': PATH = f"C:/Users/{os.getlogin()}/.custom_script_data/"
else: PATH = f"/home/{os.getlogin()}/.custom_script_data/"

print("Installion Menu - ")
print("1. WorkMan - (WorkMan is a CLI based WorkSpace and Task Manager)")
print("2. Wizard - (Wizard is a CLI based OpenAI ChatBot)")
choice = int(input("Select Option : "))

if choice == 1:

    print("\n\n\033[1mInitiating Installation ...\033[0m")

    if SYSTEM == 'Linux' and not os.path.exists(f'/home/{os.getlogin()}/.custom_script_data'):
        os.mkdir(f'/home/{os.getlogin()}/.custom_script_data')
        print(f"\nCreated Folder : /home/{os.getlogin()}/.custom_script_data\n")
    elif SYSTEM == 'Win' and not os.path.exists(f'C:/Users/{os.getlogin()}/.custom_script_data'):
        os.mkdir(f'C:/Users/{os.getlogin()}/.custom_script_data')
        print(f"\nCreated Folder : C:/Users/{os.getlogin()}/.custom_script_data\n")
    else: print('\nStorage Folder Already Available\n')

    # ----------------------------------- SYSTEM VARS ------------------------------------
    SYSTEM_VARS = {
        "WSPACES" : {},
        "aliases" : {},
        "scripts" : {}
    }

    print("\n--------------------------  Installing Packages ---------------------------")
    print("\n-> Python_Dotenv\n")
    try: os.system('pip3 install python-dotenv')
    except: pass

    print(LINE)
    print("\n-> Colorama\n")
    try: os.system('pip3 install colorama')
    except: pass


    print("\n------------------------ Creating System Vars -----------------------------")

    if SYSTEM == 'Linux':
        with open(f"/home/{os.getlogin()}/.custom_script_data/WorkMan.bin",'wb+') as f:
            pickle.dump(SYSTEM_VARS, f)
            print("\nCreated System Vars")

    elif SYSTEM == 'Win':
        with open(f"C:/Users/{os.getlogin()}/.custom_script_data/WorkMan.bin",'wb+') as f:
            pickle.dump(SYSTEM_VARS, f)
            print("\n  Created System Vars")

    print("> System Vars Created")

elif choice == 2:

    print("\nInitiating Installation for Wizard ...")

    print("\n\n--------------------------  Installing Packages ---------------------------")
    
    print("\n-> Openai\n")
    # try: os.system('pip install openai')
    # except: pass

    print("\n------------------------ Creating System Vars -------------------------------\n")

    API_KEY = input("Enter API Key for Chat GPT : \nGet at : https://platform.openai.com/account/api-keys  \n > ").strip()

    SYSTEM_VARS = {
        "API_KEY" : API_KEY
    }

    with open(PATH+'Wizard.bin','wb+') as f:
        pickle.dump(SYSTEM_VARS, f)
        print("System Vars Created")

else:
    print("Invalid Option")