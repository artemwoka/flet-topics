import flet as ft


def main(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()
    
    new_task = ft.TextField(hint_text= "Що потрібно зробити?", expand = True)
    tasks_view = ft.Column()
    cointainer = ft.Column(
        width = 600,
        controls = [
            ft.Row(
                controls = [
                    new_task,
                    ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked)
                ]
            ),
            tasks_view,
        ],
    )

    page.horizontal_aligment = ft.CrossAxisAlignment.CENTER
    page.add(cointainer)
    page.window.width = 600
    page.update()

ft.run(main)
