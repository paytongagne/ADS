import sys
sys.path.append(".")

from ads_libs.io_parse import convert_file_to_commands

class PointBasedManagementSystem:
    def __init__(self):
        # Initializes storage for driver points and count array for points distribution
        self.data = {}
        self.arr = [0 for _ in range(16)]
        # Complexity: O(1)
    
    def nuevo(self, key):
        # Registers a new driver with maximum points, raises error if driver already exists
        if key in self.data:
            raise ValueError("Conductor duplicado")
        self.data[key] = 15
        self.arr[15] += 1
        # Complexity: O(1)
        
    def consultar(self, key):
        # Returns the current points of a driver, raises error if driver doesn't exist
        if key not in self.data:
            raise ValueError("Conductor inexistente")
        return self.data[key]
        # Complexity: O(1)
         
    def quitar(self, key, new_value):
        # Deducts points from a driver, adjusts points array accordingly, raises error if driver doesn't exist
        if key not in self.data:
            raise ValueError("Conductor inexistente")
        
        current_points = self.data[key]
        new_points = max(0, current_points - new_value)
        self.arr[current_points] -= 1
        self.arr[new_points] += 1
        self.data[key] = new_points
        # Complexity: O(1)
        
    def cuantos_con_puntos(self, value):
        # Returns the number of drivers with a specific points value, raises error if points are out of valid range
        if not (0 <= value <= 15):
            raise ValueError("Puntos no validos")
        return self.arr[value]
        # Complexity: O(1)
        
def process_operations(operations):
    system = PointBasedManagementSystem()
    output = []

    for op in operations:
        parts = op.split()
        command = parts[0]
        try:
            if command == "nuevo":
                system.nuevo(parts[1])
            elif command == "quitar":
                system.quitar(parts[1], int(parts[2]))
            elif command == "consultar":
                points = system.consultar(parts[1])
                output.append(f"Puntos de {parts[1]}: {points}")
            elif command == "cuantos_con_puntos":
                count = system.cuantos_con_puntos(int(parts[1]))
                output.append(f"Con {parts[1]} puntos hay {count}")
        except ValueError as e:
            output.append(f"ERROR: {e}")
    return output
    # Overall Complexity: O(n), where n is the number of operations

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
    # Overall Complexity: O(n), where n is the number of lines in the input file

if __name__ == "__main__":
    main()

