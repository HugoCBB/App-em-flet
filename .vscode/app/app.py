'''
Como vai funcionar a logica?
1 - Importar a biblioteca Flet
2 - Definir a funçao em que a calculadora ira rodar nesse caso a função main
3 - Fazer as funcoes basicas de soma, subtração, multiplicação, divisão e C (Delete)
4 - Adicionar os numeros de 0 a 9
5 - Adicionar um output em que ira sair o resultado da aplicaçao
6 - Ser feliz
'''
import flet as ft
def main(page: ft.Page):
    page.bgcolor = '#484d50'


    def clear(e):
        resultado.value = 0
        page.update()
            
    def soma(e):
        pass
    def subtracao(e):
        pass
    def multiplicacao(e):
        pass
    def divisao(e):
        pass

    page.add(
        
    )

    resultado = ft.Text(value= '3')
    page.add(
        ft.Row(controls=[
            resultado,
        ])
    )
    page.add(
        ft.Row(controls=[
            ft.ElevatedButton(text= 'AC',color= 'Red', expand= 1, on_click= clear),
            ft.ElevatedButton(text= '+/-', color= 'Black', expand= 1),
            ft.ElevatedButton(text= '%', color= 'Black', expand= 1),
            ft.ElevatedButton(text= '/', color= 'Black', expand= 1, on_click= divisao),
        ])
    )
    page.add(
        ft.Row(controls=[
            ft.ElevatedButton(text= ' 7 ', color= 'Black', expand= 1),
            ft.ElevatedButton(text= ' 8 ', color= 'Black', expand= 1),
            ft.ElevatedButton(text= ' 9 ', color= 'Black', expand= 1),
            ft.ElevatedButton(text= ' * ', color= 'Black', expand= 1, on_click= multiplicacao),
        ])
    )
    page.add(
        ft.Row(controls=[
            ft.ElevatedButton(text= ' 4 ', color= 'Black', expand= 1),
            ft.ElevatedButton(text= ' 5 ', color= 'Black', expand= 1),
            ft.ElevatedButton(text= ' 6 ', color= 'Black', expand= 1),
            ft.ElevatedButton(text= ' - ', color= 'Black', expand= 1, on_click= subtracao),
        ])
    )
    page.add(
        ft.Row(controls=[
            ft.ElevatedButton(text= ' 1 ', color= 'Black', expand= 1),
            ft.ElevatedButton(text= ' 2 ', color= 'Black', expand= 1),
            ft.ElevatedButton(text= ' 3 ', color= 'Black', expand= 1),
            ft.ElevatedButton(text= ' + ', color= 'Black', expand= 1, on_click= soma),
        ])
    )
    page.add(
        ft.Row(controls=[
            ft.ElevatedButton(text= ' 0 ', color= 'Black', expand= 1),
            ft.ElevatedButton(text= ' . ', color= 'Black', expand= 1),
            ft.ElevatedButton(text= ' = ', color= 'Green', expand= 1),
        ])
    )
ft.app(target=main)