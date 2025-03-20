import sys
sys.path.append(".")

from ads_libs.io_parse import convert_file_to_commands

class DrivingSchool:
    def __init__(self):
        self.students = {} # Space Complexity: O(n)
        self.instructors = {} # Space Complexity: O(n)
        
    def alta(self, student: str, instructor: str): # time complexity: O(1)
        instr: Instructor = None
        stud: Student = None
        prev_instr: Instructor = None
        prev_instr_name: str = None
        try:
            if instructor in self.instructors:
                instr = self.instructors[instructor]
            else:
                instr = Instructor(instructor)
                self.instructors[instructor] = instr
                
            if student in self.students:
                stud = self.students[student]
                prev_instr_name = stud.instructor
                prev_instr = self.instructors[prev_instr_name]
                
            else:
                stud = Student(student, instructor)
                self.students[student] = stud
            
            if prev_instr is not None:
                del prev_instr.students[student]
                
            instr.students[student] = stud
            stud.instructor = instructor
        except:
            raise ValueError("alta")

    def es_alumno(self, student: str, instructor: str):  # time complexity: O(1)
        instr: Instructor = None
        
        if instructor in self.instructors:
            instr = self.instructors[instructor]
        else:
            instr = Instructor(instructor)
            self.instructors[instructor] = instr
        
        try:
            if student in instr.students and instr.students[student] is not None:
                return f"{student} es alumno de {instructor}"
            else:
                return f"{student} no es alumno de {instructor}"
        except:
            raise ValueError("es_alumno")
        

    def puntuacion(self, student: str):  # time complexity: O(1)
        stud: Student = None
        try:
            stud = self.students[student]
            return f"Puntuacion de {student}: {stud.points}"
        except:
            raise ValueError("puntuacion")
        
    def actualizar(self, student: str, n: int):  # time complexity: O(1)
        stud: Student = None
        try:
            stud = self.students[student]
            stud.points += n
            return
        except:
            raise ValueError("actualizar")
        
    def examen(self, instructor: str, n: int):  # time complexity: O(m) where m is # of students of instructor
        stud: Student = None
        instr: Instructor = None
        studs = []
        try:
            if instructor in self.instructors:
                instr = self.instructors[instructor]
            else:
                instr = Instructor(instructor)
                self.instructors[instructor] = instr

            for std in instr.students:
                stud = instr.students[std]
                if stud.points >= n:
                    studs.append(stud.name)
            return studs
        except:
            raise ValueError("examen")

            
    def aprobar(self, student: str): # time complexity: O(1)
        stud: Student = None
        instr: Instructor = None
        try:
            if student in self.students:
                stud = self.students[student]
            else:
                return f"El alumno {student} no esta matriculado"
            del self.students[student]
            instr = self.instructors[stud.instructor]
            del instr.students[student]
        except:
            raise ValueError("aprobar")
            
            

        
class Student:
    def __init__(self, name, instructor):
        self.name = name
        self.surname = ""
        self.phone_num = 0
        self.points = 0
        self.instructor = instructor
        
    def update_info(self, name, surname, phone_num):
        self.name = name
        self.surname = surname
        self.phone_num = phone_num
        
class Instructor:
    def __init__(self, name):
        self.name = name
        self.surname = ""
        self.phone_num = 0
        self.students = {} # Space Complexity: O(n)
        
    def update_info(self, name, surname, phone_num):
        self.name = name
        self.surname = surname
        self.phone_num = phone_num
        
        

def process_operations(operations):
    school = DrivingSchool()
    output = []
    
    for op in operations:
        parts = op.split()
        command = parts[0]
        temp = []

        try:
            if command == "alta":
                output.append(school.alta(parts[1], parts[2]))
            elif command == "puntuacion":
                output.append(school.puntuacion(parts[1])) 
            elif command == "es_alumno":
                output.append(school.es_alumno(parts[1], parts[2])) 
            elif command == "actualizar":
                output.append(school.actualizar(parts[1], int(parts[2])))
            elif command == "examen":
                studs = school.examen(parts[1], int(parts[2]))
                output.append(f"Alumnos de {parts[1]} a examen:")
                for stud in studs:
                    output.append(stud)
            elif command == "aprobar":
                output.append(school.aprobar(parts[1]))
            elif command == "FIN":
                output.append("---")
                break
            else:
                output.append("ERROR: Comando no valido\n")
        except ValueError:
            output.append("ERROR")
            
    return [line for line in output if line is not None]
            
    


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

    
    
