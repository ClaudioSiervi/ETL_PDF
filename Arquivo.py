# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 23:53:44 2016

@author: Claudio
"""


from etl_pdf import Ferramentas
from ImprimeResultados import ImprimeArquivosTexto
from ExtracaoTexto import BalancoEnergia, DadosBalancoEnergeticoDetalhado       
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

        #self.balanco_detalhado = self.extra_balanco()


#####-------------     
    def extrair_data_relatorio(self):

        subsistema = BalancoEnergia()    
        dic = DicionarioRegEx()
        
        data_arquivo = subsistema.data_arquivo_entrada(self.objeto_bs, 'div', dic.geral['data_ipdo_tp'])
        
        print data_arquivo 
        return data_arquivo    
      
      
    # Dados da página 1 
    def extrair_balanco_energetico_resumido(self):

        subsistema = BalancoEnergia()
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
      
        return self.sudeste, self.sul, self.nordeste, self.norte
        
        
    def balanco_energetico_detalhado_por_subsistema(self, dic):
        
        tag = 'div'        
        
        balanco_energetico_detalhado = DadosBalancoEnergeticoDetalhado()    
        
#        subsistema ={}    
        nome_subistema = dic['nome']
        num_fontes = dic['num_fontes']
        qtd_fontes = dic['num_fontes']
#                                                          (objeto_bs, tag, left_tx, top_tx):  
        fontes = balanco_energetico_detalhado.fontes(self.objeto_bs, tag, dic['fontes_lf'], dic['fontes_tp'] )
        teste = {}
        teste = {'teste':fontes[0]}
        print teste
        if (teste['teste'] == 'Produção (MWmed/dia)'):
            print 'aeee'        
        
## TODO mapear a energia gerada por cada fonte        
        producao_vf = balanco_energetico_detalhado.producao(self.objeto_bs, tag, dic['prod_verif_lf'], dic['prod_verif_tp'] )
        producao_pg = balanco_energetico_detalhado.producao(self.objeto_bs, tag, dic['prod_prog_lf'], dic['prod_prog_tp'] )
        
        ##  separa a caga da produção
        if ((len(producao_vf)==(num_fontes+2) and (len(producao_pg)==(num_fontes+2)))):
            carga_vf = [producao_vf.pop(num_fontes+1)]
            carga_pg = [producao_pg.pop(num_fontes+1)]
#            print 'carga_vf -->'+ str(self.carga_vf)
#            print 'carga_pg -->'+ str(self.carga_pg)
            
        ## lê a carga a partir de uma expressão regular
        elif ((len(producao_vf)==(num_fontes+1)) and (len(producao_pg)==(num_fontes+1))):  
            carga_vf = balanco_energetico_detalhado.carga(self.objeto_bs, tag, dic['carga_verif_lf'], dic['carga_verif_tp'] )
            carga_pg = balanco_energetico_detalhado.carga(self.objeto_bs, tag, dic['carga_prog_lf'], dic['carga_prog_tp'] )
            
#            total
#            print 'carga_vf -->'+ str(self.carga_vf)
#            print 'carga_pg -->'+ str(self.carga_pg)
            
        else:
            print 'Erro ao ler a carga do subsistema ->' + nome_subistema
            print 'O arquivo deve ter mudado de estrutura.'    

        energia_natural_afluente_vf = balanco_energetico_detalhado.ena(self.objeto_bs, tag, dic['ena_lf'], dic['ena_tp'] )
        energia_armazenada_reservatorio_vf = balanco_energetico_detalhado.ear(self.objeto_bs, tag, dic['ear_lf'], dic['ear_tp'] )

        return nome_subistema, qtd_fontes, fontes, producao_pg, producao_vf, \
                carga_vf, carga_pg, energia_natural_afluente_vf, \
                energia_armazenada_reservatorio_vf
          