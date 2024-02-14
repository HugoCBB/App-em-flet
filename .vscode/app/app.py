import flet as ft
def main(page: ft.Page):
    page.bgcolor = 'Black'
    page.window_height = 450
    page.window_width = 450
    page.window_resizable = True
    page.window_maximizable = True
    page.title = 'Calculadora'

    def get_data(e):
        resultado_at = resultado.value if resultado.value != '0' else ''
        data = e.control.data
        if data in ('0','1','2','3','4','5','6','7','8','9'):
            data = resultado_at + data
        
        else:
            if resultado_at and resultado_at[:-1] in ('+','-','*','/','.'):
                data = resultado_at[:-1]
        
            if data[-1] in ('=','%','+/-'):
                data = calculo(data = data[-1], resultado_at = resultado_at)
            
        resultado.value = data
        page.update()

    def clear(e):
        resultado.value = ''
        page.update()
    
    def calculo(data, resultado_at):
        data = eval(resultado_at)
        return data

    page.add(
        
    )

    resultado = ft.Text(value= '0', color= 'White')
    page.add(
        ft.Row(controls=[
            resultado,
        ])
    )
    page.add(
        ft.Row(controls=[
            ft.ElevatedButton(text= 'AC',bgcolor= ft.colors.TRANSPARENT,color= 'Red', expand= 1, style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()),on_click= clear),
            ft.ElevatedButton(text= '+/-',bgcolor= ft.colors.TRANSPARENT, color= 'White', expand= 1,data = '+/-', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()), on_click= get_data),
            ft.ElevatedButton(text= '%',bgcolor= ft.colors.TRANSPARENT, color= 'White', expand= 1,data = '%', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()), on_click= get_data),
            ft.ElevatedButton(text= '/',bgcolor= ft.colors.TRANSPARENT, color= 'White', expand= 1,data = '/', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()), on_click= get_data),
        ])
    )
    page.add(
        ft.Row(controls=[
            ft.ElevatedButton(text= ' 7 ',bgcolor= ft.colors.TRANSPARENT, color= 'White', expand= 1,data = '7', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()), on_click= get_data),
            ft.ElevatedButton(text= ' 8 ',bgcolor= ft.colors.TRANSPARENT, color= 'White', expand= 1,data = '8', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()), on_click= get_data),
            ft.ElevatedButton(text= ' 9 ',bgcolor= ft.colors.TRANSPARENT, color= 'White', expand= 1,data = '9', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()), on_click= get_data),
            ft.ElevatedButton(text= ' * ',bgcolor= ft.colors.TRANSPARENT, color= 'White', expand= 1,data = '*', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()), on_click= get_data),
        ])
    )
    page.add(
        ft.Row(controls=[
            ft.ElevatedButton(text= ' 4 ',bgcolor= ft.colors.TRANSPARENT, color= 'White', expand= 1,data = '4', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()), on_click= get_data),
            ft.ElevatedButton(text= ' 5 ',bgcolor= ft.colors.TRANSPARENT, color= 'White', expand= 1,data = '5', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()), on_click= get_data),
            ft.ElevatedButton(text= ' 6 ',bgcolor= ft.colors.TRANSPARENT, color= 'White', expand= 1,data = '6', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()), on_click= get_data),
            ft.ElevatedButton(text= ' - ',bgcolor= ft.colors.TRANSPARENT, color= 'White', expand= 1,data = '-', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()), on_click= get_data),
        ])
    )
    page.add(
        ft.Row(controls=[
            ft.ElevatedButton(text= ' 1 ',bgcolor= ft.colors.TRANSPARENT, color= 'White', expand= 1,data = '1', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()), on_click= get_data),
            ft.ElevatedButton(text= ' 2 ',bgcolor= ft.colors.TRANSPARENT, color= 'White', expand= 1,data = '2', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()), on_click= get_data),
            ft.ElevatedButton(text= ' 3 ',bgcolor= ft.colors.TRANSPARENT, color= 'White', expand= 1,data = '3', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()), on_click= get_data),
            ft.ElevatedButton(text= ' + ',bgcolor= ft.colors.TRANSPARENT, color= 'White', expand= 1,data = '+', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()), on_click= get_data),
        ])
    )
    page.add(
        ft.Row(controls=[
            ft.ElevatedButton(text= ' 0 ',bgcolor= ft.colors.TRANSPARENT, color= 'White', expand= 1,data = '0', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()),on_click= get_data),
            ft.ElevatedButton(text= ' . ',bgcolor= ft.colors.TRANSPARENT, color= 'White', expand= 1,data = '.', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()), on_click= get_data),
            ft.ElevatedButton(text= ' = ',bgcolor= ft.colors.TRANSPARENT,color= 'Green', expand= 1,data = '=', style= ft.ButtonStyle(padding= 25, shape=ft.CircleBorder()), on_click= get_data),
        ])
    )
ft.app(target=main)