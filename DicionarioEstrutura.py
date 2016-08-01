# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 21:09:13 2016

@author: Claudio
"""


# Mapeamento dos dados extraídos do arquivo PDF
# http://learnpythonthehardway.org/book/ex39.html
class dicionario():
    
    def __init__(self):
        self.subsistemas = {
                        "Sudeste": "SE",
                        "Sul": "S",
                        "Nordeste": "NE",
                        "Norte": "N",
                        "Itaipu": "IT",
                        "Intercambio_Inter": "II"
                        }
                        
        self.intercambio_inter = {
                        "II":[
                        "Paraguai Acaray"
                        "Uruguai Rivera"
                        "Melo"
                        "Argentina"
                        "Garabi I"
                        "Garabi II"
                        "Uruguaiana"
                        "Uruguaiana"],
                        }