import sys
from pathlib import Path
from colorama import Fore, Style, init
init(autoreset=True)

def folders_content(path, prefix=""):
    try:
        files=list(path.iterdir())
        for i, el in enumerate(files):
            connector = "└── " if i == len(files)-1 else "├── "
            if el.is_dir():
                print(f"{prefix}{Fore.BLUE}{connector}{el.name}")
                new_prefix = prefix + ("    " if i == len(files)-1 else "│   ")
                folders_content(el, new_prefix)
            else:
                print(f"{prefix}{Fore.GREEN}{connector}{el.name}")
    except:
        print("smth went wrong")

if __name__ == "__main__":
    while True:
        user_input = input("type folder`s full path: ").strip()
        p = Path(user_input)
        if not p.exists():
            print("path error try again ")
            continue
        if not p.is_dir():
            print("this isnt folder try again ")
            continue
        files = list(p.iterdir())
        if len(files) == 0:
            print("folder empty")
            continue
        if len(files) > 10:
            print("its too much try smth easier ")
            continue
        folders_content(p)
        break