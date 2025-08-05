import flet as ft
import Airtable as at
import principal as PR

def main(page: ft.Page):
    # Definición de campos globales para poder usarlos en el guardado
    cultivo_dropdown = ft.Dropdown(
        on_change=lambda e: page.update(),
        options=[
            ft.dropdown.Option("Caña de Azúcar"),
            ft.dropdown.Option("Cacao"),
            ft.dropdown.Option("Maíz"),
            ft.dropdown.Option("Coco"),
            ft.dropdown.Option("Plátano"),
        ],
        width=180,
    )

    parte_dropdown = ft.Dropdown(
        on_change=lambda e: page.update(),
        options=[
            ft.dropdown.Option("Hoja"),
            ft.dropdown.Option("Tallo"),
            ft.dropdown.Option("Cáscara"),
            ft.dropdown.Option("Bagazo"),
            ft.dropdown.Option("Rastrojo"),
        ],
        width=180,
    )

    cantidad_field = ft.TextField(width=100)
    area_field = ft.TextField(width=100)
    energia_field = ft.TextField(width=100)
    municipio_dropdown = ft.Dropdown(
        on_change=lambda e: page.update(),
        options=[
            ft.dropdown.Option("Balancán"),
            ft.dropdown.Option("Cárdenas"),
            ft.dropdown.Option("Centla"),
            ft.dropdown.Option("Centro"),
            ft.dropdown.Option("Comalcalco"),
            ft.dropdown.Option("Cunduacán"),
            ft.dropdown.Option("Emiliano Zapata"),
            ft.dropdown.Option("Huimanguillo"),
            ft.dropdown.Option("Jalapa"),
            ft.dropdown.Option("Jalpa de Méndez"),
            ft.dropdown.Option("Jonuta"),
            ft.dropdown.Option("Macuspana"),
            ft.dropdown.Option("Nacajuca"),
            ft.dropdown.Option("Paraíso"),
            ft.dropdown.Option("Tacotalpa"),
            ft.dropdown.Option("Teapa"),
            ft.dropdown.Option("Tenosique"),
        ],
        width=180,
    )
    latitud_field = ft.TextField(width=100)
    longitud_field = ft.TextField(width=100)

    def guardar_bioenergia(e: ft.ControlEvent):
        try:
            nuevo = at.Bioenergia(
                cultivo=cultivo_dropdown.value,
                parte=parte_dropdown.value,
                cantidad=float(cantidad_field.value),
                area=float(area_field.value),
                energia=float(energia_field.value),
                municipio=municipio_dropdown.value,
                latitud=float(latitud_field.value),
                longitud=float(longitud_field.value)
            )
            nuevo.save()
            snackbar = ft.SnackBar (ft.Text("Datos guardados exitosamente"), bgcolor="green", show_close_icon=True)
            page.open(snackbar)
            
        except Exception as error:
            snackbar = ft.SnackBar (ft.Text(error), bgcolor="red", show_close_icon=True)
            page.open(snackbar)

    # App bar
    page.appbar = ft.AppBar(
        title=ft.Text("Biomasa", size=30, weight=ft.FontWeight.BOLD),
        center_title=True,
        bgcolor="#66FF99",
        automatically_imply_leading=False,
    )

    # ---------- COLUMNA IZQUIERDA ----------
    col_izquierda = ft.Column(
        controls=[
            ft.Text("Cultivo Origen", size=20, weight=ft.FontWeight.BOLD),
            cultivo_dropdown,
            ft.Text("Parte Aprovechada", size=20, weight=ft.FontWeight.BOLD),
            parte_dropdown,
            ft.Row(
                controls=[
                    ft.Text("Cantidad (ton)", size=20, weight=ft.FontWeight.BOLD),
                    cantidad_field,
                ],
                spacing=80
            ),
            ft.Row(
                controls=[
                    ft.Text("Área cultivada", size=20, weight=ft.FontWeight.BOLD),
                    area_field,
                ],
                spacing=80
            ),
            ft.Row(
                controls=[
                    ft.Text("Contenido energético", size=20, weight=ft.FontWeight.BOLD),
                    energia_field,
                ],
                spacing=10
            ),
        ],
        spacing=20,
        width=350
    )

    # ---------- COLUMNA DERECHA ----------
    col_derecha = ft.Column(
        controls=[
            ft.Text("Municipio", size=20, weight=ft.FontWeight.BOLD),
            municipio_dropdown,
            ft.Text("Coordenadas", size=20, weight=ft.FontWeight.BOLD),
            ft.Row(
                controls=[
                    ft.Text("Latitud", size=20),
                    latitud_field,
                ],
                spacing=30
            ),
            ft.Row(
                controls=[
                    ft.Text("Longitud", size=20),
                    longitud_field,
                ],
                spacing=10
            ),
            ft.Container(
                content=ft.FilledButton(
                    text="Guardar",
                    width=150,
                    color="black",
                    bgcolor="green",
                    on_click=guardar_bioenergia
                ),
                padding=ft.padding.only(left=30, top=20)
            )
        ],
        spacing=30,
        width=350
    )

    def volver_menu(e: ft.ControlEvent):
        page.clean()
        PR.main(page)

    btn_volver = ft.FilledButton("Volver al menú", on_click=volver_menu)

    # ---------- LAYOUT FINAL ----------
    layout = ft.Row(
        controls=[col_izquierda, col_derecha],
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.START,
        spacing=150
    )

    contenido_principal = ft.Column(
        controls=[
            ft.Container(content=layout, padding=ft.Padding(left=280, top=20, right=0, bottom=0)),
            ft.Container(content=btn_volver, padding=ft.padding.only(top=10, right=50), alignment=ft.alignment.top_right)
        ]
    )

    page.add(contenido_principal)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
