# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 16:13:12 2016

@author: Claudio
"""


from ExtracaoTexto import BalancoEnergeticoDetalhado
#from ExtracaoTexto import BalancoEnergeticoResumido, BalancoEnergeticoDetalhado

class MapeamentoBalancoDetalhado():
    
    
#    def energia_armazenada_reservatorio(self, objeto_bs, regex):
#        
#        tag = 'div'
#        
#        balanco_detalhado_extrair = BalancoEnergeticoDetalhado()
#
#        energia_armazenada_reservatorio_vf = \
#            balanco_detalhado_extrair.energia_armazenada_reservatorio(self.objeto_bs)
#                        
##        print energia_armazenada_reservatorio_vf
#        energia_armazenada = {
#                            'verificada' : float(energia_armazenada_reservatorio_vf.replace('.',''))
#                            } 
#        
#        print "energia armazenada"                                
#        print energia_armazenada
#        return energia_armazenada
#        
    
    def energia_itaipu(self, objeto_bs, regex):
        # regex -> REGular EXpression
    
        tag = 'div'        
        
        balanco_detalhado_extrair = BalancoEnergeticoDetalhado()  
        
        itaipu = ['50Hz', '60Hz', 'Total']
 
        energia_extraida_vf = \
                balanco_detalhado_extrair.energia_itaipu(
                        objeto_bs, tag, regex['prod_verif_lf'],
                                        regex['prod_verif_tp']
                                                )                                                
        print energia_extraida_vf                
        
        energia_extraida_pg = \
                balanco_detalhado_extrair.energia_itaipu(
                        objeto_bs, tag, regex['prod_prog_lf'],
                                        regex['prod_prog_tp']
                                                          )
        print energia_extraida_pg  
        
        energia_itaipu = {}
        for indice, item in enumerate(itaipu):                                                  
            energia_itaipu[item] = {
                            "verificada" : float(energia_extraida_vf[indice].replace('.','')),
                            "programada" : float(energia_extraida_pg[indice].replace('.',''))
                                       }              
        print energia_itaipu
        return energia_itaipu     
        
    
    
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
#            print "intercambio"                                       
#            print intercambio_energia  
            intercambio_extraido = \
                    balanco_detalhado_extrair.intercambio_entre_subsistemas(
                            objeto_bs, tag, regex[intercambio_energia + '_lf'],
                                            regex[intercambio_energia + '_tp']
                                                                         )

            intercambio[intercambio_energia] = {
                                "verificada" : float(intercambio_extraido[0].replace('.','')),
                                "programada" : float(intercambio_extraido[1].replace('.',''))
                                           }              
        return intercambio
        
        
        
        
###########################################    
    
    
from ExtracaoTexto import VariacaoEnergiaArmazenada

class MapeamentoVariacaoEnergiaArmazenada():
    
    
    def energia_armazenada_maxima(self, objeto_bs, regex):
        
        tag = 'div'
        
        energia_armazenada_extrair = VariacaoEnergiaArmazenada()    
        
        energia_armazenada = {}

        energia_armazenada_maxima  = \
                    energia_armazenada_extrair.capacidade_maxima(
                                    objeto_bs, tag, regex['eam_lf'], \
                                                    regex['eam_tp'] 
                                                                 )

        energia_armazenada = { 
                            "verificada" : float(energia_armazenada_maxima[0].replace('.',''))
                                                        } 
        print "energia armazenada"                                
        print energia_armazenada
        return energia_armazenada
        