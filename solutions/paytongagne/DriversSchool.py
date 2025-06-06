import sys

class Student:
    def __init__(self, name, surname="", phone=""):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.score = 0
        self.instructor = None

class Instructor:
    def __init__(self, name, surname="", phone=""):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.students = set()

class DrivingSchool:
    def __init__(self):
        self.students = {}
        self.instructors = {}

    # O(1) complexity - Assuming dictionary access and set operations are average O(1)
    def alta(self, A, P, surname_A="", phone_A="", surname_P="", phone_P=""):
        if P not in self.instructors:
            self.instructors[P] = Instructor(P, surname_P, phone_P)
            
        if A in self.students:
            prev_instructor = self.students[A].instructor
            if prev_instructor and prev_instructor in self.instructors:
                self.instructors[prev_instructor].students.discard(A)
        
        if A not in self.students:
            self.students[A] = Student(A, surname_A, phone_A)
        
        self.students[A].instructor = P
        self.instructors[P].students.add(A)

    # O(1) complexity
    def es_alumno(self, A, P):
        return f"{A} es alumno de {P}" if A in self.students and self.students[A].instructor == P else f"{A} no es alumno de {P}"

    # O(1) complexity
    def puntuacion(self, A):
        if A not in self.students:
            return "ERROR"
        return f"Puntuacion de {A}: {self.students[A].score}"

    # O(1) complexity
    def actualizar(self, A, N):
        if A not in self.students:
            return "ERROR"
        self.students[A].score += N

    # O(n log n) complexity due to sorting operation
    def examen(self, P, N):
        if P not in self.instructors:
            return []
        qualified = sorted([s for s in self.instructors[P].students if self.students[s].score >= N])
        return qualified

    # O(1) complexity
    def aprobar(self, A):
        if A not in self.students:
            return "ERROR"
        
        instructor = self.students[A].instructor
        if instructor and instructor in self.instructors:
            self.instructors[instructor].students.discard(A)
        
        del self.students[A]

def main():
    school = DrivingSchool()
    
    for line in sys.stdin:
        line = line.strip()
        if line == "FIN":
            print("---")
            continue
        
        parts = line.split()
        cmd = parts[0]
        args = parts[1:]
        
        try:
            if cmd == "alta":
                school.alta(*args)
            elif cmd == "es_alumno":
                result = school.es_alumno(*args)
                print(result)
            elif cmd == "puntuacion":
                result = school.puntuacion(*args)
                print(result)
            elif cmd == "actualizar":
                result = school.actualizar(*args)
                if result == "ERROR":
                    print("ERROR")
            elif cmd == "examen":
                students = school.examen(*args)
                print(f"Alumnos de {args[0]} a examen:")
                if students:
                    for student in students:
                        print(student)
            elif cmd == "aprobar":
                result = school.aprobar(*args)
                if result == "ERROR":
                    print("ERROR")
        except Exception as e:
            print("ERROR")

if __name__ == "__main__":
    main()
