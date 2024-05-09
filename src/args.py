##
## MicroCLI, 2024
## args
## File description:
## args
##

from src.usage import usage
import src.commands as cmd

# Checks flags' parameters (E.g: -up parameter). "easycheck" is used for
# optional params (E.g: -up parameter optionalparam). So if it's true, it
# won't print and exit with an error but just return 0.
def check_argument(i, index, args, easycheck=False):
    if i + index >= len(args):
        if easycheck:
            return 1
        else:
            print('Error: Missing argument(s). Use --help for more information.')
            exit(84)
    return 0

# Define functions for each command
def handle_help(args, i):
    usage()
    exit(0)

def handle_ls(args, i):
    cmd.ls()

def handle_up(args, i):
    check_argument(i, 1, args)
    filename = args[i + 1]
    outputname = args[i + 2] if check_argument(i, 2, args, easycheck=True) != 1 else None
    cmd.up(filename, outputname)

def handle_rm(args, i):
    check_argument(i, 1, args)
    cmd.rm(args[i + 1])

def handle_save(args, i):
    check_argument(i, 1, args)
    filename = args[i + 1]
    targetname = args[i + 2] if check_argument(i, 2, args, easycheck=True) != 1 else None
    cmd.save(filename, targetname)

def handle_show(args, i):
    check_argument(i, 1, args)
    cmd.show(args[i + 1])

def handle_rename(args, i):
    check_argument(i, 2, args)
    cmd.rename(args[i + 1], args[i + 2])

def handle_version(args, i):
    cmd.version()

command_handlers = {
    '-h': handle_help,
    '--help': handle_help,
    '-ls': handle_ls,
    '-up': handle_up,
    '-rm': handle_rm,
    '-save': handle_save,
    '-show': handle_show,
    '-rename': handle_rename,
    '-v': handle_version,
    '--version': handle_version
}

def args_handler(args: list[str]):
    for i in range(len(args)):
        arg = args[i]
        if arg in command_handlers:
            command_handlers[arg](args, i)