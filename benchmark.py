#!/usr/bin/python3

from os import walk
import os
import os.path
import shlex
import subprocess
import sys
import logging

formatter = logging.Formatter("%(process)d - [%(asctime)s] : %(levelname)s -> %(message)s")
csvFormatter = logging.Formatter("%(message)s")

csv_logger = logging.getLogger("csv_logger")
csv_logger.setLevel(logging.DEBUG)

csv_handler = logging.FileHandler("results.csv")
csv_handler.setLevel(logging.DEBUG)
csv_handler.setFormatter(csvFormatter)

file_logger = logging.getLogger("file_logger")
file_logger.setLevel(logging.DEBUG)

stdout_logger = logging.getLogger("stdout_logger")
stdout_logger.setLevel(logging.DEBUG)

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

stdout_logger.addHandler(stdout_handler)

BINARY_PROGRAMS = [
    "greedy",
    "dynamic_programming",
]

INPUTS_DIR = "inputs"
TIMES_RUN = 13
PATH_FILES_INPUT_LIST = []

def log(message):
    file_logger.debug(message)            
    stdout_logger.debug(message)            

def list_files_input():    
    for (dirpath, _, filenames) in walk(INPUTS_DIR):
        for file in filenames:
            full_path = os.path.abspath(dirpath) + "/" + file
            PATH_FILES_INPUT_LIST.append(full_path)   


def run_code():
    csv_logger.addHandler(csv_handler)
    csv_logger.debug("Algorithm;Input;Solution;Time")

    for binary in BINARY_PROGRAMS:
        for input in PATH_FILES_INPUT_LIST:
            inputName = input.split("/")[-1][:-4]

            file_handler = logging.FileHandler(f"logs/{binary}_{inputName}.log")
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)

            if not os.path.exists(input):
                log(f"Input file: {input} not found")            
            else:
                cmd = shlex.split("./" + binary + " " + inputName + " " + input)

                times = []
                solutions = []

                for count_time in range(TIMES_RUN):
                    log(f"Binary: {binary} - Input file: {inputName} - Time {count_time+1}")            

                    process = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE,
                            universal_newlines=True)
                    stdout, stderr = process.communicate()            

                    if not stderr:
                        log(f"Time elapsed: {stdout}")

                        output = stdout.split(" ")
                        solutions.append(int(output[0]))
                        times.append(float(output[1]))
                    else:
                        print(stderr)

                time_average = sum(times) / len(times)
                solution_average = sum(solutions) / len(solutions)
                csv_logger.debug(f"{binary};{inputName};{solution_average};{time_average}")

def main():
    list_files_input()
    PATH_FILES_INPUT_LIST.sort()
    run_code()

if __name__ == "__main__":
    main()
