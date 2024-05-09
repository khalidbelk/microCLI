##
## MicroCLI, 2024
## commands
## File description:
## commands
##

import src.microfs as mfs

def ls():
    try:
        mfs.exec_cmd(["ls"])
    except Exception as e:
        print(f"An error occurred: {e}")

def up(filename, outputname=None):
    try:
        command = ["up", filename]
        if outputname:
            command.append(outputname)
        mfs.exec_cmd(command)
    except Exception as e:
        print(f"An error occurred: {e}")

def rm(filename):
    try:
        command = ["rm", filename]
        mfs.exec_cmd(command)
    except Exception as e:
        print(f"An error occurred: {e}")

def save(filename, target=None):
    try:
        command = ["save", filename, target]
        mfs.exec_cmd(command)
    except Exception as e:
        print(f"An error occurred: {e}")

def show(filename):
    try:
        command = ["show", filename]
        mfs.exec_cmd(command)
    except Exception as e:
        print(f"An error occurred: {e}")

def rename(filename, newname):
    try:
        command = ["rename", filename, newname]
        mfs.exec_cmd(command)
    except Exception as e:
        print(f"An error occurred: {e}")

def version():
    try:
        command = ["version"]
        mfs.exec_cmd(command)
    except Exception as e:
        print(f"An error occurred: {e}")