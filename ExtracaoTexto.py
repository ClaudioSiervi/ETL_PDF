# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 17:37:43 2016

@author: Claudio
"""

class ExtraiTextoBalancoEnergia():
#    import re
#    import string
#    from bs4 import BeautifulSoup

    def data_arquivo_entrada(self, objeto_bs, tag, top_num):
        import string
        
        top_tx =  'top:' +  top_num + 'px'  #314px'
        
        tag_encontrada = objeto_bs.select(tag+'[style*="'+top_tx+'"]')
        conteudo_tag = tag_encontrada[0].contents
        
        texto_extraido_unicode = ' ' .join(conteudo_tag[0].stripped_strings)
        texto_extraido_str = texto_extraido_unicode.encode('utf-8')
        texto_extraido_str = string.split(texto_extraido_str, ',')
        texto_extraido_str = texto_extraido_str[1]    # Data do IPDO       

        return texto_extraido_str
        
    # Extrai os dados da operação diária programada e verificada das 
        #tags html do Balanço de Energia
    def sistema_interligado(self, objeto_bs, tag, left_num, top_num):        
        import re        
       
        #tag ='div'
        left_tx = 'left:' + left_num + 'px' #'284px'
        top_tx =  'top:' +  top_num + 'px'  #314px'
        
        tag_encontrada = objeto_bs.find(tag, style=re.compile(r''+ left_tx+'.*?'+top_tx))
        conteudo_tag = tag_encontrada.contents
        texto_extraido_unicode =''
        tam = len(conteudo_tag)
        for item in xrange(0, tam):
#            texto_extraido_unicode = texto_extraido_unicode + ' ' .join(conteudo_tag[item].stripped_strings)
#            texto_extraido_unicode = texto_extraido_unicode + ' '
            texto_extraido_unicode = texto_extraido_unicode + ';' .join(conteudo_tag[item].stripped_strings)
            texto_extraido_unicode = texto_extraido_unicode + ';'
        
        texto_extraido_str = texto_extraido_unicode.encode('utf-8')
        
        print texto_extraido_str
        
        return texto_extraido_str       