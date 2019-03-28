import datetime
from datetime import date


class Persona:
    nombre = ""
    altura = ""
    fecha_nacimiento = date
    edad = ""

    def nombre(self):
        print(Persona.nombre)

    def altura(self):
        return Persona.altura

    def edad(self):
        # obtenemos la fecha actual del sistema
        fecha_actual = datetime.date.today()
        # Calculamos la edad restando la fecha de la persona y la fecha actual
        edad = fecha_actual.year - self.fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        print(edad)


def introducirPersonna():
    # name = str(input("Introduce un nombre:"))
    # altura = str(input("Introduce una altura:"))

    # anio = int(input("Introduce año nacimiento:"))
    # mes = int(input("Introduce mes nacimiento"))
    # dia = int(input("Introduce dia nacimiento"))

    persona1 = Persona()
    # persona1.fecha_nacimiento = datetime.date(anio, mes, dia)
    persona1.fecha_nacimiento = datetime.date(1996, 4, 5)
    print(persona1.fecha_nacimiento)
    persona1.edad()
    print(persona1.edad)


introducirPersonna()
