# Primero veamos que es lo que quiero
# Programa para mantener al día a mi papá con los distintos ingresos y gastos de el consorcio
# que tipo de tareas hay que hacer?
# 1 - mantener todos los que pagaron y los que no
# 2 - sumar cuanto se pagó al final del mes
# 3 - interfaz para ingreso de datos
# 4 - permanencia de datos
# 5 - 
#
# diseño burdo de como va a ser la app:
# https://www.figma.com/design/vSGNFtqIyQGVzrQL68UCga/App-para-consorcio?node-id=1-3&t=ELhwJEeQ6tgYoq3x-1 
#


# ¿cómo voy a guardar mis inquilinos? con diccionarios
# cada inquilino es un {diccionario}
#{"Departamento":"kasmdka","Inquilino": "kasndjasdna","Expensas":"ajsndajda","Tipo de pago":"ksdmfasdf"}




import flet as ft
import json

def switch_to_second_page(page: ft.Page):
    page.clean()
    agregar_inquilino(page)

tipos_de_pago = ["Pesos","Dólares","Otro"]

def agregar_inquilino(e):
    
    def tipos_de_pago_flet(tipos_de_pago : list) -> list:
        lista_tipo_pago_flet = []
        for i in range(len(tipos_de_pago)):
            lista_tipo_pago_flet.append(
                ft.DropdownOption(key=tipos_de_pago[i],text=tipos_de_pago[i]))
        return lista_tipo_pago_flet
    
    def dropdown_changed(e):
        tipo_de_pago_inquilino = e
        return tipo_de_pago_inquilino


    def submain(Page : ft.Page):
        while True:
            try:
                nombre_completo = ft.TextField(label="Nombre Completo")
                expensas = ft.TextField(label="Expensas",hint_text="Ingrese decimales con coma y sin puntos.")
                tipo_de_pago = ft.Dropdown(options=tipos_de_pago_flet(tipos_de_pago),
                                           on_change=dropdown_changed,
                                           key="")
                Page.add(nombre_completo,
                         expensas,
                         tipo_de_pago)

            except Exception as e:
                print (e)
    # ft.app(target= submain)
    pass














inquilinos ={"1A":{"Inquilino":"Pablo Hearne","Expensas":"300000","Tipo de pago":"Pesos","Pagó?":"Sí"},
             }

def dict_to_rows(inquilinos : dict) -> list:
    inquilinos_list = list(inquilinos.keys())
    rows_inq = []
    cells = []
    for i in range(len(inquilinos)):
        categoria = list(inquilinos[inquilinos_list[i]].keys())
        cells.append(ft.DataCell(
        ft.Text(f"{inquilinos_list[i]}"))
        )
        for j in range(len(categoria)):
            cells.append(ft.DataCell(
                ft.Text(f"{inquilinos[inquilinos_list[i]][categoria[j]]}"))
            )
        rows_inq.append(ft.DataRow(cells))
    return rows_inq



def main(page : ft.Page):
    """Cuerpo de la app"""
    #Configuración
    page.title = "Consorciapp"
    page.bgcolor = "#BAFDE1"
    page.vertical_alignment = ft.MainAxisAlignment.END
    page.horizontal_alignment = "CENTER"
    #Eventos




    #Componentes
    txt_prueba = ft.Text(value= "prueba",text_align=ft.MainAxisAlignment.CENTER)
    tabla_principal = ft.DataTable([ft.DataColumn(ft.Text("Departamento")),
                                    ft.DataColumn(ft.Text("Inquilino")),
                                    ft.DataColumn(ft.Text("Expensas")),
                                    ft.DataColumn(ft.Text("Tipo de pago")),
                                    ft.DataColumn(ft.Text("Pagó?"))],
                                    rows = dict_to_rows(inquilinos),
                                            show_bottom_border=True,
                                            border = ft.border.all(5,"#326C71"),
                                            )
    
    btn_agregar = ft.FilledTonalButton("Agregar",ft.Icons.ADD,
                                       on_focus=ft.Text("Agregar Inquilino NUevo"),color="#BAFDE1",
                                       bgcolor="#326C71",
                                       on_click=switch_to_second_page(page))
    

    page.add(tabla_principal)
    


    page.add(btn_agregar)
    pass









if __name__ == "__main__":
    ft.app(target= main)





# Necesito una lista de inquilinos para poder mover los datos
# Lista_de_inquilinos es el nombre de mi variable
# Tambien puede ser Diccionario_de_inqulinos=
# {"Departamento":"kasmdka","Inquilino": "kasndjasdna","Expensas":"ajsndajda","Tipo de pago":"ksdmfasdf"}