import json
import re



class Laptop:
	def __init__(self, name, processor, hdd, ram, cost):
		self.name = name
		self.processor = processor
		self.hdd = hdd
		self.ram = ram
		self.cost = cost 
class RecoPictogramas:
    def __init__(self,figuras,sigFase,frases,secuencias):
        self.figuras=figuras
        self.sigFase=sigFase
        self.frases=frases
        self.secuencias=secuencias


class RecoFiguras:
    def __init__(self,figRec,figSec,figSdi,figSco,aniRec,aniSec,aniOno,aniTex,aniSdi,aniSco):
        self.figRec =figRec
        self.figSec =figSec
        self.figSdi =figSdi
        self.figSco =figSco
        self.aniRec =aniRec
        self.aniSec =aniSec
        self.aniOno =aniOno
        self.aniTex =aniTex
        self.aniSdi =aniSdi
        self.aniSco =aniSco


class RecoLuces:
    def __init__(self,jueLib,reaCam,recCol,relObj,secCol,lanDir,secDir,secAlt):
        self.jueLib = jueLib
        self.reaCam = reaCam
        self.recCol = recCol
        self.relObj = relObj
        self.secCol = secCol
        self.lanDir = lanDir
        self.secDir = secDir
        self.secAlt = secAlt

class Recomendacion:
    recoPictogramas: RecoPictogramas
    recoFiguras: RecoFiguras
    recoLuces: RecoLuces

    # def __dict__():
    #     return 'holaaaa'

   