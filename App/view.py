"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import map as mp
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar videos con mas views en un país correspondientes a una categoría")
    print("3- Consultar el video que más días estuvo trending en un país")
    print("4- Consultar el video que más días estuvo trending en una categoría")
    print("5- Consultar los videos con un tag especifico que tienen más likes")
    print("0- Salir")

def initCatalog():

    return controller.initCatalog()

def loadData(catalog):

    return controller.loadData(catalog)

def consultar_id(dic, categoria):

    return controller.consultar_id(dic, categoria)

def filtrar_req1(pais, id, dic, videos, sublista):

    return controller.filtrar_req1(pais, id, dic, videos, sublista)

def filtrar_req2(pais, videos, dic, sublista):

    return controller.filtrar_req2(pais, videos, dic, sublista)
catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        answer = loadData(catalog)

        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ", "Memoria [kB]: ", f"{answer[1]:.3f}")


    elif int(inputs[0]) == 2:

       sublista = lt.newList(datastructure="ARRAY_LIST")

       num_videos = int (input("Ingrese el número de videos que quiere que se presenten en su ranking-> "))
       if num_videos > lt.size(catalog["videos"]): print("El número ingresado excede el número total de videos")
        
       else:
           
           categoria = input ("Ingrese la categoría que quiere consultar-> ")
           id = consultar_id(catalog["categories"], categoria)
           
           pais = input("Ingrese el país que quiere consultar-> ")
           filtrar_req1(pais, id, catalog["country"], catalog["videos"], sublista)

           for pos in range(1, num_videos + 1):

               elemento = lt.getElement(sublista, pos)

               print("\n\nvideo " + str(pos))
               print("trending date: " + str(elemento["trending_date"]))
               print("title: " + elemento["title"])
               print("channel title: " + elemento["channel_title"])
               print("publish time: " + str (elemento["publish_time"]))
               print("views: " + str(elemento["views"]))
               print("likes: " + str(elemento["likes"]))
               print("dislikes: " + str(elemento["dislikes"]))
        
    elif int(inputs[0]) == 3:
        sublista = lt.newList(datastructure="ARRAY_LIST")

        pais = input("Ingrese el país que desea consultar-> ")
        video = filtrar_req2(pais, catalog["videos"], catalog["country"], sublista)

        print("\n\ntitle: " + str(video[0][0]))
        print("channel title: " + str(video[0][0]))
        print("country: " + str(video[0][2]))
        print("trending days: " + str(video[1]))



    else:
        sys.exit(0)
sys.exit(0)
