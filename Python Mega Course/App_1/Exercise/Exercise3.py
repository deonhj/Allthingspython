import PySimpleGUI as Sg
from convert_to_meters import convert

label1 = Sg.Text("Enter feet: ")
input1 = Sg.Input(key="feet")

label2 = Sg.Text("Enter inches: ")
input2 = Sg.Input(key="inches")
convert_button = Sg.Button("Convert", key="convert")
output_label = Sg.Text(key="output")

window = Sg.Window("Convertor",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case "convert":
            result = f"{convert(float(values['feet']), float(values['inches']))} m"
            window['output'].update(value=result)
        case Sg.WIN_CLOSED:
            break

window.close()
