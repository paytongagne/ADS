import sys
sys.path.append(".")

from ads_libs.io_parse import convert_file_to_commands

class PointBasedManagementSystem:
    def __init__(self):
        self.data = {}
        self.arr = [0 for _ in range(16)]
    
    def nuevo(self, key):
        if key in self.data:
            raise ValueError("Conductor duplicado")
        self.data[key] = 15
        self.arr[15]+= 1
        
    def consultar(self, key):
        if key not in self.data:
            print(f"Puntos de {key}: {self.data[key]}")
        else:
            return self.data[key]
         
    def quitar(self, key, new_value):
        if key in self.data:
            if self.data[key] < new_value:
                self.arr[self.data[key]]-= 1
                self.data[key] = 0
                self.arr[0] += 1
            else:
                v = self.data[key] - new_value
                self.arr[self.data[key]]-= 1
                self.data[key] = v
                self.arr[v] += 1
        else:
            raise ValueError("Conductor inexistente")
        
    def cuantos_con_puntos(self, value):
        if 0 > value or 15 < value:
            raise ValueError("Puntos no validos")
        return self.arr[value]
        
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

    
    