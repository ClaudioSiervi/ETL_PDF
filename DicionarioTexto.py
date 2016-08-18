# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 21:31:22 2016

@author: Claudio
"""

#      tp --> top
#      fl --> left
class DicionarioRegEx:
    
    # Organizar 
    
    geral = {
    'data_ipdo_tp' : 'top:(18[0-9]|19[0-9])px'
    }

    # Página 1
    balanco = {
    'programado_lf' : 'left:(27[0-9]|28[0-9])px',
    'programado_tp' : 'top:(30[0-9]|31[0-9])px',
    'verificado_lf' : 'left:(36[0-9]|37[0-9])px',
    'verificado_tp' : 'top:(30[0-9]|31[0-9])px'
    }
    
    
    sudeste = {
    'fontes_tp' : 'top:(130[5-9]|131[0-5])px', 
    'fontes_lf' : 'left:(38[0-9])px',

    'prod_verif_tp' : 'top:(131[5-9]|132[0-5])px', 
    'prod_verif_lf' : 'left:(47[0-9])px',
    'prod_prog_tp' : 'top:(131[5-9]|132[0-5])px', 
    'prod_prog_lf' : 'left:(51[5-9]|52[0-5])px',

    'carga_verif_tp' : 'top:(131[5-9]|132[0-5])px', 
    'carga_verif_lf' : 'left:(47[0-9])px',
    'carga_prog_tp' : 'top:(131[5-9]|132[0-5])px', 
    'carga_prog_lf' : 'left:(51[5-9]|52[0-5])px',

    'ena_tp' : 'top:(137[7-9]|138[0-8])px', 
    'ena_lf' : 'left:(47[3-9]|48[0-3])px',

    'ear_tp' : 'top:(143[0-9])px', 
    'ear_lf' : 'left:(38[0-9])px'
    }

    sul = {
    'fontes_tp' : 'top:(140[5-9]|141[0-5])px', 
    'fontes_lf' : 'left:(19[4-9]|20[0-4])px',

    'prod_verif_tp' : 'top:(141[5-9]|142[0-5])px', 
    'prod_verif_lf' : 'left:(29[5-9]|30[0-5])px',
    'prod_prog_tp' : 'top:(141[5-9]|142[0-5])px', 
    'prod_prog_lf' : 'left:(33[5-9]|34[0-5])px',

    'carga_verif_tp' : 'top:(146[5-9]|147[0-5])px', 
    'carga_verif_lf' : 'left:(29[5-9]|30[0-5])px',
    'carga_prog_tp' : 'top:(146[5-9]|147[0-5])px', 
    'carga_prog_lf' : 'left:(33[0-9])px',

    'ena_tp' : 'top:(147[0-5]|148[0-5])px', 
    'ena_lf' : 'left:(28[4-9]|29[0-4])px',

    'ear_tp' : 'top:(152[5-9]|153[0-5])px', 
    'ear_lf' : 'left:(23[4-9]|24[0-4])px'
    }

    nordeste = {
    'fontes_tp' : 'top:(110[5-9]|111[0-5])px', 
    'fontes_lf' : 'left:(37[6-9]|38[0-6])px',

    'prod_verif_tp' : 'top:(111[5-9]|112[0-5])px', 
    'prod_verif_lf' : 'left:(47[5-9]|48[0-5])px',
    'prod_prog_tp' : 'top:(111[5-9]|112[0-5])px',  
    'prod_prog_lf' : 'left:(51[5-9]|52[0-5])px',

    'carga_verif_tp' : 'top:(116[0-9])px', 
    'carga_verif_lf' : 'left:(47[5-9]|48[0-5])px',
    'carga_prog_tp' : 'top:(116[0-9])px', 
    'carga_prog_lf' : 'left:(51[5-9]|52[0-5])px',

    'ena_tp' : 'top:(117[5-9]|118[0-5])px', 
    'ena_lf' : 'left:(47[0-9])px',

    'ear_tp' : 'top:(122[6-9]|123[0-6])px', 
    'ear_lf' : 'left:(41[5-9]|42[0-5])px'
    }
    
    
    norte = {
    'fontes_tp' : 'top:(108[6-9]|109[0-6])px', 
    'fontes_lf' : 'left:(7[3-9]|8[0-3])px',

    'prod_verif_tp' : 'top:(111[5-9]|112[0-5])px', 
    'prod_verif_lf' : 'left:(17[0-9])px',
    'prod_prog_tp' : 'top:(111[5-9]|112[0-5])px',  
    'prod_prog_lf' : 'left:(21[0-9])px',

    'carga_verif_tp' : 'top:(115[0-9])px', 
    'carga_verif_lf' : 'left:(17[0-9])px',
    'carga_prog_tp' : 'top:(115[0-9])px', 
    'carga_prog_lf' : 'left:(21[0-9])px',

    'ena_tp' : 'top:(116[6-9]|117[0-6])px', 
    'ena_lf' : 'left:(16[0-9])px',

    'ear_tp' : 'top:(122[6-9]|123[0-6])px', 
    'ear_lf' : 'left:(11[3-9]|12[0-3])px'
    }
    
#        
#        self.Intercambio = {
#        'norte-imperatriz_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'norte-imperatriz_lf' : 'top:(18[0-9]|19[0-9])px', 
#        'imperatriz-nordeste_tp' : 'left:(27[0-9]|28[0-9])px',
#        'imperatriz-nordeste_lf' : 'left:(27[0-9]|28[0-9])px',
#        'itaipu-sudeste_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'itaipu-sudeste_lf' : 'top:(18[0-9]|19[0-9])px', 
#        'sudeste-imperatriz_tp' : 'left:(27[0-9]|28[0-9])px',
#        'sudeste-imperatriz_lf' : 'left:(27[0-9]|28[0-9])px',
#        'sul-sudeste_tp' : 'top:(18[0-9]|19[0-9])px', 
#        'sul-sudeste_lf' : 'top:(18[0-9]|19[0-9])px', 
#        'internacional-sul_tp' : 'left:(27[0-9]|28[0-9])px',
#        'internacional-sul_lf' : 'left:(27[0-9]|28[0-9])px',
#        }