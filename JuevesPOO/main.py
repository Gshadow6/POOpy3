from cosas import Autor, Libro, Alumno
def main():
    l1 = Libro.libro_planeta("El perfume", Autor("Patrik", "Ps"), 2000)
    print(l1)

    #el codigo para cambiar el pseudonimo
    l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
    print(l1)

    print("----Herencia----")
    al1= Alumno("Jose", 20, "23232", "ICO", 9)
    al1.nombre= "Pepe"
    print(vars(al1))

main()