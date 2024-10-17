import flet as ft

class consultor_page(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/consultor",padding=10)

        
        def definir_caixas(e):
            if c1.value:
                ...




        c1 = ft.Checkbox(label='Ano e idade',label_style=ft.TextStyle(color=ft.colors.BLACK,weight='w600'),active_color='#0464f6', value=False,)
        c2 = ft.Checkbox(label='Bop',label_style=ft.TextStyle(color=ft.colors.BLACK,weight='w600'),active_color='#0464f6', value=False)


        self.page = page

        body = ft.Container(
            #bgcolor='#1e2428',
            expand=True,
            height=page.height,
            width=page.width,
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Row([ft.Icon(ft.icons.SEARCH, color='transparent'),ft.Text('Consultor',color='#0464f6',weight='w500',size=20),ft.Icon(ft.icons.SEARCH,color='#0464f6')],ft.MainAxisAlignment.CENTER),
                    ft.Row([c1,c2],ft.MainAxisAlignment.CENTER),
                ]
            )
        )



        self.controls = [
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    controls=[body],
                )
            )
        ]
