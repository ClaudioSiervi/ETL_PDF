# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 22:15:01 2016

@author: Claudio
"""


from Arquivo import ArquivoIPDO
#from ImprimeResultados import ImprimeArquivosTexto

import os
import fabric
## TODO enviar logs no slack

#def send_to_slack(user,message,emoji):
#    
#   data = json.dumps({
#       "channel": "random",
#       "username": user,
#       "text": message,
#       "icon_emoji": ':' + emoji + ':'
#   })
#
#   data = data.replace('"', '\\"')
#   url = 'https://hooks.slack.com/services/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'
#   local('curl -H "Content-Type: application/json" -X POST -d "{}" {}'.format(data, url))
#   print 'curl -H "Content-Type: application/json" -X POST -d "{}" {}'.format(data, url)
   
#curl -H "Content-Type: application/json" -X POST -d "{\"username\": \"Pedro\", \"text\": \"Messagem\", \"icon_emoji\": \":video_game:\", \"channel\": \"spy\"}"https://hooks.slack.com/services/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
   
   
   
caminho = os.getcwd()
mes = "08"
ano = "2016"
caminho = str(caminho) + "\PDFs IPDO\\" + mes +"-" + ano
#caminho += mes  

for dia in xrange(4,5):
    if (dia <10):
        nome_arquivo_entrada = caminho + '\IPDO-0'+str(dia)+ "-" + mes +"-" + ano
    else:
        nome_arquivo_entrada = caminho + '\IPDO-'+str(dia)+ "-" + mes +"-" + ano
    print "dia" + str(dia)
    
             ##TODO --> Organizar impressões sequencialmente em um arquivo único
    arquivo_ipdo = ArquivoIPDO(nome_arquivo_entrada)
#    arquivo_ipdo.imprimir_resultados()   
    
        
#    #    print arquivo_ipdo.dados_extraidos
    balanco_detalhado = arquivo_ipdo.dados_extraidos['balanco_detalhado']
#    balanco_detalhado = arquivo_ipdo.balanco_detalhado.imprimir() classe balanco_detalhado
    
    from firebase import Firebase
    f = Firebase("https://wesee-dw.firebaseio.com/balanco_detalhado/"+ mes +"-" + ano)
    r = f.post(balanco_detalhado)

import json# prettify json
print(json.dumps(balanco_detalhado, indent = 5))
 
 
#send_to_slack('Jimi Hendrix Falastrão',balanco_detalhado,':chipmunk:')

#manipula_pdf.salva_texto_em_txt(texto_extraido, 'texto_extraido.txt')
#print(html_extraido.prettify())
