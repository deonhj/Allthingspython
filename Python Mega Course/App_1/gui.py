import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a todo")
input_box = Sg.InputText(tooltip="Enter todo", key="todo")
add_button = Sg.Button("Add")

window = Sg.Window("My todo app",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 16))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + "\n")
            functions.write_todos(todos)
        case Sg.WIN_CLOSED:
            break
window.close()
