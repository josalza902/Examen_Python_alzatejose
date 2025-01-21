import json
def registro_personas():
    crear_registro = []
    try:
        id = int(input("digite el numero de identificacion "))
    except:
        print("digite solo numeros porfavor")
        return
    nombre = input("digite el nombre de la persona")
    cargo =input("digite el cargo de la persona").upper()
    salario = int(input("digite el salario de la persona"))
        
    registro = {
        "identificacion":id,
        "nombre": nombre,
        "cargo": cargo,
        "salario": salario,
        "inasistencia": 0,
        "dia":"",
        "bonos" : 0
    }
    
    
    
    try :
        with open(f"crear_nomina/personas.json","r") as registros:
            crear_registro =json.load(registros)
    except:
        print("no se ha creado el archivo del")
    
    crear_registro.append(registro)
    
    print(crear_registro)
    
    try:
        with open(f"crear_nomina/personas.json", "w") as añadir:
        
            escribir = json.dumps(crear_registro)
            añadir.write(escribir)    
    
    except:
        print("no se pudo crear")
        