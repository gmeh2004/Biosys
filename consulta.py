import flet as ft
import Airtable as at
import principal as PR

def main(page: ft.Page):

    #configuración de la pagina
    page.title="Consultas"
    page.theme_mode="light"
    page.horizontal_alignment="center"
    page.appbar= ft.AppBar(
        title=ft.Text("lista de usuarios"),
        center_title=True,
        leading=ft.Icon("people"),
        bgcolor="blue",
        color="white"
    )
    
     #Tabla de usuario
    encabezado = [
        ft.DataColumn(ft.Text("Clave")),
        ft.DataColumn(ft.Text("Contraseña")),
        ft.DataColumn(ft.Text("Nombre Completo")),
        ft.DataColumn(ft.Text("¿Es administrador?")),
    ]
    filas = []
    datos = at.Usuario.all()
    for d in datos:
        celda1 = ft.DataCell(ft.Text(d.clave))
        celda2 = ft.DataCell(ft.Text(d.contra,color="white",selectable=True,show_selection_cursor=True))
        celda3 = ft.DataCell(ft.Text(d.nombre))
        celda4 = ft.DataCell(ft.Text(d.admin))
        fila = ft.DataRow([celda1,celda2,celda3,celda4])
        filas.append(fila)
    tbl_usuarios = ft.DataTable(encabezado,filas)
    
    def volver_menu(e: ft.ControlEvent):
        page.clean()
        PR.main(page)

    btn_volver = ft.FilledButton("Volver al menú", on_click=volver_menu)

    page.add(tbl_usuarios,btn_volver)
    page.update()

if __name__ == "__main__":
   ft.app(target=main,view=ft.AppView.WEB_BROWSER)

