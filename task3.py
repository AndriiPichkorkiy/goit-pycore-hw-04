import sys
from pathlib import Path, WindowsPath
from colorama import Fore, Style

# render deep nested folders
def render_tree():
    if sys.argv[1]:
        directory = Path(sys.argv[1])

        # check is the path exist and is the path is directory
        if not directory.exists():
            print(Fore.RED + f"The path {Fore.MAGENTA + sys.argv[1] + Fore.RED} is not exist"+ Style.RESET_ALL)
            return
        elif not directory.is_dir():
            print(Fore.RED + f"The path {Fore.MAGENTA + sys.argv[1] + Fore.RED} is not a directory"+ Style.RESET_ALL)
            return

        # render given directory's name
        print(Fore.YELLOW + directory.resolve().name + Style.RESET_ALL)
        
        # render tree
        recursion_folders(directory)
    else:
        print("Was given no path in the second argument")
        return

# sort pathes in order to files
def sort_path(path: Path) -> bool:
    return path.is_dir()

# using recursion
def recursion_folders(dir: WindowsPath, padding: int = "" ) -> None:
    # get nested folders
    sorted_list = [path for path in dir.iterdir()]

    # sort pathes in order to files
    sorted_list.sort(key=sort_path)

    # check is there more dirs in the list to pretty render the tree
    isThereDir = False
    for path in sorted_list:
        if path.is_dir():
            isThereDir = True
            break
    
    # render the tree
    for path in sorted_list:
        # ignore .venv/Lib path, there are a lot of files
        # comment the 2 lines below to render the full tree
        if(path.name == "Lib"):
            continue

        # render dir path
        if path.is_dir():
            # the different in the if/else block is how to render the padding in the next recursion call
            if path == sorted_list[-1]:
                print(f"{padding} ┕──▶  {Fore.CYAN}{path.name}{Style.RESET_ALL}")
                recursion_folders(path, padding = padding + "      ")
            else:
                print(f"{padding} ├──▶  {Fore.CYAN}{path.name}{Style.RESET_ALL}")
                paddingNew = padding + " │    " if isThereDir else padding  + "      "
                recursion_folders(path, padding = paddingNew)
        # render file path
        elif path.is_file():
            first_symbol = " │   " if isThereDir else "    "
            print(f"{padding}{first_symbol}{Fore.GREEN}{path.name}" + Style.RESET_ALL)

if __name__ == "__main__":
    render_tree()
