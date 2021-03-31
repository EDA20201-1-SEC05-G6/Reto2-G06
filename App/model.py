"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import csv
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
from DISClib.Algorithms.Sorting import shellsort as sha
from DISClib.Algorithms.Sorting import insertionsort as ia
from DISClib.Algorithms.Sorting import selectionsort as sa
from DISClib.Algorithms.Sorting import quicksort as qk
from DISClib.Algorithms.Sorting import mergesort as mg
from datetime import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog ():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'category_id': None,
               'country': None,
               "categories": None}

    """
    Esta lista contiene todo los libros encontrados
    en los archivos de carga.  Estos libros no estan
    ordenados por ningun criterio.  Son referenciados
    por los indices creados a continuacion.
    """
    catalog['videos'] = lt.newList(datastructure='ARRAY_LIST')

    """
    A continuacion se crean indices por diferentes criterios
    para llegar a la informacion consultada.  Estos indices no
    replican informacion, solo referencian los libros de la lista
    creada en el paso anterior.
    """

    """
    Este indice crea un map cuya llave es el identificador del libro
    """

    catalog['category_id'] = mp.newMap(3,
                                 maptype='CHAINING',
                                 loadfactor=6.0)

    catalog['country'] = mp.newMap(37,
                                 maptype='CHAINING',
                                 loadfactor=6.0)

    catalog['categories'] = mp.newMap(3, 
                                 maptype='CHAINING',
                                 loadfactor=6.0)

    return catalog
# Funciones para agregar informacion al catalogo
def addVideo (catalog, video):
    dic = {}
    dic ["video_id"] = video ["video_id"]
    dic ["trending_date"] = datetime.strptime (video ["trending_date"], "%y.%d.%m").date ()
    dic ["title"] = video ["title"]
    dic ["channel_title"] = video ["channel_title"]
    dic ["category_id"] = int (video ["category_id"])
    dic ["publish_time"] = datetime.strptime (video ["publish_time"], "%Y-%m-%dT%H:%M:%S.%fZ")
    dic ["tags"] = video ["tags"]
    dic ["views"] = int (video ["views"])
    dic ["likes"] = int (video ["likes"])
    dic ["dislikes"] = int (video ["dislikes"])
    dic ["country"] = video ["country"]
    lt.addLast(catalog["videos"], dic)

    pos = lt.size(catalog["videos"])

    addCategoryID(catalog, video, pos)
    addCountry(catalog, video, pos)


def crearDicCategoryId (catalog):
    dic = catalog["categories"]
    categoryfile = cf.data_dir + 'video-samples/samples/category-id.csv'
    input_file = csv.DictReader(open(categoryfile, encoding='utf-8'))

    for category in input_file:
        lista = category["id\tname"].split()
        llave = " ".join(lista[1:len(lista)])
        presencia = mp.contains(dic, llave)
        if not presencia: 
            mp.put(dic, llave, int(lista [0]))

def addCategoryID(catalog, video, pos):
    dic = catalog["category_id"]
    presencia = mp.contains(dic, video["category_id"])
    if presencia:
        entry = mp.get(dic, video["category_id"])
        lista = me.getValue(entry)
        lt.addLast(lista, pos) 
    else:
        mp.put(dic, video["category_id"], lt.newList(datastructure="SINGLE_LINKED"))
        entry = mp.get(dic, video["category_id"])
        lista = me.getValue(entry)
        lt.addLast(lista, pos)

def addCountry (catalog, video, pos):
    dic = catalog["country"]
    presencia = mp.contains(dic, video["country"])

    if presencia:
        entry = mp.get(dic, video["country"])
        lista = me.getValue(entry)
        lt.addLast(lista, pos)  
    else:
        mp.put(dic, video["country"], lt.newList(datastructure="SINGLE_LINKED"))
        entry = mp.get(dic, video["country"])
        lista = me.getValue(entry)
        lt.addLast(lista, pos)

# Funciones para creacion de datos

# Funciones de consulta  

def consultar_id(dic, categoria):

    entry = mp.get(dic, categoria)
    categoryID = me.getValue(entry)

    return categoryID

def filtrar_req1(pais, id, dic, videos, sublista):

    entry = mp.get(dic, pais)
    lista = me.getValue(entry)

    for pos in lt.iterator(lista):

        video = lt.getElement(videos, pos)
        
        if video["category_id"] == id:

            lt.addLast(sublista, video)

    quickSort(sublista, cmpVideosByViewsMayor)

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByViews(video1, video2):

    valor= None
    if video1["views"] < video2["views"]:
        valor= True
    
    else:
        valor= False

    return valor

def cmpVideosByViewsMayor(video1, video2):

    valor= None
    if video1["views"] > video2["views"]:
        valor= True
    
    else:
        valor= False

    return valor

def cmpVideosByID(video1, video2):

    valor= None
    if video1["video_id"] > video2["video_id"]:
        valor= True
    
    else:
        valor= False

    return valor

def cmpVideosByLikes(video1, video2):

    valor= None
    if video1["likes"] > video2["likes"]:
        valor= True
    
    else:
        valor= False

    return valor

# Funciones de ordenamiento
def insertionSort(sublista, cmpfunction):
    
    ia.sort(sublista, cmpfunction)

def selectionSort(sublista, cmpfunction):

    sa.sort(sublista, cmpfunction)

def shellSort(sublista, cmpfunction):

    sha.sort(sublista, cmpfunction)

def quickSort(sublista, cmpfunction):

    qk.sort(sublista, cmpfunction)

def mergeSort(sublista, cmpfunction):

    mg.sort(sublista, cmpfunction)
