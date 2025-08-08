
import flet as ft
import consulta as CS
import alta_usuario as AU
import Registro_de_bioenergías as IRD  
import main as CE
import consultarbio as CB

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

    def mostrar_consultasBio(e: ft.ControlEvent):
        page.clean()
        CB.main(page)
    #Componentes de la pagina
    page.appbar = ft.AppBar (
        title= ft.Text ("Sistema de Gestión de Bionergías",font_family="Kanit",size=30),
        center_title=True,
        leading= ft.Icon ("ENERGY_SAVINGS_LEAF"),
        color = "black",
        bgcolor= ft.Colors.LIGHT_GREEN_500,
    )
    
    btn_alta = ft.ElevatedButton ("Registro de usuarios (altas)", on_click=mostrar_altaUsu,bgcolor=ft.Colors.GREEN_900,color="white")
    btn_registro = ft.ElevatedButton ("Registro de bioenergias", on_click =mostrar_registrodatos,bgcolor=ft.Colors.GREEN_900,color="white" )
    btn_consulta = ft.ElevatedButton ("Consulta de usuarios", on_click=mostrar_consultasUsu,bgcolor=ft.Colors.GREEN_900,color="white")
    btn_consultabio = ft.ElevatedButton ("Consulta de bioenergias", on_click =mostrar_consultasBio,bgcolor=ft.Colors.GREEN_900,color="white")
    
    btn_cerrar = ft.ElevatedButton ("Cerrar sesión", on_click=mostrar_loginCer,bgcolor=ft.Colors.GREEN_900,color="white")
    

   # Imagen GIF a la izquierda
    gif = ft.Image(
        src="https://raw.githubusercontent.com/gmeh2004/Biosys/main/energ-a-de-biomasa-unscreen.gif",
        width=350,
        height=350,
        fit=ft.ImageFit.CONTAIN
    )
    botones_columna = ft.Column(
        controls=[btn_alta, btn_registro, btn_consulta, btn_consultabio, btn_cerrar],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        
    )
   
    contenedor_botones = ft.Container(
        content=botones_columna,
        padding=ft.Padding(left=10, top=-210, right=0, bottom=0),  # mueve arriba e izquierda
    )

    contenedor_gif = ft.Container(
        content=gif,
        padding=ft.Padding(left=-500, top=-100, right=0, bottom=0),  # mueve arriba e izquierda
    )


    fila_principal = ft.Row(
        controls=[contenedor_gif,contenedor_botones],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=0,
        expand=True,
    )


# Agregas esa fila a la página
    page.add(fila_principal)


    page.update() 

if __name__ == "__main__":
    ft.app(target=main,view=ft.AppView.WEB_BROWSER)
