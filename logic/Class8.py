import datetime
from datetime import date


class Persona:
    nombre = ""
    altura = int
    fecha_nacimiento = date
    edad = ""

    def nombre(self):
        return self.nombre

    def altura(self):
        return self.altura

    def fecha_nacimiento(self):
        return self.fecha_nacimiento

    def edad(self):
        # obtenemos la fecha actual del sistema
        fecha_actual = datetime.date.today()
        # Calculamos la edad restando la fecha de la persona y la fecha actual
        self.edad = fecha_actual.year - self.fecha_nacimiento.year - (
                (fecha_actual.month, fecha_actual.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return self.edad


def introducirPersonna():
    # Pedimos los datos
    name = str(input("Introduce un nombre:"))
    altura = int(input("Introduce una altura:"))

    anio = int(input("Introduce año nacimiento:"))
    mes = int(input("Introduce mes nacimiento"))
    dia = int(input("Introduce dia nacimiento"))

    persona1 = Persona()
    persona1.nombre = name
    persona1.altura = altura
    persona1.fecha_nacimiento = datetime.date(anio, mes, dia)

    persona1.edad()

    return persona1


def main():
    persona1 = introducirPersonna()
    persona2 = introducirPersonna()
    persona3 = introducirPersonna()
    print("-- Introduce datos primera persona -- ")
    print(persona1.nombre, persona1.altura, persona1.edad, persona1.fecha_nacimiento)
    print("-- Introduce datos segunda persona -- ")
    print(persona2.nombre, persona2.altura, persona2.edad, persona2.fecha_nacimiento)
    print("-- Introduce datos tercera persona -- ")
    print(persona3.nombre, persona3.altura, persona3.edad, persona3.fecha_nacimiento)
