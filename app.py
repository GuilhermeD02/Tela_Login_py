import PySimpleGUI as sg
from time import sleep

sg.theme('reddit')

# layout
tela_login = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(password_char='*', key='senha')],
    [sg.Button('Enviar')],
    [sg.Output(size=(43,10))]

]
# criar a janela
janela = sg.Window('Login', layout=tela_login)
# ler os eventos
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Enviar':
        usuario_digitado = values['usuario']
        senha_digitada = values['senha']
        print('Passo 1..feito')
        sleep(5)
        print('Passo 2..feito')
        sleep(5)
        print('Passo 3..feito')
