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






tipos_de_pago = ["Pesos","Dólares","Otro"]

inquilinos ={"1A":{"Inquilino":"Pablo Hearne","Expensas":"300000","Tipo de pago":"Pesos","Pagó?":"Sí"},
             "1b":{"Inquilino":"Pablo Hearne","Expensas":"300000","Tipo de pago":"Pesos","Pagó?":"Sí"},
             "1a":{"Inquilino":"Pablo Hearne","Expensas":"300000","Tipo de pago":"Pesos","Pagó?":"Sí"},
             "KK":{"Inquilino":"Pablo Hearne","Expensas":"300000","Tipo de pago":"Pesos","Pagó?":"Sí"},
             "1B":{"Inquilino":"Pablo Hearne","Expensas":"300000","Tipo de pago":"Pesos","Pagó?":"Sí"},
             "2A":{"Inquilino":"Pablo Hearne","Expensas":"300000","Tipo de pago":"Pesos","Pagó?":"Sí"},
             }

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

def ingresar_o_modificar(Page : ft.Page):
    while True:
        try:
            nombre_completo = ft.TextField(label="Nombre Completo")           
            expensas = ft.TextField(label="Expensas",hint_text="Ingrese decimales con coma y sin puntos.")
            tipo_de_pago = ft.Dropdown(options=tipos_de_pago_flet(tipos_de_pago),
                                        on_change=dropdown_changed,
                                        key=dropdown_changed)
            ya_pago = ft.Dropdown(options=[ft.DropdownOption(text="Sí",key="si"),ft.DropdownOption(text="No",key="no")])
            Page.add(nombre_completo,
                        expensas,
                        tipo_de_pago,
                        ya_pago)
            

        except Exception as e:
            print (e)
    return

def mostrar_drawer(e):
    page.view = True
    page.drawer.update()
    return



# Ejecución del programa


def main(page : ft.Page):
    """Cuerpo de la app"""
    #Configuración
    page.scroll = True
    page.title = "Consorciapp"
    page.bgcolor = "#BAFDE1"
    page.window.bgcolor = "#326C71"
    page.window.icon = (ft.Icon(ft.Icons.ACCOUNT_BALANCE_OUTLINED))
    #   PORQUE NO CAMBIA EL ICONO LPM
    page.vertical_alignment = ft.MainAxisAlignment.END
    page.horizontal_alignment = "CENTER"
    #       ESTOS ALIGMENTS ESTÁN SOBERANAMENTE AL PEDO
    
    #NO FUNCIONA NADA EN ÉSTA CASA
    
    
    #Eventos
    def cambio_de_pagina(e: ft.ControlEvent):
        page.views.clear()
        if e.data == "0":
            page.go("/main")
        elif e.data == "1":
            page.go("/agregar_inquilinos")
    

    
    #Componentes
    
    tabla_principal = ft.DataTable([ft.DataColumn(ft.Text("Departamento")),
                                    ft.DataColumn(ft.Text("Inquilino")),
                                    ft.DataColumn(ft.Text("Expensas")),
                                    ft.DataColumn(ft.Text("Tipo de pago")),
                                    ft.DataColumn(ft.Text("Pagó?"))],
                                    rows = dict_to_rows(inquilinos),
                                    show_bottom_border=True,
                                    border = ft.border.all(5,"#326C71"),
                                    )
    
    nombre_completo = ft.TextField(label="Nombre Completo")      
    
    
    expensas = ft.TextField(label="Expensas",hint_text="Decimales con coma y sin puntos")
    
    
    tipo_de_pago = ft.Dropdown(value="Tipo de pago",options=tipos_de_pago_flet(tipos_de_pago),
                                            key=dropdown_changed)
    
    
    ya_pago = ft.Dropdown(options=[ft.DropdownOption(text="Sí",key="si"),ft.DropdownOption(text="No",key="no")])
    
    
    drawer_principal = ft.NavigationDrawer(
        on_change=cambio_de_pagina,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Página Principal",
                icon=ft.Icons.HOUSE_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.HOUSE),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.ADD_BUSINESS_OUTLINED),
                label="Agregar/modificar inquilinos",
                selected_icon=ft.Icons.ADD_BUSINESS,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.PHONE_OUTLINED),
                label="Quitar Inquilino",
                selected_icon=ft.Icons.PHONE,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.ANALYTICS_OUTLINED),
                label="Gastos",
                selected_icon=ft.Icons.ANALYTICS
            )
        ]
    )


    #Páginas
    
    
    pagina_principal = ft.Row(controls=[
        
        ft.Row(
                            controls=[
                                        # ft.Column([boton_drawer],alignment=ft.MainAxisAlignment.START),
                                        ft.Column(
                                            [tabla_principal],alignment=ft.MainAxisAlignment.END
                                            ,height=400),
                                    ],
                            alignment=ft.MainAxisAlignment.CENTER
                            )],
                              alignment=ft.MainAxisAlignment.CENTER)


    
    
    pagina_inquilinos = ft.Row([
        # drawer,
        ft.Row(
        [
        #   ft.Column([boton_drawer],alignment=ft.MainAxisAlignment.START),
          ft.Column([
            nombre_completo,
            expensas
          ]),
          ft.Column([
              tipo_de_pago,
              ya_pago
          ]),
        ]
    )
    ],alignment=ft.MainAxisAlignment.CENTER)
    
    
    
    
    
    
    def route_control(route):
        page.views.clear()
        page.views.append(
            ft.View("/main",
                    [
                        ft.FloatingActionButton(icon=ft.Icons.MENU,on_click=lambda e:page.open(drawer_principal)),
                        pagina_principal
                    ],drawer=drawer_principal
                    )
        )
        page.update()
        if page.route == "/agregar_inquilinos":
            page.views.append(
            ft.View("/agregar_inquilinos",
                    [
                        ft.FloatingActionButton(icon=ft.Icons.MENU,on_click=lambda e:page.open(drawer_principal)),
                        pagina_inquilinos,
                        ft.Button("Terminar de agregar",on_click=lambda e: page.go("/main"))
                    ], drawer=drawer_principal
                    )
            )
            page.update()
   
    


    page.on_route_change = route_control
    page.go(page.route)
    

    
    pass









if __name__ == "__main__":
    ft.app(target= main)





# Necesito una lista de inquilinos para poder mover los datos
# Lista_de_inquilinos es el nombre de mi variable
# Tambien puede ser Diccionario_de_inqulinos=
# {"Departamento":"kasmdka","Inquilino": "kasndjasdna","Expensas":"ajsndajda","Tipo de pago":"ksdmfasdf"}