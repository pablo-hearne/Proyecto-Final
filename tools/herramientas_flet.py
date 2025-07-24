import flet as ft
import tools.guardado_y_lectura as guardado_y_lectura



def tipos_de_pago_flet(tipos_de_pago : list) -> list:
    lista_tipo_pago_flet = []
    for i in range(len(tipos_de_pago)):
        lista_tipo_pago_flet.append(
            ft.DropdownOption(key=tipos_de_pago[i],text=tipos_de_pago[i]))
    return lista_tipo_pago_flet

def dropdown_changed(e):
    tipo_de_pago_inquilino = e
    return tipo_de_pago_inquilino.data


def dict_to_rows(inquilinos : dict) -> list:
    inquilinos_list = list(inquilinos.keys())
    rows_inq = []
    cells = []
    for i in range(len(inquilinos)):
        cells = []
        categoria = list(inquilinos[inquilinos_list[i]].keys())
        cells.append(ft.DataCell(
        ft.Text(inquilinos_list[i]))
        )
        for j in range(len(categoria)):
            cells.append(ft.DataCell(
                ft.Text(f"{inquilinos[inquilinos_list[i]][categoria[j]]}"))
            )
        rows_inq.append(ft.DataRow(cells))
    return rows_inq

def dict_to_list(inquilinos:dict) -> list:
    datos = inquilinos.keys()
    lista = []
    for i in datos:
        info = list(inquilinos[i].keys())
        lista.append(ft.DropdownOption(
                key=i,
                text=str(i) + " - "+str(inquilinos[i][info[0]]))
                     )
    return lista

def window_event_handler(e: ft.WindowEvent,inquilinos,gastos,alerta_cerrar,page):
    if e.type == ft.WindowEventType.CLOSE:
        guardado_y_lectura.guardar(inquilinos,gastos)
        page.open(alerta_cerrar)

        




