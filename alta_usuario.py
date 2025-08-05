import flet as ft
import principal as PR
import Airtable as at

def main(page: ft.Page):
     #Funcion que hara el proceso de guardar al usuario
    def guardar_usuario(e: ft.ControlEvent):
        clave = txt_clave.value
        contra = txt_contra.value
        contra2 = txt_contra2.value
        nombre = txt_nombre.value
        #Validar campos
        if clave == "":
            snackbar = ft.SnackBar (ft.Text("Introduce tu clave de usuario"), bgcolor="red", show_close_icon=True)
            page.open(snackbar)
            return
        elif contra == "":
            snackbar = ft.SnackBar (ft.Text("Introduce la contraseña"), bgcolor="red", show_close_icon=True)
            page.open(snackbar)
        elif contra2 == "":
            snackbar = ft.SnackBar (ft.Text("Confirma la contraseña"), bgcolor="red", show_close_icon=True)
            page.open(snackbar)
        elif nombre == "":
            snackbar = ft.SnackBar (ft.Text("Introduce tu nombre"), bgcolor="red", show_close_icon=True)
            page.open(snackbar)
        #Confirmar contraseña
        if contra != contra2:
            snackbar = ft.SnackBar (ft.Text("Las contraseñas no coinciden"), bgcolor="red", show_close_icon=True)
            page.open(snackbar)
            return
        #Guardar usuario en la nube
        nuevo = at.Usuario(
            clave = clave,
            contra = contra,
            nombre = nombre,
            admin = int(chk_admin.value)
        )
        try:
            nuevo.save()
            snackbar = ft.SnackBar (ft.Text("Usuario registrado"), bgcolor="green", show_close_icon=True)
            page.open(snackbar)
        except Exception:
            snackbar = ft.SnackBar (ft.Text(error), bgcolor="red", show_close_icon=True)
            page.open(snackbar)
    
    def cancelar_formulario(e: ft.ControlEvent):
        txt_clave.value = ""
        txt_contra.value = ""
        txt_contra2.value = ""
        txt_nombre.value = ""
        chk_admin.value = False
        page.update()

    #Confuguracion de la pagina
    page.title="Altas"
    page.theme_mode="light"
    page.window.width=800
    page.window.height=600
    page.appbar=ft.AppBar(
        title=ft.Text("Nuevo usuario"),
        center_title=True,
        leading=ft.Icon("person_add"),
        color="white",
        bgcolor="purple"
    )
    #Componentes de la pagina
    txt_clave=ft.TextField(label="Clave del usuario")
    txt_contra=ft.TextField(label="Contraseña",password=True)
    txt_contra2=ft.TextField(label="Confirmar contraseña",password=True)
    txt_nombre=ft.TextField(label="Nombre completo")
    chk_admin=ft.Checkbox(label="¿Es administrador?")
    bnt_guardar=ft.FilledButton(
        text="Guardar",
        icon=("save"),
        on_click= guardar_usuario
    )

    btn_cancelar=ft.FilledButton(
        text="Cancelar",
        icon="cancel",
        on_click=cancelar_formulario
    )

    def volver_menu(e: ft.ControlEvent):
        page.clean()
        PR.main(page)

    btn_volver = ft.FilledButton("Volver al menú", on_click=volver_menu)

    fila=ft.Row(controls=[bnt_guardar,btn_cancelar,btn_volver])

    
    #Añadir componentes a la página
    page.add(txt_clave,txt_contra,txt_contra2,txt_nombre,chk_admin,fila)

    page.update()

if __name__ == "__main__":
  ft.app(target=main,view=ft.AppView.WEB_BROWSER)

