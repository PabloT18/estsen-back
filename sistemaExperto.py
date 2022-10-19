from clips import Environment
from models import RecoPictogramas, RecoFiguras, RecoLuces, Recomendacion

def recomendacionSE(discapacidad, edadCron, edadDesa):

    
    mi_diccionario = {"recPic":0,"recFig":0,"recLuc":0}


    clp = Environment()
    clp.reset()

    clp.load('sis_est.clp')


  

    clp.eval("(assert (discapacidad "+str(discapacidad)+"))")
    clp.eval("(assert (edadCron "+str(edadCron)+"))")
    clp.eval("(assert (edadDesa "+str(edadDesa)+"))")



    clp.run()
    
  


    evaluar1 = "(find-all-facts ((?x recommendationPictogramas )) TRUE)"
    evaluar2 = "(find-all-facts ((?x recommendationFiguras )) TRUE)"
    evaluar3 = "(find-all-facts ((?x recommendationLuces )) TRUE)"


    value1  =  clp.eval(evaluar1)
    value2  =  clp.eval(evaluar2)
    value3  =  clp.eval(evaluar3)



    if(len(value1)>0):
        valPic=dict(value1[0])
        Figuras = valPic.get("Figuras")
        SigFase = valPic.get("SigFase")
        Frases = valPic.get("Frases")
        Secuencias = valPic.get("Secuencias")
        
        recPic = RecoPictogramas(Figuras, SigFase, Frases, Secuencias)
      
        # recLuc = RecoLuces(0,0,0,0,0,0,0,0)
        mi_diccionario["recPic"] = recPic.__dict__

    if(len(value2)>0):
        valFig=dict(value2[0])
        figRec = valFig.get('FigRec')
        figSec = valFig.get('FigSec')
        figSdi = valFig.get('FigSdi')
        figSco = valFig.get('FigSco')
        aniRec = valFig.get('AniRec')
        aniSec = valFig.get('AniSec')
        aniOno = valFig.get('AniOno')
        aniTex = valFig.get('AniTex')
        aniSdi = valFig.get('AniSdi')
        aniSco = valFig.get('AniSco')
        
        recFig = RecoFiguras(figRec,figSec,figSdi,figSco,aniRec,aniSec,aniOno,aniTex,aniSdi,aniSco)
        mi_diccionario["recFig"] = recFig.__dict__

    if(len(value3)>0):
        valFig=dict(value3[0])
        
        jueLib = valFig.get('JueLib')
        reaCam = valFig.get('ReaCam')
        recCol = valFig.get('RecCol')
        relObj = valFig.get('RelObj')
        secCol = valFig.get('SecCol')
        lanDir = valFig.get('LanDir')
        secDir = valFig.get('SecDir')
        secAlt = valFig.get('SecAlt')
        
        recLuc = RecoLuces(jueLib,reaCam,recCol,relObj,secCol,lanDir,secDir,secAlt)
        mi_diccionario["recLuc"] = recLuc.__dict__
    
    clp.reset()
    
    
    return mi_diccionario



