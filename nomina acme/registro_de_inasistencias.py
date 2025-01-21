from datetime import *
from registro_de_personas import *
import json

def tiempo():
    fecha = date.today()
    hora = datetime.now()
    hora_personalizada = hora.strftime("%H:%M")
    return f"el dia {fecha} // a las {hora_personalizada}"

def inasistencias():
    
    try :
        with open(f"crear_nomina/personas.json","r") as registros:
            cargar =json.load(registros)
    except:
        print("no se ha creado el archivo del")
        cargar=[{}]
        
    print("bienvenido a colocar inasistencias")
    inasistencia = int(input("digite el identificador del sujeto"))

    
    for p in cargar:
        if p["identificacion"] == inasistencia:
          
           with open(f"crear_nomina/personas.json","w") as registros:
             p["inasistencia"] += 1

             json.dump(cargar,registros) 
             
    for p in cargar:
        if p["identificacion"] == inasistencia:
          
           with open(f"crear_nomina/inasistencia.json","a") as registros:
                p["identificacion"]
                p["dia"] += tiempo()
                json.dump(cargar,registros)       
    
        
    