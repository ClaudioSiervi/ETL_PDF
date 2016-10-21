# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 22:15:01 2016

@author: Claudio
"""


from Arquivo import ArquivoIPDO
#from ImprimeResultados import ImprimeArquivosTexto

import os
#import fabric
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
mes = "04"
ano = "2016"
caminho = str(caminho) + "\PDF_IPDO\\" + mes +"-" + ano
#caminho += mes  

for dia in xrange(2,32):
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
    
    
    #https://rominirani.com/firebase-iot-tutorial-46203a92f869#.l6foxuhak
#    https://codedump.io/share/sXt99llUbBb7/1/post-data-to-firebase-using-python

    import json# prettify json

    import requests
    firebase_url = 'https://wesee-dw.firebaseio.com/balanco_detalhado/'+str(ano)+'/'+str(mes)+'/'+str(dia)
    
#    result = requests.post(firebase_url, data=json.dumps(balanco_detalhado))
    
    result = requests.post(firebase_url+'.json', data=json.dumps(balanco_detalhado))



    print(json.dumps(balanco_detalhado, indent = 5))
 
 
#send_to_slack('Jimi Hendrix Falastrão',balanco_detalhado,':chipmunk:')

#manipula_pdf.salva_texto_em_txt(texto_extraido, 'texto_extraido.txt')
#print(html_extraido.prettify())
