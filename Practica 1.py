import graphviz as gv
import os
class Pelicula:
    def __init__(self,nombre,actores,year,genero):
        self.nombre = nombre
        self.actores = actores
        self.year = year
        self.genero = genero

lst_peliculas = []
lst_actores = []
lst_years = []
lst_generos = []

def Cargar_archivo():
    ruta = input("archivo de entrada: ")
    f = open(ruta,"r")
    datos = f.read()
    filas = datos.strip().split("\n")
    
    for fila in filas:
        partes = fila.split(";")
        nombre = partes[0].strip()
        actores = partes[1].split(",")
        year = partes[2].strip()
        genero = partes[3].strip()

        for i in range(len(actores)):
            actores[i] = actores[i].strip()
            actor = actores[i]
            if actor not in lst_actores:
                lst_actores.append(actor)

        if year not in lst_years:
            lst_years.append(year)

        if genero not in lst_generos:
            lst_generos.append(genero)
                
        lst_peliculas.append(Pelicula(nombre,actores,year,genero))
    print("Se ha cargado la informacion con exito")
        
def Mostrar_peliculas():
    print("**************Peliculas**************")
    for pelicula in lst_peliculas:
        print("Nombre: ",pelicula.nombre)
        print("Año: ", pelicula.year)
        print("Genero: ", pelicula.genero)
        print("*************************************")
    input("Enter para continuar")


def Mostrar_actores():
    seleccion = None
    print("**************Seleccion de pelicula**************")
    for pelicula in lst_peliculas:
        print(str(lst_peliculas.index(pelicula)+1)+".- "+pelicula.nombre)
    print("*************************************************")
    while True:
        try:
            seleccion = int(input("Selecciona una pelicula: "))-1
            break
        except:
            print("Seleccion no valida")
        
    if abs(seleccion) > len(lst_peliculas):
        print("Seleccion no valida")
        return
    
    pelicula_seleccionada = lst_peliculas[seleccion]
    print("Actores: ")
    for actor in pelicula_seleccionada.actores:
        print(" "+str(pelicula_seleccionada.actores.index(actor)+1)+".- "+actor)
    input("Enter para continuar")

def Filtrado_por_actor():
    try:
        actor_seleccionado = input("Escribe el nombre de un actor para desplegar sus peliculas: ")
        existe = lst_actores.index(actor_seleccionado.strip())
    except:
        print("No se ha encontrado un actor llamado así, revisa mayusculas y minusculas")
        return
        

    print("Peliculas en las que participa "+actor_seleccionado+": ")

    for pelicula in lst_peliculas:
        if actor_seleccionado in pelicula.actores:
            print(" Nombre: ",pelicula.nombre)
            print(" Año: ", pelicula.year)
            print(" Genero: ", pelicula.genero)
            print("*************************************")
    input("Enter para continuar")
    
def Filtrado_por_year():
    try:
        year_seleccionado = input("Escribe el año para desplegar sus peliculas: ")
        existe = lst_years.index(year_seleccionado.strip())
    except:
        print("No se ha encontrado peliculas para ese año")
        return

    print("Peliculas publicadas en el año "+year_seleccionado+": ")
    
    for pelicula in lst_peliculas:
        if pelicula.year == year_seleccionado:
            print(" Nombre: ",pelicula.nombre)
            print(" Año: ", pelicula.year)
            print("*************************************")
            
    input("Enter para continuar")


def Filtrado_por_genero():
    try:
        genero_seleccionado = input("Escribe el genero para desplegar sus peliculas: ")
        existe = lst_generos.index(genero_seleccionado.strip())
    except:
        print("No se ha encontrado un genero llamado así, revisa mayusculas y minusculas")
        return
        
    print("Peliculas con el género "+genero_seleccionado+": ")
    
    for pelicula in lst_peliculas:
        if pelicula.genero == genero_seleccionado:
            print(" Nombre: ",pelicula.nombre)
            print(" Genero: ", pelicula.genero)
            print("*************************************")
    
    input("Enter para continuar")

def Graficar():
    salida = '''digraph {
  rankdir="LR"\n'''
    ordenar_peliculas = '''subgraph peliculas {
    rank="same"\n'''
    ordenar_actores = '''subgraph actores {
    rank="same"\n'''
    
    for pelicula in lst_peliculas:
        salida += "N_"+pelicula.nombre.replace(" ","_")+'''[shape = "none" label=<
    <TABLE cellspacing = "0" border="0">
    <TR>
    <TD bgcolor="#FC9D9A" border="1" colspan = "2">
    <font color="white">
    '''+pelicula.nombre+'''
    </font>
    </TD>
    </TR>
    <TR>
    <TD border="1">
    '''+pelicula.year+'''
    </TD>
    <TD border="1">
    '''+pelicula.genero+'''
    </TD>
    </TR>
    </TABLE>>];\n'''
        ordenar_peliculas += "N_"+pelicula.nombre.replace(" ","_")+"\n"

    for actor in lst_actores:
        salida += "N_"+actor.replace(" ","_")+'''[shape = "none" label=<
    <TABLE cellspacing = "0" border="0">
    <TR>
    <TD bgcolor="#336699" border="1" colspan = "2">
    <font color="white">
    '''+actor+'''
    </font>
    </TD>
    </TR>
    </TABLE>>]\n'''
        ordenar_actores += "N_"+actor.replace(" ","_")+"\n"

    for pelicula in lst_peliculas:
        for actor in pelicula.actores:
            salida+= "N_"+pelicula.nombre.replace(" ","_")+"->N_"+actor.replace(" ","_")+";\n"
            
    ordenar_peliculas += "}\n"
    ordenar_actores += "}\n"
    salida += ordenar_peliculas + ordenar_actores + "}"
    s = gv.Source(salida, filename="grafica_de_peliculas", format="png")
    s.view()

print("""******Lenguajes formales y de programación******
*               Sección: LFP B+                *
*              Carnet: 202102894               *
*    Nombre: Richard Alexandro Married Arana   *
************************************************""")
input()
seleccion_mp = None

while seleccion_mp != "5":
    print("""********************************
*        Menu Principal        *
* 1.-Cargar archivo de entrada *
* 2.-Gestionar Películas       *
* 3.-Filtrado                  *
* 4.-Grafica                   *
* 5.-Salir                     *
********************************""")
    seleccion_mp = input("Elige una opcion: ")
    if seleccion_mp == "1":
        Cargar_archivo()
    elif seleccion_mp == "2":
        print("""***********Gestionar Peliculas***********
1.- Mostrar peliculas                 
2.- Mostrar actores
*****************************************""")
        eleccion = input("Elige una Opcion: ")
        if eleccion == "1":
            Mostrar_peliculas()
        elif eleccion == "2":
            Mostrar_actores()
        else:
            print("seleccion no valida")
    elif seleccion_mp == "3":
        print("""*******Filtrado*******
* 1.- Por actor      *
* 2.- Por año        *
* 3.- Por género     *
**********************""")
        eleccion = input("Elige una Opcion: ")
        if eleccion == "1":
            Filtrado_por_actor()
        elif eleccion == "2":
            Filtrado_por_year()
        elif eleccion == "3":
            Filtrado_por_genero()
        else:
            print("Seleccion no valida")
    elif seleccion_mp == "4":
        Graficar()
    elif seleccion_mp == "5":
        continue
    else:
        print("Seleccion no valida")
