# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:19:27 2020

@author: CEC
"""

import pandas as pd
titulos = pd.read_csv('data/titles.csv' )
print(titulos.head(10))
print("\n"*2)
elenco = pd.read_csv('data/cast.csv', encoding='utf-8')
print(elenco.head(10))

#Cuantas peliculas estan listadas en dataframe

print(len(titulos))

print(titulos[titulos.title.str.contains("Exorcist")].sort_values('year'))

print(titulos[titulos.title.str.contains("Batman")].sort_values('year'))

print(titulos[titulos.title.str.contains("taxi driver")].sort_values('year'))

print(titulos[titulos.title.str.contains("1980")])

print(titulos[titulos.year.between(1980,2000)])

print(len( titulos[ (titulos.year >= 1980) & (titulos.year <= 2000)]))