import flet as ft
import Airtable as at
import principal as PR


def main(page: ft.Page):

    # Configuración de la página
    page.title = "Consulta usuarios"
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.scroll = "auto"

    page.appbar = ft.AppBar(
        title=ft.Text("Lista de usuarios",font_family="Kanit",size=20),
        center_title=True,
        leading=ft.Icon("people"),
        bgcolor=ft.Colors.LIGHT_GREEN_500,
        color="black"
    )

    # Obtener los datos
    datos = at.Usuario.all()

    # Lista que contiene encabezado + filas como Rows
    lista_de_filas = [
        ft.Row([
            ft.Text("Clave", weight="bold",color=ft.Colors.GREEN_800, width=100,text_align="center"),
            ft.Text("Contraseña", weight="bold",color=ft.Colors.GREEN_800, width=100,text_align="center"),
            ft.Text("Nombre Completo", weight="bold",color=ft.Colors.GREEN_800, width=100,text_align="center"),
            ft.Text("¿Es administrador?", weight="bold",color=ft.Colors.GREEN_800, width=100,text_align="center")
           
        ],
        alignment=ft.MainAxisAlignment.CENTER

        )
    ]

    for d in datos:
        lista_de_filas.append(
            ft.Row([
                ft.Text(d.clave, width=100,text_align="center"),
                ft.Text(d.contra,color="white",selectable=True,show_selection_cursor=True, width=100,text_align="center"),
                ft.Text(d.nombre, width=100,text_align="center"),
                ft.Text(d.admin, width=100,text_align="center")
                
            ],
            alignment=ft.MainAxisAlignment.CENTER
            )
        
        )

    # Contenedor con scroll vertical real
    tabla_scroll = ft.Container(
        content=ft.ListView(
            controls=lista_de_filas,
            expand=True,
           
        ),
        height=400,  # Altura que activa el scroll
        width=1000,
        bgcolor="white",
        padding=10,
        border_radius=10,
        alignment=ft.alignment.center
    )

    # Botón de volver al menú
    def volver_menu(e):
        page.scroll = None
        page.horizontal_alignment = None
        page.theme_mode = "light"
        page.appbar = None
        page.clean()
        PR.main(page)

       

    btn_volver = ft.FilledButton("Volver al menú", on_click=volver_menu,bgcolor=ft.Colors.GREEN_900,color="white")

    # Layout principal con scroll
    layout_scroll = ft.Column(
        controls=[
            tabla_scroll,
            ft.Container(height=20),
            btn_volver
        ],
        scroll="auto",
        expand=True,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER  # <--- CENTRADO
    )

    page.add(layout_scroll)
    page.update()

# Ejecutar app
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
