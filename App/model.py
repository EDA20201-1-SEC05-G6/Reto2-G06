﻿"""
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
    categoryfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(categoryfile, encoding='utf-8'))
    
    for category in input_file:
        lista = category["id\tname"].split()
        mp.put (categoryId, int (lista [0]), " ".join(lista[1:len(lista)])

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
               'category_id': None,
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
    catalog['videos'] = lt.newList('SINGLE_LINKED')

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

    catalog['category_id'] = mp.newMap(16,
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
def addVideo (catalog, video):
    lt.addLast(catalog["videos", video])

def addTrendingDate (catalog, video):
    dic = catalog["trending_date"]
    presencia = mp.contains(dic, video["trending_date"])
    if presencia:
        entry = mp.get(dic, video["trending_date"])
        lista = me.getValue(enrty)
        lt.addLast(lista, video) 
    else:
        mp.put(dic, video["trending_date"], lt.newList(datastructure="SINGLE_LINKED"))
        entry = mp.get(dic, video["trending_date"])
        lista = me.getValue(enrty)
        lt.addLast(lista, video)

def addCategoryId ()
    
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
