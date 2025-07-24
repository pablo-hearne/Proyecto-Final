


def ganancias(inquilinos:dict,gastos:dict):
    expensas_total_pesos = 0
    gastos_total_pesos = 0
    expensas_total_dolares = 0
    gastos_total_dolares = 0
    expensas_total_otros = 0
    gastos_total_otros = 0
    for inquilino in inquilinos:
        uno = inquilinos[inquilino]["Tipo de pago"] == "Pesos"
        dos = inquilinos[inquilino]["Tipo de pago"] == "Dólares"
        if uno and inquilinos[inquilino]["Pagó?"] == "Sí":
            expensas_total_pesos += float(inquilinos[inquilino]["Expensas"])
        elif dos and inquilinos[inquilino]["Pagó?"] == "Sí":
            expensas_total_dolares += float(inquilinos[inquilino]["Expensas"])
            print(expensas_total_dolares)
        elif inquilinos[inquilino]["Pagó?"] == "Sí" and not (uno or dos):
            expensas_total_otros += float(inquilinos[inquilino]["Expensas"])
    for gasto in gastos:
        keys = list(gastos[gasto].keys())
        if gastos[gasto][keys[2]] == "Pesos":
            gastos_total_pesos += float(gastos[gasto]["Monto"])
        elif gastos[gasto][keys[2]] == "Dólares":
            gastos_total_dolares += float(gastos[gasto]["Monto"])
        else:
            gastos_total_otros += float(gastos[gasto]["Monto"])
    ganancias_pesos = expensas_total_pesos - gastos_total_pesos
    ganancias_dolares = expensas_total_dolares - gastos_total_dolares
    ganancias_otros = expensas_total_otros - gastos_total_otros
    return [[ganancias_pesos,expensas_total_pesos,gastos_total_pesos],
            [ganancias_dolares,expensas_total_dolares,gastos_total_dolares],
            [ganancias_otros,expensas_total_otros,gastos_total_otros]]



