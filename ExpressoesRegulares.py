# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 21:31:22 2016

@author: Claudio
"""

#      tp --> top
#      fl --> left
class DicionarioRegEx():
    
    # Organizar 
    
    geral = {
        'data_ipdo_tp' : 'top:(18[0-9]|19[0-9])px'
        }

   
    sistema_interlidado_nacional = {
         
         # Balaço Energético Resumido (Página 1)
        'programado_lf' : 'left:(27[0-9]|28[0-9])px',
        'programado_tp' : 'top:(30[0-9]|31[0-9])px',
        
        'verificado_lf' : 'left:(36[0-9]|37[0-9])px',
        'verificado_tp' : 'top:(30[0-9]|31[0-9])px',
        
        # Demandas máximas

        }
        
    balanco = {
        'programado_lf' : 'left:(27[0-9]|28[0-9])px',
        'programado_tp' : 'top:(30[0-9]|31[0-9])px',
        'verificado_lf' : 'left:(36[0-9]|37[0-9])px',
        'verificado_tp' : 'top:(30[0-9]|31[0-9])px'
        }
        
    
    
    sudeste = {
        'nome' : 'sudeste',
        'qtd_programada_fontes' : 3,
        
        # Balaço Energético Detalhado (Página 2)
        'fontes_tp' : 'top:(128[0-9]|129[0-9]|130[0-9]|131[0-9]|132[0-9])px', 
        'fontes_lf' : 'left:(35[0-9]|36[0-9]|37[0-9]|38[0-9]|39[0-9])px',
    
        'prod_verif_tp' : 'top:(129[0-9]|130[0-9]|131[0-9]|132[0-9]|133[0-9])px', 
        'prod_verif_lf' : 'left:(44[0-9]|45[0-9]|46[0-9]|47[0-9]|48[0-9]|49[0-9])px',
        'prod_prog_tp' : 'top:(129[0-9]|130[0-9]|131[0-9]|132[0-9]|133[0-9])px', 
        'prod_prog_lf' : 'left:(48[0-9]|49[0-9]|50[0-9]|51[0-9]|52[0-9]|53[0-9])px',
                # RegEx prod == carga
        'carga_verif_tp' : 'top:(129[0-9]|130[0-9]|131[0-9]|132[0-9]|133[0-9])px', 
        'carga_verif_lf' : 'left:(44[0-9]|45[0-9]|46[0-9]|47[0-9]|48[0-9]|49[0-9])px',
        'carga_prog_tp' : 'top:(129[0-9]|130[0-9]|131[0-9]|132[0-9]|133[0-9])px',
        'carga_prog_lf' : 'left:(48[0-9]|49[0-9]|50[0-9]|51[0-9]|52[0-9]|53[0-9])px',
    
        'ena_tp' : 'top:(135[0-9]|136[0-9]|137[0-9]|138[0-9]|139[0-9]|140[0-9])px', 
        'ena_lf' : 'left:(44[0-9]|45[0-9]|46[0-9]|47[0-9]|48[0-9]|49[0-9])px',
    
        'ear_tp' : 'top:(143[0-9]|144[0-9])px', 
        'ear_lf' : 'left:(38[0-9]|39[0-9]|40[0-9]|41[0-9]|42[0-9]|43[0-9])px',
    
        'ear1_tp' : 'top:(143[0-9]|144[0-9])px', 
        'ear1_lf' : 'left:(39[0-9]|40[0-9]|41[0-9]|42[0-9]|43[0-9])px',
        
        # Variação de Energia Armazenada (Página 3)
        'eam_tp' : 'top:(194[0-9]|195[0-9]|196[0-9])px', 
        'eam_lf' : 'left:(36[0-9]|37[0-9]|38[0-9]|39[0-9]|40[0-9])px',
        
        # Demanda Máxima Instantânea (Página 14)
        'carga_hora_verif_tp' : 'top:(1229[0-9]|1230[0-9])px',
        'carga_hora_verif_lf' : 'left:(22[0-9]|23[0-9]|24[0-9])px',

        'carga_hist_tp' : 'top:(1229[0-9]|1230[0-9])px',
        'carga_hist_lf' : 'left:(34[0-9]|35[0-9]|36[0-9])px',

        'data_hist_tp' : 'top:(1229[0-9]|1230[0-9])px',
        'data_hist_lf' : 'left:(40[0-9]|41[0-9]|42[0-9])px'

        }


    sul = {
        'nome' : 'sul',
        'qtd_programada_fontes' : 3,
    
        'fontes_tp' : 'top:(138[0-9]|139[0-9]|140[0-9]|141[0-9]|142[0-9]|143[0-9])px', 
        'fontes_lf' : 'left:(18[0-9]|19[0-9]|20[0-9])px',
    
        'prod_verif_tp' : 'top:(139[0-9]|140[0-9]|141[0-9]|142[0-9]|143[0-9]|144[0-9])px', 
        'prod_verif_lf' : 'left:(27[0-9]|28[0-9]|29[0-9]|29[0-9]|30[0-9]|31[0-9])px',
        'prod_prog_tp' : 'top:(139[0-9]|140[0-9]|141[0-9]|142[0-9]|143[0-9]|144[0-9])px', 
        'prod_prog_lf' : 'left:(31[0-9]|32[0-9]|33[0-9]|34[0-9]|35[0-9])px',
    
        'carga_verif_tp' : 'top:(143[0-9]|144[0-9]|145[0-9]|146[0-9]|147[0-9]|148[0-9])px', 
        'carga_verif_lf' : 'left:(27[0-9]|28[0-9]|29[0-9]|29[0-9]|30[0-9]|31[0-9])px',
       
        'carga_prog_tp' : 'top:(143[0-9]|144[0-9]|145[0-9]|146[0-9]|147[0-9]|148[0-9])px', 
        'carga_prog_lf' : 'left:(30[0-9]|31[0-9]|33[0-9]|34[0-9]|35[0-9])px',
    
        'ena_tp' : 'top:(147[0-9]|148[0-9]|149[0-9]|150[0-9])px', 
        'ena_lf' : 'left:(27[0-9]|28[0-9]|29[0-9]|30[0-9]|31[0-9])px',
    
        'ear_tp' : 'top:(152[0-9]|153[0-9]|154[0-9]|155[0-9])px', 
        'ear_lf' : 'left:(22[0-9]|23[0-9]|24[0-9]|25[0-9]|26[0-9])px',
    
        'ear1_tp' : 'top:(152[0-9]|153[0-9]|154[0-9]|155[0-9])px', 
        'ear1_lf' : 'left:(23[0-9]|24[0-9]|25[0-9]|26[0-9])px',
    
        'eam_tp' : 'top:(194[0-9]|195[0-9]|196[0-9])px', 
        'eam_lf' : 'left:(31[0-9]|32[0-9]|33[0-9]|34[0-9]|35[0-9])px',

        # Demanda Máxima Instantânea (Página 14)
        'carga_hora_verif_tp' : 'top:(1226[0-9]|1227[0-9])px',
        'carga_hora_verif_lf' : 'left:(22[0-9]|23[0-9]|24[0-9])px',
## TODO expressão do sul é diferente dos outros
        'carga_hist_tp' : 'top:(1226[0-9]|1227[0-9])px',
        'carga_hist_lf' : 'left:(34[0-9]|35[0-9]|36[0-9])px',

#        'data_hist_tp' : 'top(1229[0-9]|1230[0-9])px',
#        'data_hist_lf' : 'left(40[0-9]|41[0-9]|42[0-9])px'
       
        }
    
    
    nordeste = {
        'nome' : 'nordeste',
        'qtd_programada_fontes' : 3,
        
        'fontes_tp' : 'top:(110[0-9]|111[0-9])px', 
        'fontes_lf' : 'left:(35[0-9]|36[0-9]|37[0-9]|38[0-9]|39[0-9])px',
    
        'prod_verif_tp' : 'top:(111[0-9]|112[0-9]|113[0-9]|114[0-9])px', 
        'prod_verif_lf' : 'left:(44[0-9]|45[0-9]|46[0-9]|47[0-9]|48[0-9])px',
        
        'prod_prog_tp' : 'top:(111[0-9]|112[0-9]|113[0-9]|114[0-9])px',  
        'prod_prog_lf' : 'left:(50[0-9]|51[0-9]|52[0-9]|53[0-9]|54[0-9])px',
    
        'carga_verif_tp' : 'top:(114[0-9]|115[0-9]|116[0-9]|117[0-9])px', 
        'carga_verif_lf' : 'left:(44[0-9]|45[0-9]|46[0-9]|47[0-9]|48[0-9])px',
        
        'carga_prog_tp' : 'top:(114[0-9]|115[0-9]|116[0-9]|117[0-9])px', 
        'carga_prog_lf' : 'left:(49[0-9]|50[0-9]|51[0-9]|52[0-9])px',
    
        'ena_tp' : 'top:(117[0-9]|118[0-9]|119[0-9])px', 
        'ena_lf' : 'left:(44[0-9]|45[0-9]|46[0-9]|47[0-9]|48[0-9])px',
    
        'ear_tp' : 'top:(121[0-9]|122[0-9]|123[0-9]|124[0-9])px', 
        'ear_lf' : 'left:(41[0-9]|42[0-9]|43[0-9]|44[0-9])px',
        
        'eam_tp' : 'top:(194[0-9]|195[0-9]|196[0-9])px', 
        'eam_lf' : 'left:(49[0-9]|50[0-9]|51[0-9]|52[0-9]|53[0-9]|54[0-9])px',
        
        # Demanda Máxima Instantânea (Página 14)
        'carga_hora_verif_tp' : 'top:(1231[0-9]|1232[0-9])px',
        'carga_hora_verif_lf' : 'left:(22[0-9]|23[0-9]|24[0-9])px',

        'carga_hist_tp' : 'top:(1231[0-9]|1232[0-9])px',
        'carga_hist_lf' : 'left:(34[0-9]|35[0-9]|36[0-9])px',

        'data_hist_tp' : 'top:(1231[0-9]|1232[0-9])px',
        'data_hist_lf' : 'left:(40[0-9]|41[0-9]|42[0-9])px'        
        }
    
    
    norte = {
        'nome' : 'norte',
        'qtd_programada_fontes' : 2,
        
        'fontes_tp' : 'top:(107[0-9]|108[0-9]|109[0-9])px', 
        'fontes_lf' : 'left:(6[0-9]|7[0-9]|8[0-9]|9[0-9])px',
    
        'prod_verif_tp' : 'top:(110[0-9]|111[0-9]|112[0-9])px', 
        'prod_verif_lf' : 'left:(14[0-9]|15[0-9]|16[0-9]|17[0-9])px',
    
        'prod_prog_tp' : 'top:(110[0-9]|111[0-9]|112[0-9])px',  
        'prod_prog_lf' : 'left:(17[0-9]|18[0-9]|19[0-9]|20[0-9]|21[0-9]|22[0-9])px',
    
        'carga_verif_tp' : 'top:(114[0-9]|115[0-9])px', 
        'carga_verif_lf' : 'left:(16[0-9]|16[0-9]|16[0-9]|17[0-9])px',
        'carga_prog_tp' : 'top:(114[0-9]|115[0-9])px', 
        'carga_prog_lf' : 'left:(18[0-9]|19[0-9]|20[0-9]|21[0-9])px',
    
        'ena_tp' : 'top:(115[0-9]|116[0-9]|117[0-9])px', 
        'ena_lf' : 'left:(14[0-9]|15[0-9]|16[0-9])px',
    
        'ear_tp' : 'top:(120[0-9]|121[0-9]|122[0-9]|123[0-9])px', 
        'ear_lf' : 'left:(11[0-9]|12[0-9])px',
    
        'ear1_tp' : 'top:(120[0-9]|121[0-9]|122[0-9]|123[0-9])px', 
        'ear1_lf' : 'left:(45[0-9]|46[0-9]|47[0-9])px',
    
        'eam_tp' : 'top:(194[0-9]|195[0-9]|196[0-9])px', 
        'eam_lf' : 'left:(43[0-9]|44[0-9]|45[0-9]|46[0-9]|47[0-9]|48[0-9])px',

        # Demanda Máxima Instantânea (Página 14)
        'carga_hora_verif_tp' : 'top:(1230[0-9]|1231[0-9])px',
        'carga_hora_verif_lf' : 'left:(22[0-9]|23[0-9]|24[0-9])px',   

        'carga_hist_tp' : 'top:(1231[0-9]|1232[0-9])px',
        'carga_hist_lf' : 'left:(34[0-9]|35[0-9]|36[0-9])px',

        'data_hist_tp' : 'top:(1231[0-9]|1232[0-9])px',
        'data_hist_lf' : 'left:(40[0-9]|41[0-9]|42[0-9])px'      
        
        }
    
    
    itaipu ={
        'nome' : 'itaipu',
        
        'qtd_programada_fontes' : 2,
        
        'fontes_tp' : 'top(131[0-9]|132[0-9]|133[0-9])px',
        'fontes_lf' : 'left(3[0-9]|4[0-9]|5[0-9])px',
        
        'prod_verif_tp' : 'top:(131[0-9]|132[0-9]|133[0-9])px', 
        'prod_verif_lf' : 'left:(8[7-9]|9[0-9]|10[0-9])px',
    
        'prod_prog_tp' : 'top:(131[0-9]|132[0-9]|133[0-9])px',  
        'prod_prog_lf' : 'left:(13[0-9]|14[0-9]|15[0-9])px',
        }    
    
    ## TODO faltam as expressoes das demandas máximas do SIN
    # balanço detalhado
    sistema_interligado = {
                            'sudeste' : sudeste,
                            'sul' : sul, 
                            'nordeste' : nordeste,
                            'norte' : norte}   
    
    
#    balanco_energetico = {
#                    'lista_subsistemas' : ['sudeste', 'sul', 'nordeste', 'norte'],
#                    'sudeste' : sudeste,
#                    'sul' : sul, 
#                    'nordeste' : nordeste,
#                    'norte' : norte,
#                    'sistema_interlidado_nacional' : sistema_interlidado_nacional} 
    
    
    
# Intercambio de Energia entre subsistemas      
    intercambio = {
        'norte-imperatriz_tp' : 'top:(114[0-9]|115[0-9])px', 
        'norte-imperatriz_lf' : 'left:(22[0-9]|23[0-9]|24[0-9]|25[0-9]|26[0-9])px', 
        'imperatriz-nordeste_tp' : 'top:(114[0-9]|115[0-9])px',
        'imperatriz-nordeste_lf' : 'left:(29[0-9]|30[0-9]|31[0-9]|32[0-9]|33[0-9])px',
        'itaipu-sudeste_tp' : 'top:(130[0-9]|131[0-9])px', 
        'itaipu-sudeste_lf' : 'left:(20[0-9]|21[0-9]|22[0-9]|23[0-9]|24[0-9])px', 
        'sudeste-imperatriz_tp' : 'top:(125[0-9]|126[0-9])px',
        'sudeste-imperatriz_lf' : 'left:(24[0-9]|25[0-9]|26[0-9]|27[0-9]|28[0-9])px',
        'sul-sudeste_tp' : 'top:(148[0-9]|149[0-9]|150[0-9])px', 
        'sul-sudeste_lf' : 'left:(35[0-9]|36[0-9]|37[0-9]|38[0-9]|39[0-9]|40[0-9]|41[0-9]|42[0-9]|43[0-9]|44[0-9]|45[0-9]|46[0-9]|47[0-9]|48[0-9]|49[0-9]|50[0-9])px', 
        'internacional-sul_tp' : 'top:(147[0-9]|147[0-9]|148[0-9]|149[0-9]|150[0-9]|151[0-9]|152[0-9]|153[0-9])px',
        'internacional-sul_lf' : 'left:(3[0-9]|4[0-9]|5[0-9]|6[0-9]|7[0-9]|8[0-9]|9[0-9]|10[0-9]|11[0-9]|12[0-9]|13[0-9]|14[0-9]|15[0-9])px'
        }
    







class DicionarioStrings():
    
    
    subsistemas = ['sudeste', 'sul', 'nordeste', 'norte']
    sub ={
        'SE' : 'sudeste',
        'S'  : 'sul',        
        'NE' : 'nordeste',
        'N'  : 'norte',
        }
    subsistemas_acronimos = {
        'sudeste' : 'SE',
        'sul' : 'S',
        'nordeste' : ' NE',
        'norte' : 'N'
    }    
    
    fontes_energia = {
        1 : 'Hidro',
        2 : 'Termo',
        3 : 'Eólica',
        4 : 'Nuclear',
#        5 : 'Solar',
        
    }
        
    