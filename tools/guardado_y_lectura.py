import json




def guardar(inquilinos,gastos):
    with open(r"storage/inquilinos.json","w+") as archivo_inquilinos:
        json.dump(inquilinos,archivo_inquilinos)
    with open(r"storage/gastos.json","w+") as archivo_gastos:
        json.dump(gastos,archivo_gastos)
    return

def str_a_dict(futuro_diccionario:str):
    diccionario = eval(futuro_diccionario)
    return diccionario

def leer_json():
    try:
        with open(r"storage/gastos.json") as archivo_gastos:
            gastos = json.load(archivo_gastos)
        with open(r"storage/inquilinos.json") as archivo_inquilinos:
            inquilinos = json.load(archivo_inquilinos)
        # for gasto in gastos:
        #     print(type(gasto))
        #     gastos[gasto] = eval(gastos[gastos])
        # for inquilino in inquilinos:
        #     inquilinos[inquilinos] = eval(inquilinos[inquilino])
        
    except Exception as e:
        print(e)
        inquilinos={}
        gastos={}
    return inquilinos,gastos
