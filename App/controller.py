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
 """

import config as cf
import model
import csv
import time
import tracemalloc


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():

    return model.newCatalog()

# Funciones para la carga de datos
def loadData(catalog):

    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    
    model.crearDicCategoryId(catalog)
    loadVideos(catalog)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory

def loadVideos(catalog):
    videosfile = cf.data_dir + 'video-samples/samples/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))

    for video in input_file:
        model.addVideo(catalog, video)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def consultar_id(dic, categoria):

    return model.consultar_id(dic, categoria)

def filtrar_req1(pais, id, dic, videos, sublista):

    return model.filtrar_req1(pais, id, dic, videos, sublista)

def filtrar_req2(pais,videos, dic, sublista):

    return model.filtrar_req2(pais, videos, dic, sublista)

def filtrar_req3(id, videos, dic, sublista):

    return model.filtrar_req3(id, videos, dic, sublista)

def filtrar_req4(dic, sublista, tag, videos, pais):

    return model.filtrar_req4(dic, sublista, tag, videos, pais)

#Funciones para medir tiempo y memoria

def getTime():
    
    return float(time.perf_counter()*1000)

def getMemory():

    return tracemalloc.take_snapshot()

def deltaMemory(start_memory, stop_memory):

    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0
    
    for stat in memory_diff:

        delta_memory = delta_memory + stat.size_diff

    delta_memory = delta_memory/1024.0

    return delta_memory
