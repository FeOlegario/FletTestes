import flet as ft


class HomePage(ft.View):



    def __init__(self, page: ft.Page):
        super().__init__(route="/home",padding=60)

        self.consultor = ft.Container(
            border_radius=8,
            padding=3,
            bgcolor='#f8f9ff',
            shadow=ft.BoxShadow(blur_radius=3, color=ft.colors.with_opacity(opacity=0.2,color='black'),offset=(0,1)),
            width=120,
            height=120,
            ink=True,
            on_click=lambda e: page.go("/consultor"),
            content= ft.Column(
                spacing=2,
                controls=[
                    ft.Row([ft.Image(src=f"apps/assets/Lupa.png", width=70, height=90)],ft.MainAxisAlignment.CENTER),
                    ft.Row([ft.Text('Consultor', size=18,text_align=ft.TextAlign.RIGHT,weight='w500')],ft.MainAxisAlignment.CENTER)
                ]
            )
        )

        self.quantum = ft.Container(
            border_radius=8,
            padding=3,
            bgcolor='#f8f9ff',
            shadow=ft.BoxShadow(blur_radius=3, color=ft.colors.with_opacity(opacity=0.2,color='black'),offset=(0,1)),
            width=120,
            height=120,
            ink=True,
            on_click=lambda e: page.go("/qauntum"),
            content= ft.Column(
                spacing=2,
                controls=[
                    ft.Row([ft.Image(src=f"apps/assets/Quantum.png", width=90, height=90)],ft.MainAxisAlignment.CENTER),
                    ft.Row([ft.Text('Quantum', size=18,text_align=ft.TextAlign.RIGHT,weight='w500')],ft.MainAxisAlignment.CENTER)
                ]
            )
        )

        self.testt = ft.Container(
            border_radius=8,
            bgcolor="#43b2de",
            width=250,
            height=120,
            
        )


        self.page = page

        self.centro = ft.Container(
            content=ft.Column(
                [
                    ft.Row([self.consultor, self.quantum],ft.MainAxisAlignment.CENTER,ft.CrossAxisAlignment.CENTER),
                    self.testt
                ], ft.MainAxisAlignment.CENTER, ft.CrossAxisAlignment.CENTER
            )
        )

        self.controls = [
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    controls=[self.centro],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        ]