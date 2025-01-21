from registro_de_personas import *

def nomina():
    
    try :
        with open(f"crear_nomina/personas.json","r") as registros:
            cargar =json.load(registros)
    except:
        print("no se ha creado el archivo del")
        cargar=[{}]
        
        identificador = int(input("digite el identificador del sujeto"))
    for p in cargar:
        if p["identificacion"] == identificador:
          
           with open(f"crear_nomina/nomina{id}.json","a") as registros:
             salud  = p["salario"] *4/100
             print(salud)
             pension = p["salario"] *4/100
             print(pension)
             if p["salario"] < 2000000:
                 auxilio_de_transporte = p["salario"] *10/100 + p["salario"]
                 print(auxilio_de_transporte)
             else:
                  if p["inasistencia"] >= 1:
                      dia = p["saldo"] / 30  
                      print("por inasistencia es" + p["saldo"]-dia*p["inasistencia"])
                  else:
                      if p["bonos"] >1:
                          print(p["saldo"]+p["bonos"])
                                        
             

             json.dump(cargar,registros) 