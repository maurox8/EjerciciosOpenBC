class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def calificacion(self):
        if self.nota > 10:
            return"el alumno ha aprobado"
        else:
            return"el alumno ha reprobado"
        
    def __str__(self):
        return "El alumno {} ha obtenido una calificación de {} puntos, por lo tanto {}".format(self.nombre, self.nota, self.calificacion())
Mauro = Alumno("Mauro", 9)
Tifany = Alumno('Tifany', 11)
print(Mauro)
print(Tifany)
