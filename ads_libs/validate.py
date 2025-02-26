import sys
from termcolor import colored

def validate_output(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
    
    if lines1 == lines2:
        print(colored("Outputs are identical", "green"))
    else:
        print(colored("Outputs differ", "red"))
        for i, (l1, l2) in enumerate(zip(lines1, lines2), start=1):
            if l1 != l2:
                print(colored(f"Difference at line {i}:\nExpected: {l1.strip()}", "yellow"))
                print(colored(f"Got: {l2.strip()}", "cyan"))


if __name__ == "__main__":

    if len(sys.argv) < 3:
        raise Exception("Usage: python script.py <input_file1> <input_file2>")
    
    validate_output(sys.argv[1], sys.argv[2])