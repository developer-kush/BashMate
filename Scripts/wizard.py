from cmd import Cmd
import openai 
import os
from dotenv import load_dotenv
import shutil
import textwrap
import pickle

cols, rows = shutil.get_terminal_size()

from colorama import Fore as F, Style as S

BOLD = '\033[1m'
NORM = '\033[0m'
REV = '\033[7m'

CLEAR = 'cls' if os.name == 'nt' else 'clear' if os.name == 'posix' else 'c'
if CLEAR == 'c': exit()

# ----------------------------------- Reading Sys Info -------------------------------- 

if os.name == 'posix': DATAPATH = f"/home/{os.getlogin()}/.custom_script_data/Wizard.bin"
else: DATAPATH = f"C:/Users/{os.getlogin()}/.custom_script_data/Wizard.bin"

try:
    with open(DATAPATH,'rb+') as f:
        SYS_INFO = pickle.load(f)
except:
    print("\n\nX Error in Reading System Settings")
    exit()

openai.api_key = SYS_INFO['API_KEY']

# -------------------------------------------------------------------------------------

os.system(CLEAR)

BANNER = [                                                                                
    f"{BOLD+F.CYAN} █     █░ ██▓▒███████▒ ▄▄▄       ██▀███  ▓█████▄ ",
    f"{BOLD+F.CYAN}▓█░ █ ░█░▓██▒▒ ▒ ▒ ▄▀░▒████▄    ▓██ ▒ ██▒▒██▀ ██▌",
    f"{BOLD+F.CYAN}▒█░ █ ░█ ▒██▒░ ▒ ▄▀▒░ ▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌",
    f"{BOLD+F.LIGHTBLUE_EX}░█░ █ ░█ ░██░  ▄▀▒   ░░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌",
    f"{BOLD+F.LIGHTBLUE_EX}░░██▒██▓ ░██░▒███████▒ ▓█   ▓██▒░██▓ ▒██▒░▒████▓ ",
    f"{BOLD+F.LIGHTBLUE_EX}░ ▓░▒ ▒  ░▓  ░▒▒ ▓░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒ ",
    f"{BOLD+F.BLUE}  ▒ ░ ░   ▒ ░░░▒ ▒ ░ ▒  ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒ ",
    f"{BOLD+F.BLUE}  ░   ░   ▒ ░░ ░ ░ ░ ░  ░   ▒     ░░   ░  ░ ░  ░ ",
    f"{BOLD+F.BLUE}    ░     ░    ░ ░          ░  ░   ░        ░    "
]
Banner = '\n\n' + ('\n'.join([i.center(cols+10," ")[:-10] for i in BANNER])) + '\n\n' + f"{BOLD + S.BRIGHT + F.CYAN}Wizard {F.RED}NEBULA{F.RESET}, {F.LIGHTBLUE_EX}Beholder{F.RESET} of the {F.CYAN}Answers".center(cols+40," ")

USERNAME = os.getlogin().upper()


WRAPPEROBJECT = textwrap.TextWrapper(width=cols-5)
def wrap(text):
    lines = text.split('\n')
    res = []
    for line in lines:
        res.append('\n  '.join(WRAPPEROBJECT.wrap(line)))
    return '\n  '.join(res)

class Interactor(Cmd):

    intro = Banner
    prompt = f" \n{F.RED+REV+BOLD} {USERNAME} {NORM}{BOLD} >{F.GREEN} \n\n"+'  '

    def __init__(self, messages):
        super().__init__()
        self.messages = messages
        self.model = "gpt-3.5-turbo"
        self.mode = "chat"

    def do_cls(self, args):
        """Clears the screen"""
        os.system(CLEAR)
        print(self.intro)
    do_clear = do_cls
    
    def default(self, line):
        """Chats with OpenAi models"""
        if line == "EOF": raise KeyboardInterrupt()

        if self.mode == "chat":
            messages.append({"role": "user", "content": line})

            try:
                chat = openai.ChatCompletion.create(
                    model=self.model, messages = messages
                )
            except openai.error.APIConnectionError as e:
                print(F.RED+"\nX Connection Could not be Established"); return
            except openai.error.RateLimitError as e:
                print(F.RED + f"\n X Rate Limit Exceeded : {F.CYAN}Consider upgrading your API key"); return
            reply = wrap(chat.choices[0].message.content.lstrip())
            messages.append({"role": "assistant", "content": reply})
            print("\n"+f"{F.LIGHTBLUE_EX + REV + BOLD} NEBULA {NORM + BOLD} >\n\n  "+ reply)
    
    def do_exit(self, arg): raise KeyboardInterrupt()

def save_chat(messages):
    print(f"\n{F.RED} X This Feature will {F.YELLOW}SOON{F.RED} be added")
    return

if __name__ == '__main__':

    messages = [{"role":"system","content":"Your are Doby. You extensively use emojis in your messages to make them more expressive."}]

    try:
        interactor = Interactor(messages)
        interactor.cmdloop()
    except KeyboardInterrupt as e:
        try:
            save = input(f"\n\n {F.RED}> Do you want to save the chat? [y/n] : ").lower()
            if save in 'yes':
                name = input(f"\n {F.BLUE}> Enter a name for the chat : ")
                save_chat(messages)
                input('\nPress Enter to Continue ...')
        except EOFError as e: pass
        except KeyboardInterrupt as e: pass
        os.system(CLEAR)
        exit()
    except ModuleNotFoundError as e:
        print(F.RED+f"\n X Module Not Found : {F.CYAN}Consider pip installing unavaillable modules")