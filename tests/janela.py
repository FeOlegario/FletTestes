import flet as ft
import pandas as pd

# Função que cria o diálogo com a tabela
def abrir_dialogo_com_tabela(e, page):
    # Definindo a tabela com cabeçalhos e algumas linhas de exemplo


    df = pd.read_excel('otarios.xlsx')
    coluna_data = 'DT ANIVERSARIO'# Substitua com o nome real da coluna
    df[coluna_data] = pd.to_datetime(df[coluna_data], dayfirst=True).dt.strftime('%d/%m/%Y')
    colunas = [ft.DataColumn(ft.Text("Selecionar"))] + [ft.DataColumn(ft.Text(col)) for col in df.columns]
    linhas = [
            ft.DataRow(cells=[
                ft.DataCell(ft.Checkbox()),  # Adiciona a caixinha de seleção
                ft.DataCell(ft.Text(str(row[0]))),
                ft.DataCell(ft.Text(str(row[1]))),
                ft.DataCell(ft.Text(str(row[2]))),
                ft.DataCell(ft.Text(str(row[3]))),  # Adiciona a quarta coluna
                ft.DataCell(ft.Text(str(row[4]))),  # Adiciona a quarta coluna
                ft.DataCell(ft.Text(str(row[5]))),  # Adiciona a quarta coluna
                ft.DataCell(ft.Text(str(row[6]))),  # Adiciona a quarta coluna
            ])
            for index, row in df.iterrows()
        ]

    tabela = ft.DataTable(columns=colunas, rows=linhas,show_bottom_border=True)

    cv = ft.Column([tabela],scroll=ft.ScrollMode.ADAPTIVE,)
    vc = ft.Row([cv],scroll=ft.ScrollMode.ALWAYS,on_scroll_interval=0)

    # Criando o diálogo e adicionando a tabela nele
    dialogo = ft.AlertDialog(
        title=ft.Text("Tabela de Dados"),
        content=vc,
        adaptive=True,
        actions=[ft.TextButton("Fechar", on_click=lambda e: page.close(dialogo))],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # Exibindo o diálogo
    page.dialog = dialogo
    dialogo.open = True
    page.update()

# Função principal para a interface inicial
def main(page):
    # Definindo o botão que abre o diálogo com a tabela
    botao = ft.ElevatedButton("Abrir Tabela", on_click=lambda e: abrir_dialogo_com_tabela(e, page))
    page.add(botao)

# Rodando o app principal no contexto correto
if __name__ == "__main__":
    ft.app(target=main)
