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

gastos = {"Sueldo Ariel":{"Monto":"500000","Descripción":"Sueldo correspondiente a Ariel"},
          "Sueldo Jorge":{"Monto":"500000","Descripción":"Sueldo correspondiente a Jorge"},
          "Sueldo Pepe":{"Monto":"500000","Descripción":"Sueldo correspondiente a Pepe"},
          "Plomero":{"Monto":"20000","Descripción":"Arreglo cañería 8A"}
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
    
    
    #Eventos
    def cambio_de_pagina(e: ft.ControlEvent):
        page.views.clear()
        if e.data == "0" and page.route != "/main":
            page.go("/main")
        elif e.data == "1" and page.route != "/agregar_inquilinos":
            page.go("/agregar_inquilinos")
    
    def ingresar_o_modificar(e : ft.OptionalControlEventCallable,aux = False):
        def funcion_auxiliar(f):
            ingresar_o_modificar(f,aux=True)
            page.close(alerta_inquilino_ya)
            page.open(ft.SnackBar(ft.Text("Inquilino Modificado")))
            return
        alerta_expensas = ft.AlertDialog(
                                modal=True,
                                title=ft.Text("ALERTA"),
                                content=ft.Text("Por favor ingrese numeros con puntos y sin coma"),
                                actions=[
                                    ft.TextButton("Perdón no lo hago de vuelta", on_click=lambda e: page.close(alerta_expensas)),
                                ],
                                actions_alignment=ft.MainAxisAlignment.END,
                            )
        alerta_inquilino_ya = ft.AlertDialog(
                                modal=True,
                                title=ft.Text("ALERTA"),
                                content=ft.Text("El inquilino ya se encuentra registrado"),
                                actions=[
                                    ft.FilledButton("Modificar",color="#326C71",on_click=funcion_auxiliar),
                                    ft.TextButton("Cancelar",on_click=lambda f: page.close(alerta_inquilino_ya)),
                                ],
                                actions_alignment=ft.MainAxisAlignment.END,
                            )
        try:
            float(expensas.value)
            if (departamento.value not in inquilinos) or aux:
                inquilinos[departamento.value] = {
                "Inquilino":nombre_completo.value,
                "Expensas":expensas.value,
                "Tipo de pago":tipo_de_pago.value,
                "Pagó?":ya_pago.value
                }
                page.update()
            else:
                page.open(alerta_inquilino_ya)

        except ValueError:
            page.open(alerta_expensas)
        
        tabla_principal.rows = dict_to_rows(inquilinos)
        tabla_principal.update()
    
    

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
    
    tabla_gastos = ft.DataTable([ft.DataColumn(ft.Text("Gasto")),
                                 ft.DataColumn(ft.Text("Monto")),
                                 ft.DataColumn(ft.Text("Descripción"))],
                                 rows = dict_to_rows(gastos),
                                 show_bottom_border=True,
                                 border = ft.border.all(5,"#326C71"),
                                 )
    
    departamento = ft.TextField(label="Departamento")
    
    nombre_completo = ft.TextField(label="Nombre Completo")      
    
    expensas = ft.TextField(label="Expensas",hint_text="Decimales con puntos y sin coma")
    
    tipo_de_pago = ft.Dropdown(value="Tipo de pago",options=tipos_de_pago_flet(tipos_de_pago),
                                            key=dropdown_changed)

    ya_pago = ft.Dropdown(options=[ft.DropdownOption(text="Sí",key="Sí"),ft.DropdownOption(text="No",key="No")])
    
    
    drawer_principal = ft.NavigationDrawer(
        on_change=cambio_de_pagina,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Página Principal",
                icon=ft.Icons.HOUSE_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.HOUSE),
            ),
            ft.Divider(thickness=3),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.PERSON_ADD_OUTLINED),
                label="Agregar/modificar inquilinos",
                selected_icon=ft.Icons.PERSON_ADD,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.PERSON_REMOVE_OUTLINED),
                label="Quitar Inquilino",
                selected_icon=ft.Icons.PERSON_REMOVE,
            ),
            ft.Divider(thickness=1,opacity=1),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.ANALYTICS_OUTLINED),
                label="Agregar Gastos",
                selected_icon=ft.Icons.ANALYTICS
            )
        ]
    )


    #Páginas
    
    
    pagina_principal =ft.Row(
                            controls=[
                                        ft.Column(
                                            [tabla_principal],alignment=ft.MainAxisAlignment.END
                                            ,height=400),
                                        ft.Column(
                                            [tabla_gastos],alignment=ft.MainAxisAlignment.END
                                            ,height=400)
                                    ],
                            alignment=ft.MainAxisAlignment.CENTER
                            )


    
    pagina_inquilinos =ft.Column([ft.Row(
        [
          ft.Column([departamento]),
          ft.Column([
            nombre_completo,
            expensas
          ]),
          ft.Column([
              tipo_de_pago,
              ya_pago
          ]),
          ft.Column([
              ft.Button("Agregar/modificar inquilino",color="#326C71",on_click=ingresar_o_modificar)
          ],
                    alignment=ft.MainAxisAlignment.END)
        ],alignment=ft.MainAxisAlignment.CENTER
    ),
                                  tabla_principal
                                  ],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    
    
    
    
    
    
    def route_control(route):
        page.views.clear()
        page.views.append(
            ft.View("/main",
                    [
                        ft.FloatingActionButton(icon=ft.Icons.MENU,on_click=lambda e:page.open(drawer_principal)),
                        pagina_principal
                    ],drawer=drawer_principal,scroll=ft.ScrollMode.ADAPTIVE
                    )
        )
        page.update()
        if page.route == "/agregar_inquilinos":
            page.views.append(
            ft.View("/agregar_inquilinos",
                    [
                        ft.FloatingActionButton(icon=ft.Icons.MENU,on_click=lambda e:page.open(drawer_principal)),
                        pagina_inquilinos
                    ], drawer=drawer_principal,scroll=ft.ScrollMode.ADAPTIVE
                    )
            )
            page.update()
   
    


    page.on_route_change = route_control
    page.go(page.route)
    

    
    pass









if __name__ == "__main__":
    ft.app(target= main,name="Consorciapp")





# Necesito una lista de inquilinos para poder mover los datos
# Lista_de_inquilinos es el nombre de mi variable
# Tambien puede ser Diccionario_de_inqulinos=
# {"Departamento":"kasmdka","Inquilino": "kasndjasdna","Expensas":"ajsndajda","Tipo de pago":"ksdmfasdf"}