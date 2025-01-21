from registro_de_personas import *
from registro_de_bonos import *
from registro_de_inasistencias import *


opc = 0

while opc != 6:
    print("bienvenido al inventario")
    print(f"\n presione 1 para registro de empleado")
    print(f"\n presione 2 para registro de inasistencia")
    print(f"\n presione 3 para registro de bono")
    print(f"\n presione 6 para salir")
    opc = int(input("digite un numero: "))
    match opc:
        case 1:
            print("registro de empleados")
            registro_personas()
        case 2:
            print("registro de inasistencias")
            inasistencias()
        case 3: 
            print("registro de bonos extralegales")
            registro_bonos()
        case 4:
            print("calculo de nomina")
        case 6:
            print("usted ha salido del programa")
        case _:
            print("no es una opcion factible")