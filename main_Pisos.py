import PySimpleGUI as sg
from Calculo_P import *

menu_layout = (
    ["ajuda",["Como usar?"]],
)
layout = [

      [sg.Menu(menu_layout)],
      [sg.Text("Largura - A",size=(12,1)),sg.In(size=(15,1),key='La')],
      [sg.Text("Compri  - A",size=(12,1)),sg.In(size=(15,1),key='Ca')],
      [sg.Text("Largura - P",size=(12,1)),sg.In(size=(15,1),key='Lp')],
      [sg.Text("Compri  - P",size=(12,1)),sg.In(size=(15,1),key='Cp')],
      [sg.Button("Calcular" ,key='calcular'), sg.Exit()],
      [sg.Output(size=(30,5))]

 ]

janela = sg.Window("Pisos_v1.0_Relese", layout, size=(260, 260), element_justification='right')


def utili():
    sg.PopupNoTitlebar("""                   No primeiro campo a largura da área.
                   No segundo o comprimento da área.
                   No terceiro a largura do piso.
                   No quarto o comprimento do piso.\n
                   Autor: Washington Luis de Assis Pereira .
                   Contato: slash.o.teobaldo@gmail.com  
    
""")



while True:
    event, values = janela.read(timeout=0)
    if event == "Como usar?":
        utili()
    if event == "calcular":
        print(pecasL(float(values['La']),float(values['Lp'])))
        print(pecasA(float(values['Ca']),float(values['Cp'])))
        print(cobert(float(values['Lp']),float(values['Cp'])))

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
janela.close()
