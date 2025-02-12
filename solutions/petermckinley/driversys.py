#uses hashmap, all lookups are ~O(1)
#for counting number of drivers with points, uses array, O(1) lookup time
class DriversLiscenseSystem:
    def __init__(self):
        self.index = {}
        self.arr = [0] * 16
    
    def nuevo(self, dni):
        if dni in self.index:
            return ("ERROR: Conductor duplicado")
        self.index[dni] = 15
        self.arr[15] += 1
    
    def quitar(self, dni, puntos):
        if dni not in self.index:
            return ("ERROR: Conductor inexistente")
        self.arr[self.index[dni]] -= 1
        self.index[dni] -= puntos
        
        if(self.index[dni] < 0):
            self.index[dni] = 0
        if(self.index[dni] > 15):
            self.index[dni] = 15
        
        self.arr[self.index[dni]] += 1

    def consultar(self, dni):
        if dni not in self.index:
            return ("ERROR: Conductor inexistente")
        return ("Puntos de " + str(dni) + ": " + str(self.index[dni]))
    
    def cuantos_con_puntos(self, puntos):
        if puntos < 0 or puntos > 15:
            return ("ERROR: Puntos no válidos")
        return ("Con " + str(puntos) + " puntos hay " + str(self.arr[puntos]))


def process_input():
    system = DriversLiscenseSystem()
    output = []
    while True:
        command = input().strip()
        parts = command.split()
        op = parts[0]
            
        if op == "nuevo":
            output.append(system.nuevo(parts[1]))
        elif op == "quitar":
            output.append(system.quitar(parts[1], int(parts[2])))
        elif op == "consultar":
            output.append(system.consultar(parts[1]))
        elif op == "cuantos_con_puntos":
            output.append(system.cuantos_con_puntos(int(parts[1])))
        elif op == "FIN":
            output.append("---")
            break
        else:
            output.append("ERROR: Comando no válido\n")
    
    for line  in output:
        if line != None:
            print(line)

process_input()

"""nuevo 123A
nuevo 456B
nuevo 666
cuantos_con_puntos 15
cuantos_con_puntos 0
quitar 666 15
cuantos_con_puntos 0
quitar 456B 9
consultar 456B
quitar 123A 10
cuantos_con_puntos 5
quitar 456B 1
cuantos_con_puntos 5
FIN

Con 15 puntos hay 3
Con 0 puntos hay 0
Con 0 puntos hay 1
Puntos de 456B: 6
Con 5 puntos hay 1
Con 5 puntos hay 2
---"""


"""
nuevo 123A
nuevo 123A
cuantos_con_puntos 20
quitar 456B 2
FIN

ERROR: Conductor duplicado
ERROR: Puntos no válidos
ERROR: Conductor inexistente
---
"""
