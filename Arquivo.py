# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 23:53:44 2016

@author: Claudio
"""



from ExtracaoTexto import BalancoEnergeticoResumido, BalancoEnergeticoDetalhado       
from ImprimeResultados import ImprimeArquivosTexto
from Mapeamento import DicionarioRegEx
from Utilitarios import Ferramentas
from bs4 import BeautifulSoup



class ArquivoIPDO():
    
    
    
    # construtor
    def __init__(self, nome_arquivo_entrada):
        self.__init__ = self.mapeia_texto(nome_arquivo_entrada)
        self.dados_extraidos = self.arquivo_ipdo
        self.log_dados_extraidos = self.log_arquivo_ipdo


    def mapeia_texto(self, nome_arquivo_entrada):
       
        # exemplo:  nome_arquivo_entrada = 'IPDO-22-06-2016 - unlocked.pdf'
        nome_arquivo_saida = nome_arquivo_entrada + '-unlocked.pdf'
        
        # exemplo:  nome_arquivo_entrada = 'IPDO-22-06-2016.pdf'
        nome_arquivo_entrada = nome_arquivo_entrada + '.pdf'
    
        ferramenta = Ferramentas()
         
        self.log_arquivo_ipdo = {}          # log de ocorrências
        
        ferramenta.desbloqueia(nome_arquivo_entrada, nome_arquivo_saida)
        
        self.html_extraido = ferramenta.pdf_para_html(nome_arquivo_saida)    
        
        self.objeto_bs = BeautifulSoup(self.html_extraido, 'html.parser')

        self.balanco_energetico_resumido = self.extrair_balanco_energetico_resumido()
        self.balanco_energetico_detalhado = self.extrair_balanco_energetico_detalhado()
        
        self.arquivo_ipdo = {}
        self.arquivo_ipdo["geral"] = self.balanco_energetico_resumido["geral"] 
        self.arquivo_ipdo["balanco_resumido"] = self.balanco_energetico_resumido["balanco_resumido"] 
        self.arquivo_ipdo["balanco_detalhado"] = self.balanco_energetico_detalhado["balanco_detalhado"]

        print self.arquivo_ipdo


#####-------------     

    def imprimir_resultados(self):
        
        try:
            imprimir = ImprimeArquivosTexto()
            
            imprimir.texto_em_html(self.html_extraido, 'texto_extraido.html')
            imprimir.balanco_energia_resumido_em_xlsx(self.arquivo_ipdo["geral"], self.arquivo_ipdo["balanco_resumido"])

        except IOError as e:
            self.log_arquivo_ipdo["imprimir_resultados"] = "I/O error({0}): {1}".format(e.errno, e.strerror)                        
            print self.log_arquivo_ipdo["imprimir_resultados"]
      
      
    # Dados da página 1 
    def extrair_balanco_energetico_resumido(self):

        balanco_resumido = BalancoEnergeticoResumido()    
        dicionario = DicionarioRegEx()
        
        data_arquivo_ipdo = balanco_resumido.extrair_data_arquivo_ipdo(self.objeto_bs, 'div', dicionario.geral['data_ipdo_tp'])
        
        programada = balanco_resumido.extrair_dados_sistema(self.objeto_bs, 'div', dicionario.balanco['programado_lf'] , dicionario.balanco['programado_tp'])        
        verificada = balanco_resumido.extrair_dados_sistema(self.objeto_bs, 'div', dicionario.balanco['verificado_lf'], dicionario.balanco['verificado_tp'])      
        
        arquivo_ipdo = {}
        arquivo_ipdo = {"geral":{"data_arquivo":data_arquivo_ipdo}}
        arquivo_ipdo["balanco_resumido"] = {"programada":programada, "verificada": verificada}

        return arquivo_ipdo   
#        return arquivo_ipdo["balanco_resumido"]["programado"], arquivo_ipdo["balanco_resumido"]["verificado"]
        
        
        
    # Dados da página 2    
    def extrair_balanco_energetico_detalhado(self):

        dicionario = DicionarioRegEx()
        
        self.sudeste = self.balanco_energetico_detalhado_por_subsistema(dicionario.sudeste)
        self.sul = self.balanco_energetico_detalhado_por_subsistema(dicionario.sul)
        self.nordeste = self.balanco_energetico_detalhado_por_subsistema( dicionario.nordeste)                      
        self.norte = self.balanco_energetico_detalhado_por_subsistema(dicionario.norte)                
        
        self.sistema_interligado_nacional = {}
        self.sistema_interligado_nacional['balanco_detalhado'] = {'sudeste' :'', 'sul':'', 'nordeste':'', 'norte':''}
        self.sistema_interligado_nacional['balanco_detalhado']['sudeste'] = self.sudeste['sudeste']
        self.sistema_interligado_nacional['balanco_detalhado']['sul'] =  self.sul['sul']  
        self.sistema_interligado_nacional['balanco_detalhado']['nordeste'] =  self.nordeste['nordeste']
        self.sistema_interligado_nacional['balanco_detalhado']['norte'] =  self.norte['norte']
        
#        print self.sistema_interligado_nacional['subsistemas'] 
#        return self.sudeste, self.sul, self.nordeste, self.norte
        return self.sistema_interligado_nacional
        
        
        
        
    def balanco_energetico_detalhado_por_subsistema(self, regex):
        
        tag = 'div'        
        balanco_energetico_detalhado = BalancoEnergeticoDetalhado()    
        
        subsistema = {}
        subsistema[regex['nome']] = {}
        
        qtd_fontes = regex['qtd_programada_fontes']
#                                                                                    (objeto_bs, tag, left_tx, top_tx):  
        [fontes_lista, fontes_json]  = balanco_energetico_detalhado.fontes_energeticas(self.objeto_bs, tag, regex['fontes_lf'], regex['fontes_tp'] )
        
        subsistema[regex['nome']]['qtd_fontes'] = {'programada':regex['qtd_programada_fontes'], 'verificada':len(fontes_lista)-1} # -1 -> retira Total

        if subsistema[regex['nome']]['qtd_fontes']['programada'] <> subsistema[regex['nome']]['qtd_fontes']['verificada']:
            
            self.log_arquivo_ipdo["fontes"] = "Erro: A quantidade de fontes verificadas é diferente da quantidade programada."            
            self.log_arquivo_ipdo["fontes"]["verificada"] = subsistema[regex["nome"]]["qtd_fontes"]["verificada"]
            self.log_arquivo_ipdo["fontes"]["programada"] = subsistema[regex["nome"]]["qtd_fontes"]["programada"]            
            
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