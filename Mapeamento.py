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
    'data_ipdo_tp' : 'top:(18[0-9]|19[0-9])px',
    'num_fontes_sudeste' : 3,
    'num_fontes_sul' : 3,
    'num_fontes_nordeste' : 3,
    'num_fontes_norte' : 2
    }

    # Página 1
    balanco = {
    'programado_lf' : 'left:(27[0-9]|28[0-9])px',
    'programado_tp' : 'top:(30[0-9]|31[0-9])px',
    'verificado_lf' : 'left:(36[0-9]|37[0-9])px',
    'verificado_tp' : 'top:(30[0-9]|31[0-9])px'
    }
    
    
    sudeste = {
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

    'ear_tp' : 'top:(140[0-9]|141[0-9]|142[0-9]|143[0-9]|144[0-9])px', 
    'ear_lf' : 'left:(35[0-9]|36[0-9]|37[0-9]|38[0-9]|39[0-9]|40[0-9])px'
    }


    sul = {
    'fontes_tp' : 'top:(138[0-9]|139[0-9]|140[0-9]|141[0-9]|142[0-9]|143[0-9])px', 
    'fontes_lf' : 'left:(17[0-9]|18[0-9]|19[0-9]|20[0-9])px',

    'prod_verif_tp' : 'top:(139[0-9]|140[0-9]|141[0-9]|142[0-9]|143[0-9]|144[0-9])px', 
    'prod_verif_lf' : 'left:(27[0-9]|28[0-9]|29[0-9]|29[0-9]|30[0-9]|31[0-9])px',
    'prod_prog_tp' : 'top:(139[0-9]|140[0-9]|141[0-9]|142[0-9]|143[0-9]|144[0-9])px', 
    'prod_prog_lf' : 'left:(31[0-9]|32[0-9]|33[0-9]|34[0-9]|35[0-9])px',

    'carga_verif_tp' : 'top:(143[0-9]|144[0-9]|145[0-9]|146[0-9]|147[0-9]|148[0-9])px', 
    'carga_verif_lf' : 'left:(27[0-9]|28[0-9]|29[0-9]|29[0-9]|30[0-9]|31[0-9])px',
    'carga_prog_tp' : 'top:(143[0-9]|144[0-9]|145[0-9]|146[0-9]|147[0-9]|148[0-9])px', 
    'carga_prog_lf' : 'left:(30[0-9]|31[0-9]|33[0-9]|34[0-9]|35[0-9])px',

    'ena_tp' : 'top:(145[0-9]|146[0-9]|147[0-9]|148[0-9]|149[0-9]|150[0-9])px', 
    'ena_lf' : 'left:(26[0-9]|27[0-9]|28[0-9]|29[0-9]|30[0-9]|31[0-9])px',

    'ear_tp' : 'top:(150[0-9]|151[0-9]|152[0-9]|153[0-9]|154[0-9]|155[0-9])px', 
    'ear_lf' : 'left:(21[0-9]|22[0-9]|23[0-9]|24[0-9]|25[0-9]|26[0-9])px'
    }
    
## TODO erro aqui
    nordeste = {
    'fontes_tp' : 'top:(110[0-9]|111[0-9])px', 
    'fontes_lf' : 'left:(35[0-9]|36[0-9]|37[0-9]|38[0-9]|39[0-9])px',

    'prod_verif_tp' : 'top:(111[0-9]|112[0-9]|113[0-9]|114[0-9])px', 
    'prod_verif_lf' : 'left:(44[0-9]|45[0-9]|46[0-9]|47[0-9]|48[0-9])px',
    'prod_prog_tp' : 'top:(111[0-9]|112[0-9]|113[0-9]|114[0-9])px',  
    'prod_prog_lf' : 'left:(48[0-9]|49[0-9]|50[0-9]|51[0-9]|52[0-9])px',

    'carga_verif_tp' : 'top:(114[0-9]|115[0-9]|116[0-9]|117[0-9])px', 
    'carga_verif_lf' : 'left:(44[0-9]|45[0-9]|46[0-9]|47[0-9]|48[0-9])px',
    
    'carga_prog_tp' : 'top:(114[0-9]|115[0-9]|116[0-9]|117[0-9])px', 
    'carga_prog_lf' : 'left:(49[0-9]|50[0-9]|51[0-9]|52[0-9])px',

    'ena_tp' : 'top:(116[0-9]|117[0-9]|118[0-5])px', 
    'ena_lf' : 'left:(44[0-9]|45[0-9]|46[0-9]|47[0-9]|48[0-9])px',

    'ear_tp' : 'top:(120[0-9]|121[0-9]|122[0-9]|123[0-9])px', 
    'ear_lf' : 'left:(40[0-9]|41[0-9]|42[0-9]|43[0-9])px'
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