import sys
sys.path.append(".")

from ads_libs.io_parse import convert_file_to_commands


class LicenseSystem:
    def __init__(self):
        self.drivers = {}  # Stores drivers and their points
        # Tracks number of drivers per points
        self.points_count = {i: 0 for i in range(16)} # O(16)

    def nuevo(self, dni): # O(1)
        if dni in self.drivers:
            raise ValueError("Conductor duplicado")
        self.drivers[dni] = 15
        self.points_count[15] += 1

    def quitar(self, dni, puntos): # O(1)
        if dni not in self.drivers:
            raise ValueError("Conductor inexistente")

        current_points = self.drivers[dni]
        self.points_count[current_points] -= 1
        new_points = max(0, current_points - puntos)
        self.drivers[dni] = new_points
        self.points_count[new_points] += 1

    def consultar(self, dni): # O(1)
        if dni not in self.drivers:
            raise ValueError("Conductor inexistente")
        return self.drivers[dni]

    def cuantos_con_puntos(self, puntos): # O(1)
        if puntos < 0 or puntos > 15:
            raise ValueError("Puntos no validos")
        return self.points_count[puntos]


def process_operations(operations): # O(p), p is the number of operaitons
    system = LicenseSystem()
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
