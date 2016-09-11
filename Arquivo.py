# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 23:53:44 2016

@author: Claudio
"""



from ExtracaoTexto import BalancoEnergeticoResumido, BalancoEnergeticoDetalhado, VariacaoEnergiaArmazenada       
from ImprimeResultados import ImprimeArquivosTexto
from ExpressoesRegulares import DicionarioRegEx
from Mapeamento import MapeamentoBalancoDetalhado
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

#####-------------     

    def imprimir_resultados(self):
        
        try:
            imprimir = ImprimeArquivosTexto()
            
            imprimir.texto_em_html(self.html_extraido, 'texto_extraido.html')
            imprimir.balanco_energia_resumido_em_xlsx(self.arquivo_ipdo["geral"], self.arquivo_ipdo["balanco_resumido"])
            imprimir.balanco_energia_detalhado_em_xlsx(self.arquivo_ipdo["geral"], self.arquivo_ipdo["balanco_detalhado"])
                        
            
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


    # Dados da página 2    
    def extrair_balanco_energetico_detalhado(self):

#        balanco_energetico_detalhado_por_subsistema = BalancoEnergeticoDetalhado
        dicionario = DicionarioRegEx()         
        mapeamento = MapeamentoBalancoDetalhado()
        
        sudeste = self.balanco_energetico_detalhado_por_subsistema(dicionario.sudeste)
        sul = self.balanco_energetico_detalhado_por_subsistema(dicionario.sul)
        nordeste = self.balanco_energetico_detalhado_por_subsistema( dicionario.nordeste)                      
        norte = self.balanco_energetico_detalhado_por_subsistema(dicionario.norte)                
        
        sistema_interligado_nacional = {}
        sistema_interligado_nacional['balanco_detalhado'] = {'sudeste' :'', 'sul':'', 'nordeste':'', 'norte':''}
        sistema_interligado_nacional['balanco_detalhado']['sudeste'] = sudeste['sudeste']
        sistema_interligado_nacional['balanco_detalhado']['sul'] =  sul['sul']  
        sistema_interligado_nacional['balanco_detalhado']['nordeste'] =  nordeste['nordeste']
        sistema_interligado_nacional['balanco_detalhado']['norte'] =  norte['norte']
        
#        print dicionario.intercambio
        self.intercambio = mapeamento.intercambio_sistema_interligado_nacional(self.objeto_bs, dicionario.intercambio)   
        print "intercâmbio"        
        import json# prettify json
        print(json.dumps(self.intercambio, indent = 3))
        
#        print self.sistema_interligado_nacional['subsistemas'] 
#        return self.sudeste, self.sul, self.nordeste, self.norte
        return sistema_interligado_nacional
        
#    # Dados da página 3    
#    def extrair_energia_armazenada_maxima(self):
#
##        balanco_energetico_detalhado_por_subsistema = BalancoEnergeticoDetalhado
#        dicionario = DicionarioRegEx()
#        
#        self.sudeste = self.balanco_energetico_detalhado_por_subsistema(dicionario.sudeste)
#        self.sul = self.balanco_energetico_detalhado_por_subsistema(dicionario.sul)
#        self.nordeste = self.balanco_energetico_detalhado_por_subsistema( dicionario.nordeste)                      
#        self.norte = self.balanco_energetico_detalhado_por_subsistema(dicionario.norte)   
#        

        
    ## TODO trnasferir balanco_energetico_detalhado_por_subsistema para a classe de ExtraçãoTexto
    def balanco_energetico_detalhado_por_subsistema(self, regex):
        
        tag = 'div'        
        balanco_detalhado_extrair = BalancoEnergeticoDetalhado()    
        
        balanco_detalhado = {}
        balanco_detalhado[regex['nome']] = {}
        
        qtd_fontes = regex['qtd_programada_fontes']
#                                                                                    (objeto_bs, tag, left_tx, top_tx):  
        [fontes_lista, fontes_json]  = balanco_detalhado_extrair.fontes_energeticas(self.objeto_bs, tag, regex['fontes_lf'], regex['fontes_tp'] )
        
        
        balanco_detalhado[regex['nome']]['qtd_fontes'] = {'programada':regex['qtd_programada_fontes'], 'verificada':len(fontes_lista)-1} # -1 -> retira Total

        if balanco_detalhado[regex['nome']]['qtd_fontes']['programada'] <> balanco_detalhado[regex['nome']]['qtd_fontes']['verificada']:
            
            ## Log -> modificação na estrutura do arquivo
            self.log_arquivo_ipdo["fontes"] = "Erro: A quantidade de fontes verificadas é diferente da quantidade programada."            
#            self.log_arquivo_ipdo["fontes"]["verificada"] = subsistema[regex["nome"]]["qtd_fontes"]["verificada"]
#            self.log_arquivo_ipdo["fontes"]["programada"] = subsistema[regex["nome"]]["qtd_fontes"]["programada"]            
#            
            print regex['nome']          
            print 'Erro: A quantidade de fontes verificadas é diferente da quantidade programada.'
            print 'programada ->'  + str(balanco_detalhado[regex['nome']]['qtd_fontes']['programada'])
            print 'verificada ->'  + str(balanco_detalhado[regex['nome']]['qtd_fontes']['verificada'])
            
            import sys            
            sys.exit()     
     
        producao_vf = balanco_detalhado_extrair.producao(
                self.objeto_bs, tag, regex['prod_verif_lf'], regex['prod_verif_tp'] )
        
        producao_pg = balanco_detalhado_extrair.producao(
                self.objeto_bs, tag, regex['prod_prog_lf'], regex['prod_prog_tp'] )
        
        ##  separa a caga da produção
        if ((len(producao_vf)==(qtd_fontes+2) and (len(producao_pg)==(qtd_fontes+2)))):
            carga_vf = [producao_vf.pop(qtd_fontes+1)]
            carga_pg = [producao_pg.pop(qtd_fontes+1)]
            
        ## lê a carga a partir de uma expressão regular
        elif ((len(producao_vf)==(qtd_fontes+1)) and (len(producao_pg)==(qtd_fontes+1))):  
            
            carga_vf = balanco_detalhado_extrair.carga(
                    self.objeto_bs, tag, regex['carga_verif_lf'], regex['carga_verif_tp'] )

            carga_pg = balanco_detalhado_extrair.carga(
                self.objeto_bs, tag, regex['carga_prog_lf'], regex['carga_prog_tp'] )
            
        else:
            print 'Erro ao ler a carga do subsistema ->' +  regex['nome']
            print 'O arquivo deve ter mudado de estrutura.'    
        

        for indice, fonte in enumerate(fontes_lista):
            fontes_json[fonte] = {  
                'programada' : producao_pg[indice], 
                'verificada' : producao_vf[indice]
                }
                
        balanco_detalhado[regex['nome']]['energia'] = fontes_json
        
        balanco_detalhado[regex['nome']]["carga"] = {
            "programada" : carga_pg[0],
            "verificada" : carga_vf[0]
            }
        
        energia_natural_afluente_vf = \
                    balanco_detalhado_extrair.energia_narutal_afluente(
                            self.objeto_bs, tag, regex['ena_lf'], regex['ena_tp'] 
                    )
                    
        balanco_detalhado[regex['nome']]['ena'] = {
                    'verificada' : energia_natural_afluente_vf[0]
                    }
        
        energia_armazenada_reservatorio_vf = \
                    balanco_detalhado_extrair.energia_armazenada_reservatorio(
                            self.objeto_bs, tag, regex['ear_lf'], regex['ear_tp']
                        )
                        
#        print energia_armazenada_reservatorio_vf
        balanco_detalhado[regex['nome']]['ear'] = {
                            'verificada' : energia_armazenada_reservatorio_vf
                            }  
  
        self.valida_conteudo_numerico(balanco_detalhado)
        
        return balanco_detalhado  
        
    
                      

    ## TODO criar uma classe de validação
    ## TODO escrever resultados das validações no arquivo de log
    
    # valida se o conteúdo dos campos é numerico
    def valida_conteudo_numerico(self, balanco_detalhado):
        
        ferramenta = Ferramentas()
        for subsistema in balanco_detalhado:
            
            for fonte in balanco_detalhado[subsistema]["energia"]:
#                print "   energia " + fonte
                for tipo in balanco_detalhado[subsistema]["energia"][fonte]:
#                    print "        " + tipo + " " + str(balanco_detalhado[subsistema]["energia"][fonte]["verificada"])
                    ferramenta.eh_numerico(fonte, balanco_detalhado[subsistema]["energia"][fonte]["verificada"])
                    ferramenta.eh_numerico(fonte, balanco_detalhado[subsistema]["energia"][fonte]["programada"])
        
        ferramenta.eh_numerico("carga", balanco_detalhado[subsistema]["carga"]["verificada"])
        ferramenta.eh_numerico("carga", balanco_detalhado[subsistema]["carga"]["programada"])
        ferramenta.eh_numerico("ena", balanco_detalhado[subsistema]["ena"]["verificada"])
        ferramenta.eh_numerico("ear", balanco_detalhado[subsistema]["ear"]["verificada"])            
        
        
    def energia_armazenada_maxima(self, regex):
        
        tag = 'div'        
        energia_armazenada_extrair = VariacaoEnergiaArmazenada()    
        
        energia_armazenada = {}
        energia_armazenada[regex['nome']] = {}
##                                                                                    (objeto_bs, tag, left_tx, top_tx):  
        energia_armazenada_maxima  = energia_armazenada_extrair.capacidade_maxima(
                                        self.objeto_bs, tag, regex['eam_lf'], regex['eam_tp'] )

        print energia_armazenada_maxima
#        
#        
#        balanco_detalhado[regex['nome']]['qtd_fontes'] = {'programada':regex['qtd_programada_fontes'], 'verificada':len(fontes_lista)-1} # -1 -> retira Total
        