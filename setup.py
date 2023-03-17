import os
import pickle

LINE = '\n\n-------------------------------------------------------------------------------------'
BOLD = '\033[1m'

SYSTEM = 'Win' if os.name == 'nt' else 'Linux' if os.name == 'posix' else 'Unknown'
if SYSTEM == 'Unknown': print("\nOS not Supported\n"); quit()

if SYSTEM == 'Win': PATH = f"C:/Users/{os.getlogin()}/.custom_script_data/"
else: PATH = f"/home/{os.getlogin()}/.custom_script_data/"

if SYSTEM == 'Linux' and not os.path.exists(f'/home/{os.getlogin()}/.custom_script_data'):
    os.mkdir(f'/home/{os.getlogin()}/.custom_script_data')
    print(f"\nCreated Folder : /home/{os.getlogin()}/.custom_script_data\n")
elif SYSTEM == 'Win' and not os.path.exists(f'C:/Users/{os.getlogin()}/.custom_script_data'):
    os.mkdir(f'C:/Users/{os.getlogin()}/.custom_script_data')
    print(f"\nCreated Folder : C:/Users/{os.getlogin()}/.custom_script_data\n")
else: print('\nStorage Folder Already Available\n')

print("Installion Menu - ")
print("1. WorkMan - (WorkMan is a CLI based WorkSpace and Task Manager)")
print("2. Wizard - (Wizard is a CLI based OpenAI ChatBot)")
choice = int(input("Select Option : "))

if choice == 1:

    print(f"\n\n{BOLD}Initiating Installation for Workman...\033[0m")

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

    if os.path.exists(PATH+"WorkMan.bin"):
        print("\nAlready Exists, Recreate ? [y/n]")
        if input() in 'yes':
            with open(PATH+"WorkMan.bin",'wb+') as f:
                pickle.dump(SYSTEM_VARS, f)
                print("\n  Created System Vars")
    else:
        with open(PATH+"WorkMan.bin",'wb+') as f:
            pickle.dump(SYSTEM_VARS, f)
            print("\n  Created System Vars")

    print("Installation Done. Retry if there are installation issues.\n\n")

elif choice == 2:

    print(f"\n\n{BOLD}Initiating Installation for Wizard ...\n")

    print("\n\n--------------------------  Installing Packages ---------------------------")
    
    print("\n-> Openai\n")
    try: os.system('pip install openai')
    except: pass

    print("\n---------------------- Creating directories and System Vars ------------------\n")

    if not os.path.exists(PATH+"Wiz_Chats/"):
        os.mkdir(PATH+"Wiz_Chats/")
        print("\nWiz Chats Directory Created\n")

    API_KEY = input("Enter API Key for Chat GPT : \n\nGet at : https://platform.openai.com/account/api-keys  \n > ").strip()

    SYSTEM_VARS = {
        "API_KEY" : API_KEY,
        "CHATS" : set()
    }

    if os.path.exists(PATH+"Wizard.bin"):
        if input("") in 'yes': 
            with open(PATH+'Wizard.bin','wb+') as f:
                pickle.dump(SYSTEM_VARS, f)
                print("System Vars Created")
    else:
        with open(PATH+'Wizard.bin','wb+') as f:
            pickle.dump(SYSTEM_VARS, f)
            print("System Vars Created")


else:
    print("Invalid Option")