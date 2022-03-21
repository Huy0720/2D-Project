import os
import sys
import time
import argparse

if __name__ == "__main__":
    NO_OF_VARIABLES = 0

    parser = argparse.ArgumentParser(prog="main.py", usage='python %(prog)s [options] path', description="Parse the specified CNF file based on the input directory/file path that consists of the boolean satisfiability assignment (SAT) problem to be solved.")
    parser.add_argument('Filepath', metavar='path', type=str, help='the path to the CNF file to be parsed')
    args = parser.parse_args()
    input_path = args.Filepath
    filename = os.path.abspath(input_path)
    if not os.path.isfile(filename):
        print('The file specified by the path does not exist! Quitting...')
        sys.exit()

    output_list = []
    variables_list = []

    with open(filename) as f:
        data = f.readlines()

        for line in data:
            if line[0] == "p":
                line = line.split(" ")
                NO_OF_VARIABLES = line[2]
            elif not (line[0] == "c" or line == "\n"):
                output_list.append(line.split("\n")[0][:-1].split())
                line = line.split(" ")

                for var in line[:-1]:
                    if (var != "0" or var != "\n") and not (
                        abs(int(var)) in variables_list
                    ):
                        variables_list.append(abs(int(var)))

# Kosaraju's algorithm 
start = time.time()
kosaraju = Kosaraju(NO_OF_VARIABLES, output_list)
print(kosaraju.sat_solve())
end = time.time()
duration = format(end - start, '.22g')
print("Time taken for Kosaraju's algorithm: ", duration)
