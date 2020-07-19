import PySimpleGUI as sg
from Calculo_P import pecasL

menu_layout = (
    ["ajuda",["Como usar?"]],
)
layout = [

      [sg.Menu(menu_layout)],
      [sg.Text("Largura - A",size=(12,1)),sg.In(size=(15,1),key='La')],
      [sg.Text("Compri  - A",size=(12,1)),sg.In(size=(15,1),key='Ca')],
      [sg.Text("Largura - P",size=(12,1)),sg.In(size=(15,1),key='Lp')],
      [sg.Text("Compri  - P",size=(12,1)),sg.In(size=(15,1),key='Cp')],
      [sg.Text("Resultados",size=(28,1))],
      [sg.Button("Calcular"), sg.Exit()],
      [sg.Output(size=(30,5))]

 ]

janela = sg.Window("Pisos_v1.0_Relese", layout, size=(260, 260), element_justification='right')
event,values = janela.Read()

def utili():
    sg.PopupNoTitlebar("""                   No primeiro campo a largura da área.
                   No segundo o comprimento da área.
                   No terceiro a largura do piso.
                   No quarto o comprimento do piso.\n
                   Autor: Washington Luis de Assis Pereira .
                   Contato: slash.o.teobaldo@gmail.com  
    
""")



while True:
    if event == "Como usar?":
        utili()


