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
        
                                        # saida-chegada
        sentido_transferencia_energia = ['norte-imperatriz', 'imperatriz-nordeste', \
                                        'itaipu-sudeste','sudeste-imperatriz', 'sul-sudeste', \
                                        'internacional-sul']
        intercambio = {}   
        
        for intercambio_energia in sentido_transferencia_energia:            
            
            intercambio_extraido = \
                    balanco_detalhado_extrair.intercambio_entre_subsistemas(
                            objeto_bs, tag, regex[intercambio_energia + '_lf'],
                                            regex[intercambio_energia + '_tp']
                                                                         )

            intercambio[intercambio_energia] = {
                                "programada" : float(intercambio_extraido[0].replace('.','')),
                                "verificada" : float(intercambio_extraido[1].replace('.',''))
                                            }            
        return intercambio
        
        
###########################################    
    
    
from ExtracaoTexto import VariacaoEnergiaArmazenada

class MapeamentoVariacaoEnergiaArmazenada():
    
    
    def energia_armazenada_maxima(self, objeto_bs, regex):
        
        tag = 'div'
        
        energia_armazenada_extrair = VariacaoEnergiaArmazenada()    
        
        energia_armazenada = {}
        
#        for subsistema in sistema_interligado:
            
        energia_armazenada_maxima  = \
                    energia_armazenada_extrair.capacidade_maxima(
                                    objeto_bs, tag, regex['eam_lf'], \
                                                    regex['eam_tp'] 
                                                                 )

        energia_armazenada = { 
                            "verificada" : float(energia_armazenada_maxima[0].replace('.',''))
                                                        } 
                                        
        print energia_armazenada
        return energia_armazenada
        