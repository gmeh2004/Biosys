
import flet as ft
import Airtable as at
import principal as PR  

def main(page: ft.Page):

    def validar_usuario(e: ft.ControlEvent):
        usuario = txt_usuario.value
        contra = txt_contra.value
        snackbar = ft.SnackBar(content=None, bgcolor="red", show_close_icon=True)

        if usuario == "":
            snackbar.content = ft.Text("Introduce tu usuario")
            page.open(snackbar)
            return
        elif contra == "":
            snackbar.content = ft.Text("Introduce tu contraseña")
            page.open(snackbar)
            return

        # Obtener todos los usuarios desde Airtable
        usuarios = at.Usuario.all()

        # Buscar si existe un usuario con esas credenciales
        usuario_encontrado = next(
            (u for u in usuarios if u.clave == usuario and u.contra == contra), None
        )

        if usuario_encontrado is None:
            snackbar.content = ft.Text("Credenciales incorrectas")
            page.open(snackbar)
        else:
            page.clean()
            PR.main(page)
            # Puedes mostrar mensaje de bienvenida si quieres:
            # snackbar.content = ft.Text(f"Bienvenid@: {usuario_encontrado.nombre}")
            # page.open(snackbar)

    # Configuración de la página
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.title = "Inicio de sesión"
    page.window.width = 800
    page.window.height = 600
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
    }

    # Componentes visuales
    logo = ft.Icon("person", size=60, color=ft.Colors.GREEN_500)

    page.appbar = ft.AppBar(
        title=ft.Text("Bienvenid@", font_family="Kanit"),
        center_title=True,
        leading=ft.Icon("person_add"),
        color="black",
        bgcolor=ft.Colors.LIGHT_GREEN_500,
    )

    txt_usuario = ft.TextField(label="Username/Correo", width=250)
    txt_contra = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=250)

    btn_login = ft.FilledButton(
        "Iniciar sesión",
        icon=ft.Icons.LOGIN,
        width=300,
        color="white",
        bgcolor=ft.Colors.GREEN_500,
        on_click=validar_usuario,
        
    )


    # Agregar componentes a la página
    page.add(logo, txt_usuario, txt_contra, btn_login)
    page.update()

# Inicializar la aplicación
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
