import sys


def convert_file_to_commands(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]
    
def process_operations(test_case):
    return NotImplemented

def main():
    if len(sys.argv) < 2:
       raise Exception("Usage: python script.py <input_file>")

    input_file = sys.argv[1]
    operations = convert_file_to_commands(input_file)
    
    test_case = []

    for line in operations:
        if line == "FIN":
            if test_case:
                print("\n".join(process_operations(test_case)))
                print("---")
                test_case = []
        else:
            test_case.append(line)


if __name__ == "__main__":

    main()