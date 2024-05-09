##
## MicroCLI, 2024
## main
## File description:
## main
##

from sys import argv, exit
import src.microfs as mfs

from src.args import args_handler

# Basic ./microCLI command, runs the main.py located at the root on your micro:bit
def run():
    try:
        mfs.up("main.py")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(argv) == 1:
        run()
    else:
        args = args_handler(argv[1:])
    exit(0)