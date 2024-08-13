import flet as ft

def main(page: ft.Page):
    page.title = "Administrador de tareas"
    page.window.width = 450
    page.window.height = 500

    def agregar_tarea(e):
        if nueva_tarea.value:
            tarea = ft.Row([
                ft.Checkbox(label=nueva_tarea.value),
                ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e, t=nueva_tarea.value: editar_tarea(e, t)),
                ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, tarea=None: eliminar_tarea(e, tarea))
            ])
            page.add(tarea)
            nueva_tarea.value = ""
            nueva_tarea.update()

    def editar_tarea(e, tarea):
        nueva_tarea.value = tarea
        page.controls.remove(e.control.parent)
        page.update()

    def eliminar_tarea(e, tarea):
        page.controls.remove(e.control.parent)
        page.update()

    nueva_tarea = ft.TextField(hint_text="Ingrese su tarea", width=300)
    page.add(ft.Row([nueva_tarea, ft.ElevatedButton("Añadir", on_click=agregar_tarea)]))

ft.app(target=main)
