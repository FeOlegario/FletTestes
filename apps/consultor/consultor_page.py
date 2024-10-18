# import flet as ft
from apps.consultor.consultor_app import *




class consultor_page(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/consultor",padding=10)


        def carregamento(visible: bool):
            carregando.visible = visible
            page.update()


        def pesquisar(e):
            carregamento(True)

            vitima_valor = vitima.value
            ano_valor = ano.value
            bop_valor = bop.value

            ps= ''

            if not c1.value and not c2.value:
                aviso('Selecione uma opção e preencha os campos.',color='#ff8800')
                carregamento(False)
                return None


            if c1.value:
                if vitima_valor == '' or ano_valor == '':
                    carregamento(False)
                    aviso('Preencha todos os campos.',color='red')
                    page.update()

                    return None
                
                elif not ano_valor.isdigit() or len(ano_valor) > 4 or len(ano_valor) < 4:
                    return print('Ano inválido.')
                
                vitima_valor = ' '.join(vitima_valor.split())
                vitima_valor= vitima_valor.upper()
                ano_valor = ano_valor.strip()
                ps = consultar(vitima_valor, ano_valor,bop_valor)


                carregamento(False)
                aviso('Concluido!',color='#1bc22f')
                page.update()
                return None
            
            if c2.value:
                if not bop_valor:
                    return print('Insira um BOP.')
                
                bop_valor = bop_valor.strip()
                ps = consultar(vitima_valor, ano_valor,bop_valor)
                carregamento(False)
                aviso('Concluido!',color='#1bc22f')
                page.update()

                return None



        def aviso(message, color=""):
            if color == "red":
                alerta = ft.AlertDialog(
                    title=ft.Text(
                        "Erro", 
                        color='#FFFFFF',
                        font_family='inter'),
                    content=ft.Text(
                        message,
                        size=15,
                        font_family='inter',
                        color='#FFFFFF',),
                    actions=[ft.TextButton(
                        "OK", 
                        on_click=lambda e: page.close(alerta),
                        style=ft.ButtonStyle(
                            color='#0064FF',
                            bgcolor={
                                    ft.ControlState.DEFAULT: "#FFFFFF",
                                    ft.ControlState.FOCUSED: "#5caee0",
                                    ft.ControlState.PRESSED: "#4990e2",
                                    ft.ControlState.DISABLED: "#cccccc"
                                }
                        ))
                        ],
                    bgcolor= '#EB2939'
                )
                page.open(alerta)
            else:
                page.snack_bar = ft.SnackBar(
                    ft.Text(message, color='#FFFFFF',weight='bold'),
                    bgcolor=color,
                    open=True,
                )

        def ano_vitma(e):
            if c1.value:
                ano.visible = True
                vitima.visible = True
                bop.visible = False
                bop.value = None
                c2.value= False
            else:
                ano.visible = False
                vitima.visible = False
                ano.value = None
                vitima.value = None
            page.update()

        def bop_status(e):
            if c2.value:
                bop.visible = True     
                ano.visible = False
                vitima.visible = False
                c1.value=False
                ano.value = None
                vitima.value = None
            else:
                bop.visible = False
                bop.value = None
            page.update()





        estilo_bt=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=2),
            bgcolor={
                ft.ControlState.DEFAULT: "#0464f6",
                ft.ControlState.FOCUSED: "#5caee0",
                ft.ControlState.PRESSED: "#4990e2",
                ft.ControlState.DISABLED: "#cccccc"
            },
            color={
                ft.ControlState.DEFAULT: ft.colors.WHITE,
                ft.ControlState.PRESSED: ft.colors.WHITE60,
            },
            elevation={
                ft.ControlState.DEFAULT: 3,
                ft.ControlState.HOVERED: 5,
            },
            padding=15,
            text_style={
                ft.ControlState.DEFAULT: ft.TextStyle(
                    size=15,
                    weight="w500"
                )
            },
            
        )


# print(f'"{bop.value}","{ano.value}","{vitima.value}"')



        carregando = ft.ProgressRing(
            visible=False,
            color='#0064FF'
        )

        btn_pesquisar = ft.ElevatedButton('Pesquisar', on_click=pesquisar, width=200, style=estilo_bt)

        app_bar= ft.TextButton(content=ft.Row([ft.Icon(name=ft.icons.ARROW_BACK_IOS_NEW, color='#0464f6'),ft.Text('Voltar',color='#0464f6')]), width=100, on_click=lambda e: page.go("/home"))

        c1 = ft.Checkbox(label='Ano e Nome da vítima',label_style=ft.TextStyle(color=ft.colors.BLACK,weight='w600'),active_color='#0464f6', value=False,on_change=ano_vitma)
        c2 = ft.Checkbox(label='BOP',label_style=ft.TextStyle(color=ft.colors.BLACK,weight='w600'),active_color='#0464f6', value=False,on_change=bop_status)


        ano = ft.TextField(label='Ano do fato',width=200,visible=False,)
        vitima = ft.TextField(label='Nome da vítima',width=200,multiline=True,max_lines=2,visible=False)
        bop = ft.TextField(label='Numero do BOP',width=200,multiline=True,max_lines=2,visible=False)
        


        self.page = page

        body = ft.Container(
            # bgcolor='#1e2428',
            expand=True,
            height=page.height,
            width=page.width,
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Row([ft.Icon(ft.icons.SEARCH, color='transparent'),ft.Text('Consultor',color='#0464f6',weight='w500',size=20),ft.Icon(ft.icons.SEARCH,color='#0464f6')],ft.MainAxisAlignment.CENTER),
                    # ft.Divider(height=20, color="transparent"),
                    ft.Row([c1,c2],ft.MainAxisAlignment.CENTER),
                    ft.Row([bop,ano,vitima],ft.MainAxisAlignment.CENTER),
                    ft.Row([btn_pesquisar],ft.MainAxisAlignment.CENTER),
                    ft.Row([carregando],ft.MainAxisAlignment.CENTER),

                ]
            )
        )



        self.controls = [
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    controls=[app_bar,body],spacing=0
                )
            )
        ]
