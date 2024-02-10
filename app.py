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
def soma(a,b):
    print(1)
def subtracao(a,b):
    pass
def multiplicacao(a,b):
    pass
def divisao(a,b):
    pass
lista = []
def main(page: ft.Page):
    def numeros(e):
        page.add(
            ft.Row(controls=[
                ft.ElevatedButton(text= '0'),
                ft.ElevatedButton(text= '1'),
                ft.ElevatedButton(text= '2'),
                ft.ElevatedButton(text= '3'),
                ft.ElevatedButton(text= '4'),
                ft.ElevatedButton(text= '5'),
                ft.ElevatedButton(text= '6'),
                ft.ElevatedButton(text= '7'),
                ft.ElevatedButton(text= '8'),
                ft.ElevatedButton(text= '9'),
            ])
        )
    numeros(lista)
ft.app(target=main)