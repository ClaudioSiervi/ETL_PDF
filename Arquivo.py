# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 23:53:44 2016

@author: Claudio
"""


from etl_pdf import Ferramentas
from ImprimeResultados import ImprimeArquivosTexto
from ExtracaoTexto import BalancoEnergeticoResumido, BalancoEnergeticoDetalhado       
from Mapeamento import DicionarioRegEx

from bs4 import BeautifulSoup


class ArquivoIPDO():
    
    def __init__(self, nome_arquivo_entrada):
        self.__init__ = self.mapeia_texto(nome_arquivo_entrada)


    def mapeia_texto(self, nome_arquivo_entrada):
        # exemplo:  nome_arquivo_entrada = 'IPDO-22-06-2016 - unlocked.pdf'
        nome_arquivo_saida = nome_arquivo_entrada + '-unlocked.pdf'
        # exemplo:  nome_arquivo_entrada = 'IPDO-22-06-2016.pdf'
        nome_arquivo_entrada = nome_arquivo_entrada + '.pdf'
    
        converte = Ferramentas()
        converte.desbloqueia(nome_arquivo_entrada, nome_arquivo_saida)
        
        html_extraido = converte.pdf_para_html(nome_arquivo_saida)    
        
        imprime = ImprimeArquivosTexto()
        imprime.texto_em_html(html_extraido, 'texto_extraido.html')
        
        self.objeto_bs = BeautifulSoup(html_extraido, 'html.parser')

        self.data_relatorio = self.extrair_data_relatorio()#(objeto_bs)
        self.balanco_energetico_resumido = self.extrair_balanco_energetico_resumido()#()(objeto_bs)
        self.balanco_energetico_detalhado = self.extrair_balanco_energetico_detalhado()#(objeto_bs)
        
        print self.balanco_energetico_detalhado


#####-------------     

    def extrair_data_relatorio(self):

        subsistema = BalancoEnergeticoResumido()    
        dic = DicionarioRegEx()
        
        data_arquivo = subsistema.data_arquivo_entrada(self.objeto_bs, 'div', dic.geral['data_ipdo_tp'])
        
        print data_arquivo 
        return data_arquivo    
      
      
    # Dados da página 1 
    def extrair_balanco_energetico_resumido(self):

        subsistema = BalancoEnergeticoResumido()
        dic = DicionarioRegEx()
        
        programado = subsistema.resumo_sin(self.objeto_bs, 'div', dic.balanco['programado_lf'] , dic.balanco['programado_tp'])        
        verificado = subsistema.resumo_sin(self.objeto_bs, 'div', dic.balanco['verificado_lf'], dic.balanco['verificado_tp'])      

        return [programado, verificado]
        
        
    # Dados da página 2    
    def extrair_balanco_energetico_detalhado(self):

        dicionario = DicionarioRegEx()
        
        self.sudeste = self.balanco_energetico_detalhado_por_subsistema(dicionario.sudeste)
        self.sul = self.balanco_energetico_detalhado_por_subsistema(dicionario.sul)
        self.nordeste = self.balanco_energetico_detalhado_por_subsistema( dicionario.nordeste)                      
        self.norte = self.balanco_energetico_detalhado_por_subsistema(dicionario.norte)                
        
        self.sistema_interligado_nacional = {}
        self.sistema_interligado_nacional['subsistemas'] = {'sudeste' :'', 'sul':'', 'nordeste':'', 'norte':''}
        self.sistema_interligado_nacional['subsistemas']['sudeste'] = self.sudeste['sudeste']
        self.sistema_interligado_nacional['subsistemas']['sul'] =  self.sul['sul']  
        self.sistema_interligado_nacional['subsistemas']['nordeste'] =  self.nordeste['nordeste']
        self.sistema_interligado_nacional['subsistemas']['norte'] =  self.norte['norte']
        
#        print self.sistema_interligado_nacional['subsistemas'] 
#        return self.sudeste, self.sul, self.nordeste, self.norte
        return self.sistema_interligado_nacional['subsistemas']
        
        
        
        
    def balanco_energetico_detalhado_por_subsistema(self, regex):
        
        tag = 'div'        
        balanco_energetico_detalhado = BalancoEnergeticoDetalhado()    
        
        subsistema = {}
        subsistema[regex['nome']] = {}
        
        qtd_fontes = regex['qtd_programada_fontes']
#                                                                                    (objeto_bs, tag, left_tx, top_tx):  
        [fontes_lista, fontes_json]  = balanco_energetico_detalhado.recupera_fontes(self.objeto_bs, tag, regex['fontes_lf'], regex['fontes_tp'] )
        
        subsistema[regex['nome']]['qtd_fontes'] = {'programada':regex['qtd_programada_fontes'], 'verificada':len(fontes_lista)-1} # -1 -> retira Total

        if subsistema[regex['nome']]['qtd_fontes']['programada'] <> subsistema[regex['nome']]['qtd_fontes']['verificada']:
            print 'Erro: A quantidade de fontes verificadas é diferente da quantidade programada.'
            print 'programada ->'  + str(subsistema[regex['nome']]['qtd_fontes']['programada'])
            print 'verificada ->'  + str(subsistema[regex['nome']]['qtd_fontes']['verificada'])
            import sys            
            sys.exit()     
        
        
        producao_vf = balanco_energetico_detalhado.producao(self.objeto_bs, tag, regex['prod_verif_lf'], regex['prod_verif_tp'] )
        producao_pg = balanco_energetico_detalhado.producao(self.objeto_bs, tag, regex['prod_prog_lf'], regex['prod_prog_tp'] )
        
        ##  separa a caga da produção
        if ((len(producao_vf)==(qtd_fontes+2) and (len(producao_pg)==(qtd_fontes+2)))):
            carga_vf = [producao_vf.pop(qtd_fontes+1)]
            carga_pg = [producao_pg.pop(qtd_fontes+1)]
            
        ## lê a carga a partir de uma expressão regular
        elif ((len(producao_vf)==(qtd_fontes+1)) and (len(producao_pg)==(qtd_fontes+1))):  
            carga_vf = balanco_energetico_detalhado.carga(self.objeto_bs, tag, regex['carga_verif_lf'], regex['carga_verif_tp'] )
            carga_pg = balanco_energetico_detalhado.carga(self.objeto_bs, tag, regex['carga_prog_lf'], regex['carga_prog_tp'] )
            
        else:
            print 'Erro ao ler a carga do subsistema ->' +  regex['nome']
            print 'O arquivo deve ter mudado de estrutura.'    

        # produção programa e verificada por fonte
        for indice, fonte in enumerate(fontes_lista):
            fontes_json[fonte] = {  
                'programada' : producao_pg[indice], 
                'verificada' : producao_vf[indice]
                }
                
        subsistema[regex['nome']]['energia'] = fontes_json
        
        energia_natural_afluente_vf = balanco_energetico_detalhado.ena(self.objeto_bs, tag, regex['ena_lf'], regex['ena_tp'] )
        subsistema[regex['nome']]['ena'] = {'verificada' : energia_natural_afluente_vf[0]}
        
        energia_armazenada_reservatorio_vf = balanco_energetico_detalhado.ear(self.objeto_bs, tag, regex['ear_lf'], regex['ear_tp'] )
        subsistema[regex['nome']]['ear'] = {'verificada' : energia_armazenada_reservatorio_vf[0]}
        
        return subsistema          