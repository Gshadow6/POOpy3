class Alumno:
    facultad = "FES Aragón"

    def __init__(self, nom, ed, carr):
        self.__nombre = nom #Un atributo se hace privado con __
        self.__edad = ed
        self.__carrera = carr