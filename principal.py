
import flet as ft
import consulta as CS
import alta_usuario as AU
import Registro_de_bioenergías as IRD  # <--- este es el archivo que te faltaba importar
import main as CE

def main (page: ft.Page):
    #Configuración de la pagina
    page.theme_mode = "light" 
    page.horizontal_alignment = "center" 
    page.title = "Menú Principal" 
    page.window.width = 800 
    page.window.height = 600 
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
    }
    #Funciones para abrir las otras paginas
    def mostrar_registrodatos(e: ft.ControlEvent):
        page.clean()
        IRD.main(page)
    def mostrar_consultasUsu (e: ft.ControlEvent):
        page.clean()
        CS.main(page)
    def mostrar_altaUsu(e: ft.ControlEvent):
        page.clean()
        AU.main(page)
    def mostrar_loginCer(e: ft.ControlEvent):
        page.clean()
        CE.main(page)
    #Componentes de la pagina
    page.appbar = ft.AppBar (
        title= ft.Text ("Sistema de Gestión de Bionergías",font_family="Kanit",size=30),
        center_title=True,
        leading= ft.Icon ("ENERGY_SAVINGS_LEAF"),
        color = "black",
        bgcolor= ft.Colors.RED_100,
    )

    
    btn_registro = ft.ElevatedButton ("Registro de bioenergias", on_click =mostrar_registrodatos )
    btn_consulta = ft.ElevatedButton ("Consulta de usuarios", on_click=mostrar_consultasUsu)
    btn_alta = ft.ElevatedButton ("Registro de usuarios (altas)", on_click=mostrar_altaUsu)
    btn_cerrar = ft.ElevatedButton ("Cerrar sesión", on_click=mostrar_loginCer)

    #Añadir a la pagina y actualizar
    page.add(btn_registro,btn_consulta,btn_alta,btn_cerrar) 
    page.update() 

if __name__ == "__main__":
    ft.app(target=main,view=ft.AppView.WEB_BROWSER)


