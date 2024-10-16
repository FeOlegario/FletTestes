from connection.bases import *
import flet as ft


def main(page: ft.Page):
    page.title = "Ágora"
    page.theme_mode = "light"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.min_height = 537
    page.window.min_width = 703
    page.window.height = 537
    page.window.width = 703
    page.bgcolor = "#ffffff"
    page.update()

    def nova_rota(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar( title=ft.Text("ScriptHub"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("visite o quantum", on_click=lambda _: page.go("/quantum"))
                ]
            )
        )

        if page.route == "/quantum":
            page.views.append(
                ft.View(
                    "/quantum",
                    [
                        ft.AppBar(title=ft.Text("ScriptHub"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Voltar", on_click=lambda _: page.go("/"))
                    ]
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    


    page.on_route_change = nova_rota
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)