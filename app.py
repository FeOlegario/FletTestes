# import flet as ft
from apps.home.home import *
from apps.consultor.consultor_page import *

def main(page: ft.Page):
    page.title = 'ScriptHub'
    page.theme_mode = "light"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.min_height = 537
    page.window.min_width = 703
    page.window.height = 537
    page.window.width = 703
    page.window.maximizable = False
    page.window_resizable = True 
    page.bgcolor = "#ffffff"
    page.update()


    def router(route):
        page.views.clear()

        if page.route == "/consultor":
            consultor = consultor_page(page)
            page.title='Consultor'
            page.views.append(consultor)

        if page.route == "/home":
            home = HomePage(page)
            page.title='ScriptHub'
            page.views.append(home)

        page.update()

    page.on_route_change = router
    page.go("/consultor")


ft.app(target=main, assets_dir="assets")