import re
from fastapi import FastAPI
 
import sistemaExperto as SE



app = FastAPI(title='Sistema Estimulacion Sensorial',
            description='Sistema REST y comunicacion con Sistema Experto',
            version='1.0.1')

@app.get('/')
def index():
    return 'Sistema Experto'

# @app.get('/recomendacion')
# async def recomendacion(datos: RecomendacionRequestModel):
#     SE.recomendacionSE(datos.discapacidad,datos.edadCron,datos.edadDesa)
#     return 'Sistema Experto'
# discapacidad=0&edadCron=0&edadDesa=0

@app.get('/recomendacion/{discapacidad,edadCron,edadDesa}')
async def recomendacion(discapacidad,edadCron,edadDesa):
    print(discapacidad)
    print(edadCron)
    print(edadDesa)
    response = SE.recomendacionSE(discapacidad,edadCron,edadDesa)
    
    return response 