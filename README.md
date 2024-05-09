# MicroCLI

This project was built to facilitate the process of interacting directly with your **BBC micro:bit** as a developer without tools like MakeCode or Python Editor.
It is built on top of [Microfs](https://github.com/ntoll/microfs), which has made the process easier.

## Requirements

- Python 3.11

## Usage

**Install dependencies** with :

`
    pip install -r requirements.txt
`

**Execute** the command:
```
  make
```

**Use** the program like this:
```
./microCLI [-ls | -up | -save | -rename | -rm | -v | --version | -h | --help] <FILENAME> <NEWNAME>
DESCRIPTION:

    ./microCLI                      : run your main.py file on the micro:bit. The file should be located at the root (same level as the microCLI).

    -h | --help                     : display this message and exit.
    -ls                             : show the files currently on the micro:bit filesystem.
    -up <FILENAME> <NEWNAME>        : upload a specific file into the micro:bit. Needs the path of the source file. Accepts an optional argument to name the file you want to upload differently.
    -save <FILENAME> <NEWNAME>      : save a file from the micro:bit to your device. The file name is required. You can optionally specify a new name for the file you want to save.
    -rm <FILENAME>                  : delete a file from the micro:bit.
    -rename <FILENAME> <NEWNAME>    : renames a file directly into the micro:bit. Needs the name of the file you want to rename and the new name. E.g.: -rename hello.py main.py
    -show <FILENAME>                : show the content of a file on the micro:bit (similar to Unix 'cat' command)
    -v | --version                  : shows the MicroPython version and some information about the connected micro:bit

```

## Why ?

I was trying to find out a way to directly test stuff on my micro:bit. After doing some research I found out that there wasn’t so many ways available to run python code on it aside of the MakeCode / Python Editor online tools. I eventually found a VS Code extension that did the job, but having to use the command palette to navigate every couple of minutes was a hassle (search for the right text to click on...etc), then I found out it was using MicroFS under the hood, so I said that's a good start to build an easy way test my stuff via terminal. While MicroFS is solid, the original repository was not so user-friendly for someone who would just like to quickly run his code into the device, since it's more focused on its pip package 'ufs', which is understandable, but I wanted something more straightforward and simpler. 

So I decided to create something that would suit my needs and make it simpler for others who might be in the same situation.


Main advantages:

- Quick Setup: Use a Makefile to build the CLI executable, focusing only on the commands you need.
- Easy Testing: Apply changes directly to your micro:bit's main.py file with a single command: **./microCLI**
- More intuitive usage & enhanced message.
- More recent & maintained.
- Includes more features such as file renaming and file content displaying (maybe more to be added).