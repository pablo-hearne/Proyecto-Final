import flet as ft
from tools.funciones import *
from tools.guardado_y_lectura import *
from tools.herramientas_flet import *

inquilinos,gastos = guardado_y_lectura.leer_json()
tipos_de_pago = ["Pesos","Dólares","Otro"]

# Ejecución del programa


def main(page : ft.Page):
    """Cuerpo de la app"""
    #Configuración
    page.window.prevent_close = True
    page.window.on_event = lambda e: window_event_handler(e,inquilinos,gastos,alerta_cerrar,page)
    page.scroll = True
    page.title = "Consorciapp"
    page.bgcolor = "#BAFDE1"
    page.window.bgcolor = "#326C71"
    page.window.icon = "icon.ico"

    
    #Eventos
    
    def actualizar_listas():
        lista_gastos.options = dict_to_list(gastos)
        lista_inquilinos.options = dict_to_list(inquilinos)
        lista_inquilinos.update()
        lista_inquilinos.update()
        page.update()
        return
    
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
        elif page.route == "/agregar_gastos":
            page.views.append(
                ft.View("/agregar_gastos",
                        [
                            ft.FloatingActionButton(icon=ft.Icons.MENU,on_click=lambda e:page.open(drawer_principal)),
                            pagina_gastos
                        ],drawer=drawer_principal,scroll=ft.ScrollMode.ADAPTIVE 
                )
            )
            page.update()
        elif page.route == "/modificar":
            page.views.append(
                ft.View("/modificar",
                    [
                        ft.FloatingActionButton(icon=ft.Icons.MENU,on_click=lambda e:page.open(drawer_principal)),
                        pagina_modificar
                    ],drawer=drawer_principal,scroll=ft.ScrollMode.ADAPTIVE
                    )
            )
            page.update()
        elif page.route == "/resumen":
            page.views.append(    
                ft.View("/resumen",
                    [
                        ft.FloatingActionButton(icon=ft.Icons.MENU,on_click=lambda e:page.open(drawer_principal)),
                        pagina_resumen
                    ],drawer=drawer_principal,scroll=ft.ScrollMode.ADAPTIVE
                    )
            )
            page.update()
    
    def funcion_auxiliar_agregar(f):
        ingresar_o_modificar(f,aux=True)
        page.close(alerta_inquilino_ya)
        page.open(ft.SnackBar(ft.Text("Inquilino Modificado")))
        return
    

    
    def auxiliar_gastos(e):
        agregar_gasto(e,False)
        page.close(alerta_gastos)
        page.open(ft.SnackBar(ft.Text("Gasto Modificado")))
        return

    def cambio_de_pagina(e: ft.ControlEvent):
        page.views.clear()
        if e.data == "0" and page.route != "/main":
            page.go("/main")
        elif e.data == "1" and page.route != "/agregar_inquilinos":
            page.go("/agregar_inquilinos")
        elif e.data == "2" and page.route != "/agregar_gastos":
            page.go("/agregar_gastos")
        elif e.data == "4" and page.route != "/modificar":
            page.go("/modificar") 
        elif e.data == "3" and page.route != "/resumen":
            page.go("/resumen")
        return
    
    def ingresar_o_modificar(e : ft.OptionalControlEventCallable,aux = False):

        try:
            float(expensas.value)
            if (departamento.value not in inquilinos) or aux:
                inquilinos[departamento.value] = {
                "Inquilino":nombre_completo.value,
                "Expensas":expensas.value,
                "Tipo de pago":tipo_de_pago.value,
                "Pagó?":ya_pago.value
                }
                if departamento.value not in inquilinos:
                    page.open(ft.SnackBar(ft.Text("Inquilino Agregado")))
                departamento.value = ""
                nombre_completo.value = ""
                expensas.value = ""
                tipo_de_pago.value = ""
                ya_pago.value = ""
                page.update()
            else:
                page.open(alerta_inquilino_ya)

        except ValueError:
            page.open(alerta_expensas)
        
        tabla_principal.rows = dict_to_rows(inquilinos)
        tabla_principal.update()
        actualizar_listas()
        return
    

    def agregar_gasto(f,aux=True):
        try:
            float(gasto_monto.value)
            if gasto.value in gastos and aux:
                page.open(alerta_gastos)
            else:
                gastos[gasto.value]={
                    "Descripción":gasto_descripción.value,
                    "Monto":gasto_monto.value,
                    "Tipo de Cambio":tipo_de_pago.value,
                }
                gasto.value = ""
                gasto_descripción.value = ""
                gasto_monto.value = ""
                tipo_de_pago.value = ""
                page.update()
                page.open(ft.SnackBar(ft.Text("Gasto Agregado")))
        except ValueError:
            page.open(alerta_expensas)
        
        tabla_gastos.rows = dict_to_rows(gastos)
        tabla_gastos.update()
        actualizar_listas()
        return

    def eliminar(f:ft.OptionalControlEventCallable,diccionario : dict,value):
        def funcion_auxiliar_eliminar(f,diccionario,value):
            try:
                diccionario.pop(value)
                cerrar_alerta(f)
                tabla_gastos.rows = dict_to_rows(gastos)
                tabla_principal.rows = dict_to_rows(inquilinos)
                tabla_gastos.update()
                tabla_principal.update()
                lista_gastos.options = dict_to_list(gastos)
                lista_inquilinos.options = dict_to_list(inquilinos)
                lista_gastos.update()
                lista_inquilinos.update()
                page.update()
            except KeyError:
                page.open(ft.SnackBar(ft.Text("Seleccione otra opción")))
            return
        
        alerta_eliminar = ft.AlertDialog(
                    modal=True,
                    title="Eliminar",
                    content=ft.Text("¿Está seguro que desea eliminar?"),
                    actions=[ft.FilledButton("Eliminar",bgcolor="#E55934",
                                                on_click=lambda e:funcion_auxiliar_eliminar(f,diccionario,value)),
                            ft.Button("Cancelar",on_click=lambda g: page.close(alerta_eliminar))]
                    )
        
        def cerrar_alerta(f):
            page.close(alerta_eliminar)
            page.open(ft.SnackBar(ft.Text("Eliminado")))
            return
        page.open(alerta_eliminar)
        return
    #Componentes
    
    alerta_cerrar = ft.AlertDialog(title="Cerrar el Programa?",
                                   modal= True,
                                   actions=[
                                       ft.FilledButton("Cerrar",
                                                       on_click=lambda e: page.window.destroy()),
                                       ft.Button("Cancelar",
                                                 on_click=lambda e: page.close(alerta_cerrar))
                                   ])
    
    alerta_gastos = ft.AlertDialog(
                    title="Gasto ya en lista",
                    modal=True,
                    content=ft.Text("Elija un nombre distinto (plomero --> plomero 5A) \nO presione modificar para modificar"),
                    actions=[
                        ft.TextButton("Cancelar", on_click=lambda e: page.close(alerta_gastos)),
                        ft.FilledButton("Modificar",on_click=auxiliar_gastos)
                    ]
    )
    
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
                                ft.FilledButton("Modificar",color="#326C71",on_click=funcion_auxiliar_agregar),
                                ft.TextButton("Cancelar",on_click=lambda f: page.close(alerta_inquilino_ya)),
                            ],
                            actions_alignment=ft.MainAxisAlignment.END,
                        )
    
    
    
    tabla_principal = ft.DataTable([ft.DataColumn(ft.Text("Depto")),
                                    ft.DataColumn(ft.Text("Inquilino")),
                                    ft.DataColumn(ft.Text("Expensas")),
                                    ft.DataColumn(ft.Text("Moneda")),
                                    ft.DataColumn(ft.Text("Pagó?"))],
                                    rows = dict_to_rows(inquilinos),
                                    show_bottom_border=True,
                                    border = ft.border.all(3,"#326C71"),column_spacing=30
                                    )
    
    tabla_gastos = ft.DataTable([ft.DataColumn(ft.Text("Gasto")),
                                 ft.DataColumn(ft.Text("Descripción")),
                                 ft.DataColumn(ft.Text("Monto")),
                                 ft.DataColumn(ft.Text("Moneda"))],
                                 rows = dict_to_rows(gastos),
                                 show_bottom_border=True,
                                 border = ft.border.all(3,"#326C71"),column_spacing=30
                                 )
    
    departamento = ft.TextField(label="Departamento")
    
    nombre_completo = ft.TextField(label="Nombre Completo")      
    
    expensas = ft.TextField(label="Expensas",hint_text="Decimales con puntos y sin coma")
    
    tipo_de_pago = ft.Dropdown(value="Tipo de pago",options=tipos_de_pago_flet(tipos_de_pago),
                                            key=dropdown_changed,label="Moneda")

    ya_pago = ft.Dropdown(options=[ft.DropdownOption(text="Sí",key="Sí"),ft.DropdownOption(text="No",key="No")],label="Pagó?",
                          on_change=dropdown_changed)
    
    gasto = ft.TextField(label="Gasto")
    
    gasto_monto = ft.TextField(label="Monto",hint_text="Número sin comas y con puntos")
    
    gasto_descripción = ft.TextField(label="Descripción")
    
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
            ft.Divider(thickness=1,opacity=1),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.ADD_CHART_OUTLINED),
                label="Agregar/modificar Gastos",
                selected_icon=ft.Icons.ADD_CHART
            ),
                        ft.Divider(thickness=1,opacity=1),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.ANALYTICS_OUTLINED,
                label="Resumen",
                selected_icon=ft.Icons.ANALYTICS
            ),
            ft.Divider(thickness=1,opacity=1),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.MODE_OUTLINED),
                label="Quitar Gastos/expensas",
                selected_icon=ft.Icons.MODE
            )

        ]
    )

    lista_inquilinos = ft.Dropdown(
        label="Inquilinos",
        hint_text="Seleccione",
        options=dict_to_list(inquilinos),
        on_change=dropdown_changed,
        enable_search=True,
    )
    lista_gastos = ft.Dropdown(
        label= "Gastos",
        hint_text="Seleccione",
        options=dict_to_list(gastos),
        on_change=dropdown_changed,
        enable_search=True
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
              ft.Button("Agregar/modificar inquilino",color="#326C71",on_click=ingresar_o_modificar)
        ],alignment=ft.MainAxisAlignment.CENTER),
        tabla_principal]
        ,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    pagina_gastos = ft.Column(
        [ft.Row(
            [
                gasto,
                gasto_monto,
                gasto_descripción,
                tipo_de_pago,
                ft.Button("Agregar",on_click=agregar_gasto)
            ],ft.MainAxisAlignment.CENTER
        ),
         tabla_gastos
         ],horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    
    pagina_modificar=ft.Column([
                            ft.Column([
                                ft.Row([lista_inquilinos,
                                        ft.FilledButton("Borrar",bgcolor="#E55934",on_click=lambda e: eliminar(e,inquilinos,lista_inquilinos.value))]),
                                ft.Divider(color="#F5EFFF",thickness=2),
                                ft.Row([lista_gastos,
                                        ft.FilledButton("Borrar",bgcolor="#E55934",on_click=lambda e: eliminar(e,gastos,lista_gastos.value))]),  
                                ],alignment=ft.MainAxisAlignment.CENTER),
                            ft.Row([
                                tabla_principal,
                                tabla_gastos                                
                                ],alignment=ft.MainAxisAlignment.CENTER)   
                            ],horizontal_alignment=ft.CrossAxisAlignment.CENTER)


    
    
    pagina_resumen=ft.Row(
        [
            ft.Column([tabla_principal,
                       ft.Text(f"Expensas totales en pesos: {ganancias(inquilinos,gastos)[0][1]}"),
                       ft.Text(f"Expensas totales en dólares: {ganancias(inquilinos,gastos)[1][1]}"),
                       ft.Text(f"Expensas totales otros: {ganancias(inquilinos,gastos)[2][1]}")
                       ],horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            ft.Column([
                ft.Text("Ganancias del mes en pesos:"),
                ft.Text(f"{ganancias(inquilinos,gastos)[0][0]}"),
                ft.Text("Ganancias del mes en dolares:"),
                ft.Text(f"{ganancias(inquilinos,gastos)[1][0]}"),
                ft.Text("Ganancias del mes en dolares:"),
                ft.Text(f"{ganancias(inquilinos,gastos)[2][0]}")
            ],horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            ft.Column([
                tabla_gastos,
                ft.Text(f"Gastos totales en pesos: {ganancias(inquilinos,gastos)[0][2]}"),
                ft.Text(f"Gastos totales en dólares: {ganancias(inquilinos,gastos)[1][2]}"),
                ft.Text(f"Gastos totales otros: {ganancias(inquilinos,gastos)[2][2]}")
            ],horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            
        ],alignment=ft.MainAxisAlignment.CENTER
    )
    
    page.on_route_change = route_control
    page.go(page.route)
    



# guardar(inquilinos,gastos)





if __name__ == "__main__":
    ft.app(target= main,name="Consorciapp",assets_dir="assets")







