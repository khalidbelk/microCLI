##
## MicroCLI, 2024
## usage
## File description:
## usage
##

def usage():
    print("./microCLI [-ls | -up | -save | -rename | -rm | -v | --version | -h | --help] <FILENAME> <NEWNAME>")
    print("")
    print("DESCRIPTION:")
    print("")
    print("     ./microCLI                      : run your main.py file on the micro:bit. The file should be located at the root (same level as the microCLI).")
    print("")
    print("     -h | --help                     : display this message and exit.")
    print("     -ls                             : show the files currently on the micro:bit filesystem.")
    print("     -up <FILENAME> <NEWNAME>        : upload a specific file into the micro:bit. Needs the path of the source file. Accepts an optional argument to name the file you want to upload differently.")
    print("     -save <FILENAME> <NEWNAME>      : save a file from the micro:bit to your device. The file name is required. You can optionally specify a new name for the file you want to save.")
    print("     -rm <FILENAME>                  : delete a file from the micro:bit.")
    print("     -rename <FILENAME> <NEWNAME>    : renames a file directly into the micro:bit. Needs the name of the file you want to rename and the new name. E.g.: -rename hello.py main.py")
    print("     -show <FILENAME>                : show the content of a file on the micro:bit (similar to Unix 'cat' command)")
    print("     -v | --version                  : shows the MicroPython version and some information about the connected micro:bit")
    print("")
