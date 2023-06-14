from cosas import Alumno

def main():
    """
    al1 = Alumno()
    print(al1)
    al2 = Alumno()
    print(al2)
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)

    print("----Cambiar atributo de instancia----")
    al1.facultad = "FES Aragón EdoMex"
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)

    print("----Cambiar atributo de clase----")
    Alumno.facultad = "FES Aragón EdoMex"
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)

    print("-----Un vistazo a los objetos----")
    print(vars(al1))
    print(vars(al2))

    print("----Modificar atributos publicos----")
    al1.edad= 999
    print(vars(al1))
    print(vars(al2))
    """
    #ErrorGit
    al1= Alumno("Diego", 19, "ICO")
    al2= Alumno("Montse", 20, "Derecho")
    print(vars(al1))
    al1.__edad= 333
    print(al1.__edad)
    print(vars(al1))
main()