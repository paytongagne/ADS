def convert_file_to_commands(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]
    


