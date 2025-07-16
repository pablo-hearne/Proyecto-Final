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

def inquilinos_para_flet():
    pass














inquilinos ={}





def main(page : ft.Page):
    """Cuerpo de la app"""
    #Configuración
    page.title = "Consorciapp"
    page.bgcolor = "#BAFDE1"
    page.vertical_alignment = ft.MainAxisAlignment.END
    page.horizontal_alignment = "CENTER"
    #Eventos

    def dict_to_rows(inquilinos : dict) -> list:
        inquilinos_list = inquilinos.keys()
        rows_inq = []
        for i in len(inquilinos):
            rows_inq.append(ft.DataCell(
            ft.Text(f"{inquilinos_list[i]}"))
            )
            rows_inq.append(ft.DataCell(
                ft.Text(f"{inquilinos[inquilinos_list[i]]["Inquilino"]}"))
            )
            rows_inq.append(ft.DataCell(
                ft.Text(f"{inquilinos[inquilinos_list[i]]["Expensas"]}"))
            )
            rows_inq.append(ft.DataCell(
                ft.Text(f"{inquilinos[inquilinos_list[i]]["Tipo de Pago"]}"))
            )
            rows_inq.append(ft.DataCell(
                ft.Text(f"{inquilinos[inquilinos_list[i]]["Pagó?"]}"))
            )
        return rows_inq




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
                                       bgcolor="#326C71")
    

    # page.add(tabla_principal)
    


    page.add(txt_prueba)
    pass









if __name__ == "__main__":
    ft.app(target= main)





# Necesito una lista de inquilinos para poder mover los datos
# Lista_de_inquilinos es el nombre de mi variable
# Tambien puede ser Diccionario_de_inqulinos=
# {"Departamento":"kasmdka","Inquilino": "kasndjasdna","Expensas":"ajsndajda","Tipo de pago":"ksdmfasdf"}