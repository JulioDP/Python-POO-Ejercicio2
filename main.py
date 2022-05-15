class Alumno:
    def __init__(self, alumno,nota):
        self.alumno = alumno
        self.nota = nota
        self.apro = False


    def aprovado(self):
        if self.nota >= 6:
            self.apro = True

    def calificacion(self):
        self.aprovado()
        if self.apro:
            print(f"El alumno { self.alumno} aprovobo la materia {self.nota}")
        else:
            print(f"El alumno {self.alumno} no aprovo la materia {self.nota}")

alumno  = Alumno("juan",9)
alumno.calificacion()


