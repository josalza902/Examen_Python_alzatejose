from registro_de_personas import *
from datetime import *
def tiempo():
    fecha = date.today()
    hora = datetime.now()
    hora_personalizada = hora.strftime("%H:%M")
    return f"el dia {fecha} // a las {hora_personalizada}"

def registro_bonos():
    try :
        with open(f"crear_nomina/personas.json","r") as registros:
            cargar =json.load(registros)
    except:
        print("no se ha creado el archivo del")
        cargar =[{}]
        
    print("bienvenido a colocar bonos")
    identificador = int(input("digite el identificador del sujeto"))
    print("bienvenido a colocar bonos")
    monto = int(input("digite la cantidad del bono"))
    
    for p in cargar:
        if p["identificacion"] == identificador:
          
           with open(f"crear_nomina/personas.json","w") as registros:
             p["bonos"] += monto

             json.dump(cargar,registros) 