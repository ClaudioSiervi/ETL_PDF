# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 16:13:12 2016

@author: Claudio
"""


from ExtracaoTexto import BalancoEnergeticoDetalhado

class MapeamentoBalancoDetalhado():
    
        
    
    
    def intercambio_sistema_interligado_nacional(self, objeto_bs, regex):
        # regex -> REGular EXpression
    
        tag = 'div'        
        
        balanco_detalhado_extrair = BalancoEnergeticoDetalhado() 
    
        intercambio = {}        
                                        # saida-chegada
        sentido_transferencia_energia = ['norte-imperatriz', 'imperatriz-nordeste', \
                                        'itaipu-sudeste','sudeste-imperatriz', 'sul-sudeste', \
                                        'internacional-sul']

        for intercambio_energia in sentido_transferencia_energia:            
            
            intercambio_extraido = \
                    balanco_detalhado_extrair.intercambio_entre_subsistemas(
                            objeto_bs, tag, regex[intercambio_energia + '_lf'],
                                            regex[intercambio_energia + '_tp']
                                                                         )

            intercambio[intercambio_energia] = {
                                "verificada" : float(intercambio_extraido[0]),
                                "programada" : float(intercambio_extraido[1])
                                            }            
        return intercambio