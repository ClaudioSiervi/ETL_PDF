# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 19:20:17 2016

@author: Claudio
"""
from openpyxl import load_workbook
#from Arquivo import ArquivoIPDO
from Utilitarios import Ferramentas
#from openpyxl import Workbook
import string

class ImprimeArquivosTexto():
    
    
    
    def texto_em_txt(self, texto, nome_arquivo_saida):
    # Salva o texto extraído do pdf em um arquivo texto
        arquivo_texto = open(nome_arquivo_saida, "w")
        self.status_escrita = arquivo_texto.write(texto)
        arquivo_texto.close()
        
        
    def texto_em_html(self, texto, nome_arquivo_saida):
    # Salva o texto extraído do pdf em um arquivo texto
        arquivo_texto = open(nome_arquivo_saida, "w")
        self.status_escrita = arquivo_texto.write(texto)
        arquivo_texto.close()
        

    # Imprime o resumo do balanço energético    
    def balanco_energia_resumido_em_xlsx(self, geral, balanco_resumido):
        
#        try:
        wb_ipdo = load_workbook('IPDO.xlsx') 
        ws_balanco_resumido = wb_ipdo['BalancoResumido']
        
        ferramenta = Ferramentas()
        
        [primeira_linha, ultima_linha] = ferramenta.linha_nao_vazia(ws_balanco_resumido)
        
        ultima_linha = ultima_linha + 1        
        
        indice = 'A'+str(ultima_linha) 
           
        ws_balanco_resumido[indice] = geral["data_arquivo"]
        
        num_elementos_pg = len(balanco_resumido["programada"]) # Número de elementos do resumo
        conta_valores = 0
        
        for conta_coluna_pg in xrange(1, num_elementos_pg):
            letra = ferramenta.retorna_letra_da_coluna(conta_coluna_pg + 1)
            indice = letra + str(ultima_linha)            
            ws_balanco_resumido[indice] = balanco_resumido["programada"][conta_valores]       
            conta_valores = conta_valores + 1
        
        num_elementos_vf = len(balanco_resumido["verificada"]) + conta_coluna_pg
        conta_valores = 0       
        
        for conta_coluna_vf in xrange(conta_coluna_pg, num_elementos_vf):
            letra = ferramenta.retorna_letra_da_coluna(conta_coluna_vf + 2)
            indice = letra + str(ultima_linha)            
            ws_balanco_resumido[indice] = balanco_resumido["verificada"][conta_valores]
            conta_valores = conta_valores + 1                
        
        wb_ipdo.save('IPDO.xlsx')   # sobrescreve resultados
 
#        except:
#            print '------------------------------------------------------------'
#            print 'ERRO: Não foi possível salvar os resultados na planilha.xlsx'               
        
        
        
    def balanco_energia_detalhado_em_xlsx(self, geral, balanco_detalhado):
        
        wb_ipdo = load_workbook('IPDO.xlsx') 
        ws_balanco_detalhado = wb_ipdo['BalancoDetalhado']

        ferramenta = Ferramentas()
        
        [primeira_linha, ultima_linha] = ferramenta.linha_nao_vazia(ws_balanco_detalhado)
        
        ultima_linha = ultima_linha + 1        
            
        
        indice = 'A'+str(ultima_linha)
        
        ws_balanco_detalhado[indice] = geral["data_arquivo"]
        
        fontes_relatorio = ["Hidro","Termo","Nuclear","Eólica","Solar","Total","Carga"]
        subsistemas_relatorio = ["sudeste","sul","nordeste","norte"]
        
        coluna_pg = 1 # primeira fonte programada
        coluna_vf = 8 # primeira fonte verificada
        
        for subsistema in subsistemas_relatorio:    
            print subsistema

            for fonte in fontes_relatorio:
                coluna_pg += 1
                coluna_vf += 1
                print coluna_pg
                print coluna_vf
                indice_pg = ferramenta.retorna_letra_da_coluna(coluna_pg) + str(ultima_linha)
                indice_vf = ferramenta.retorna_letra_da_coluna(coluna_vf) + str(ultima_linha)
                print indice_pg
                print indice_vf
                
                for fonte_extraida in balanco_detalhado[subsistema]["energia"]:
                    print fonte_extraida
                    if (fonte == fonte_extraida):
                        print fonte
                        
                    
                        ws_balanco_detalhado[indice_pg] = balanco_detalhado[subsistema]["energia"][fonte]["programada"]
                        print balanco_detalhado[subsistema]["energia"][fonte]["programada"]                        
                        print ws_balanco_detalhado[indice_pg]                        
                        
                        ws_balanco_detalhado[indice_vf] = balanco_detalhado[subsistema]["energia"][fonte]["verificada"]
                        print balanco_detalhado[subsistema]["energia"][fonte]["verificada"]                        
                        print ws_balanco_detalhado[indice_vf]  
                        continue
            coluna_pg += 7  # pula  fonte verificada
            coluna_vf += 7  # pula fonte programada
#                elif (fonte == "Carga"):
#                    balanco_detalhado[subsistema]["carga"]["prevista"]
#                    ws_balanco_detalhado[indice_vf]
#                    else:
#                        ws_balanco_detalhado[indice_pg] = 0
#                        ws_balanco_detalhado[indice_vf] = 0
                    
#            ws_balanco_detalhado[indice_vf] = 
        
        wb_ipdo.save('IPDO.xlsx')   # sobrescreve resultados