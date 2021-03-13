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

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def crearDicCategoryId ():
    categoryId = mp.newMap(16,
                           maptype='CHAINING',
                           loadfactor=2.0)
    categoryfile = cf.data_dir + 'video-samples/samples/category-id.csv'
    input_file = csv.DictReader(open(categoryfile, encoding='utf-8'))
    
    for category in input_file:
        lista = category["id\tname"].split()
        mp.put (categoryId, int (lista [0]), " ".join(lista[1:len(lista)]))

    return categoryId

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
               'video_id': None,
               'trending_date': None,
               'title': None,
               'channel_title': None,
               'category': None,
               'publish_time': None,
               'tags': None,
               'views': None,
               'likes': None,
               'country': None}

    """
    Esta lista contiene todo los libros encontrados
    en los archivos de carga.  Estos libros no estan
    ordenados por ningun criterio.  Son referenciados
    por los indices creados a continuacion.
    """
    catalog['videos'] = lt.newList(datastructure='SINGLE_LINKED')

    """
    A continuacion se crean indices por diferentes criterios
    para llegar a la informacion consultada.  Estos indices no
    replican informacion, solo referencian los libros de la lista
    creada en el paso anterior.
    """

    """
    Este indice crea un map cuya llave es el identificador del libro
    """
    catalog['video_id'] = mp.newMap(92817,
                                   maptype='CHAINING',
                                   loadfactor=4.0)

    catalog['trending_date'] = mp.newMap(1095,
                                   maptype='CHAINING',
                                   loadfactor=4.0)

    catalog['category'] = mp.newMap(16,
                                 maptype='CHAINING',
                                 loadfactor=2.0)

    catalog['tags'] = mp.newMap(92817,
                                 maptype='CHAINING',
                                 loadfactor=4.0)

    catalog['views'] = mp.newMap(92817,
                                 maptype='CHAINING',
                                 loadfactor=4.0)

    catalog['likes'] = mp.newMap(92817,
                                 maptype='CHAINING',
                                 loadfactor=4.0)

    catalog['country'] = mp.newMap(50,
                                 maptype='CHAINING',
                                 loadfactor=4.0)

    return catalog
# Funciones para agregar informacion al catalogo
def addVideo (catalog, DicCategoryId, video):
    lt.addLast(catalog["videos"], video)
    addCategory(catalog, DicCategoryId, video)
    addCountry(catalog, video)
    addLikes(catalog, video)
    addTags(catalog, video)
    addTrendingDate(catalog, video)
    addViews(catalog, video)

def addTrendingDate (catalog, video):
    dic = catalog["trending_date"]
    presencia = mp.contains(dic, video["trending_date"])
    if presencia:
        entry = mp.get(dic, video["trending_date"])
        lista = me.getValue(entry)
        lt.addLast(lista, video) 
    else:
        mp.put(dic, video["trending_date"], lt.newList(datastructure="SINGLE_LINKED"))
        entry = mp.get(dic, video["trending_date"])
        lista = me.getValue(entry)
        lt.addLast(lista, video)

def addCategory (catalog, dic, video):
    mapa = catalog["category"]
    entry = mp.get(dic, int (video["category_id"]))
    categoria = me.getValue(entry)
    
    presencia = mp.contains(mapa, categoria)
    if presencia:
        entry = mp.get(mapa, categoria)
        lista = me.getValue(entry)
        lt.addLast(lista, video) 
    else:
        mp.put(mapa, categoria, lt.newList(datastructure="SINGLE_LINKED"))
        entry = mp.get(mapa, categoria)
        lista = me.getValue(entry)
        lt.addLast(lista, video)

def addTags (catalog, video):
    dic = catalog["tags"]
    lista = video["tags"].split("|")

    for tag in lista:
        presencia = mp.contains(dic, tag)

        if presencia:
            entry = mp.get(dic, tag)
            lista = me.getValue(entry)
            lt.addLast(lista, video)   
        else:
            mp.put(dic, tag, lt.newList(datastructure="SINGLE_LINKED"))
            entry = mp.get(dic, tag)
            lista = me.getValue(entry)
            lt.addLast(lista, video)

def addViews (catalog, video):
    dic = catalog["views"]
    presencia = mp.contains(dic, int (video["views"]))

    if presencia:
        entry = mp.get(dic, int (video["views"]))
        lista = me.getValue(entry)
        lt.addLast(lista, video)  
    else:
        mp.put(dic, int (video["views"]), lt.newList(datastructure="SINGLE_LINKED"))
        entry = mp.get(dic, int (video["views"]))
        lista = me.getValue(entry)
        lt.addLast(lista, video)

def addLikes (catalog, video):
    dic = catalog["likes"]
    presencia = mp.contains(dic, int (video["likes"]))

    if presencia:
        entry = mp.get(dic, int (video["likes"]))
        lista = me.getValue(entry)
        lt.addLast(lista, video)  
    else:
        mp.put(dic, int (video["likes"]), lt.newList(datastructure="SINGLE_LINKED"))
        entry = mp.get(dic, int (video["likes"]))
        lista = me.getValue(entry)
        lt.addLast(lista, video)

def addCountry (catalog, video):
    dic = catalog["country"]
    presencia = mp.contains(dic, video["country"])

    if presencia:
        entry = mp.get(dic, video["country"])
        lista = me.getValue(entry)
        lt.addLast(lista, video)  
    else:
        mp.put(dic, video["country"], lt.newList(datastructure="SINGLE_LINKED"))
        entry = mp.get(dic, video["country"])
        lista = me.getValue(entry)
        lt.addLast(lista, video)

# Funciones para creacion de datos

# Funciones de consulta
def reqLab (catalog):
    mapa = catalog["likes"]
    llaves = mp.keySet(mapa)



# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
