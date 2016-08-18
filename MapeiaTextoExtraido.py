# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 23:53:44 2016

@author: Claudio
"""



from ExtracaoTexto import BalancoEnergia, Subsistemas       
from DicionarioTexto import DicionarioRegEx

class MapeiaTexto():
    
    def data_relatorio(self, objeto_bs):

        dados = BalancoEnergia()    
        dic = DicionarioRegEx()
        self.data_arquivo = dados.data_arquivo_entrada(objeto_bs, 'div', dic.geral['data_ipdo_tp'])
        
        print self.data_arquivo 
        return self.data_arquivo    
      
      
    # Dados da página 1 
    def resumo_balanco_energia(self, objeto_bs):

        dados = BalancoEnergia()
        dic = DicionarioRegEx()
        self.programado = dados.resumo_sin(objeto_bs, 'div', dic.balanco['programado_lf'] , dic.balanco['programado_tp'])        
        self.verificado = dados.resumo_sin(objeto_bs, 'div', dic.balanco['verificado_lf'], dic.balanco['verificado_tp'])      

        return [self.programado, self.verificado]
        
        
    # TODO mapear o  balanço de energia por subsistema    
    def balanco_por_subsistema(self, objeto_bs):
        
       dic = DicionarioRegEx()
        ## TODO separar a caga da produção SE
       self.sudeste = self.balanco_energetico_detalhado('Sudeste', objeto_bs, dic.sudeste)
       self.sul = self.balanco_energetico_detalhado('Sul', objeto_bs, dic.sul)
       self.nordeste = self.balanco_energetico_detalhado('Nordeste', objeto_bs, dic.nordeste)                
        ## TODO arrumar a extração de fontes de energia       
       self.norte = self.balanco_energetico_detalhado('Norte', objeto_bs, dic.norte)                
      
       return self.sudeste, self.sul, self.nordeste, self.norte
        
        
        
    def balanco_energetico_detalhado(self, nome_subsis, objeto_bs, dic):
        
        tag = 'div'
        dados = Subsistemas()    
        
        self.nome_subis = nome_subsis 
        #                                                  (objeto_bs, tag, left_tx, top_tx):  
        self.fontes = dados.fontes(objeto_bs, tag, dic['fontes_lf'], dic['fontes_tp'] )
        
        self.producao_vf = dados.producao(objeto_bs, tag, dic['prod_verif_lf'], dic['prod_verif_tp'] )
        self.producao_pg = dados.producao(objeto_bs, tag, dic['prod_prog_lf'], dic['prod_prog_tp'] )

        self.carga_vf = dados.carga(objeto_bs, tag, dic['carga_verif_lf'], dic['carga_verif_tp'] )
        self.carga_pg = dados.carga(objeto_bs, tag, dic['carga_prog_lf'], dic['carga_prog_tp'] )

        self.ena_vf = dados.ena(objeto_bs, tag, dic['ena_lf'], dic['ena_tp'] )
        
        self.ear_vf = dados.ear(objeto_bs, tag, dic['ear_lf'], dic['ear_tp'] )


#        
        return self.fontes, self.producao_vf, self.producao_pg, self.carga_vf, self.carga_pg, self.ena_vf, self.ear_vf
          
        
#    def fontes(self, objeto_bs, tag, left_tx, top_tx):      
#        
##        
#        sudeste = {
#    'fontes_tp' : 'top:(130[5-9]|131[0-5])px', 
#    'fontes_lf' : 'left:(38[0-9])px',
#
#    'prod_verif_tp' : 'top:(131[5-9]|132[0-5])px', 
#    'prod_verif_lf' : 'left:(47[0-9])px',
#    'prod_prog_tp' : 'top:(131[5-9]|132[0-5])px', 
#    'prod_prog_lf' : 'left:(51[5-9]|52[0-5])px',
#
##        'carga_verif_tp' : 'top:(18[0-9]|19[0-9])px', 
##        'carga_verif_lf' : 'left:(27[0-9]|28[0-9])px',
##        'carga_prog_tp' : 'top:(18[0-9]|19[0-9])px', 
##        'carga_prog_lf' : 'left:(27[0-9]|28[0-9])px',
#
#    'ena_tp' : 'top:(47[3-9]|48[0-3])px', 
#    'ena_lf' : 'left:(137[7-9]|138[0-8])px',
#
#    'ear_tp' : 'top:(143[0-9])px', 
#    'ear_lf' : 'left:(38[0-9])px'
#    }