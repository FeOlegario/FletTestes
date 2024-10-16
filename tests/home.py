import flet as ft


class HomePage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/home",padding=60)

        self.page = page

        self.quantum = ft.Row(
            [
                ft.Container(
                    content=ft.Image(src=f"/quantum_png.png"),
                    alignment=ft.alignment.center,
                    height=150,
                    on_click=lambda e: print('click'),
                    ink=True,
                    rtl=True,
                    ),

                ft.Stack(
                    [
                        ft.Column(
                            [
                                ft.Container(
                                    content=ft.Image(src=f"/Lupa.png",fit=ft.ImageFit.SCALE_DOWN),
                                    height=150,
                                    alignment=ft.alignment.center,
                                    ink=True,
                                    on_click=lambda e: print('oi')
                                ),
                                ft.Text("Consultor")
                            ], horizontal_alignment="center"
                        ),
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )











        self.teste = ft.Container(
            ft.Stack(
                [
                    ft.Column(
                        [
                            ft.Image(src=f"/Lupa.png",height=80),
                            ft.Container(content=ft.Text('Consultor')),
                        ],horizontal_alignment="center"
                    )
                ]
            ),bgcolor=ft.colors.AMBER, padding=3
        )





        self.controls = [
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    controls=[self.quantum],
                    horizontal_alignment="center",
                )
            )
        ]