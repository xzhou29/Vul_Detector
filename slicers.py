#!/bin/sh
import os
import platform
import Globals

def backward_slicer(filename):
    pass


def dg_slicer(filename):
    pass


def c_code_slicer_slicer(file_absolute_path):
    line_number = 45
    if platform.system() == "Linux":
        filename = file_absolute_path.split("/")[-1]
        file_dir = file_absolute_path.replace(filename, "")
        backup_path = filename.replace(".", "_")
        os.system("mkdir -p tmp")
        command = "cp " + file_absolute_path + " tmp/" + filename
        os.system(command)
        command = "./" +  Globals.config['Modules']['joern'] + "/joern-parse tmp/"
        os.system(command)
        # TODO - add condition for existing folder
        command = "python slicers/c_slicer_joern/parse_joern_output.py --code "\
                  + filename + " --line " \
                  + str(line_number) + " --output results/parsed_data/" \
                  + backup_path
        os.system(command)
        os.system("rm -r tmp")
        os.system("rm -r parsed")