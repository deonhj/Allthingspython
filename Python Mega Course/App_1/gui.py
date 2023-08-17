import functions
import PySimpleGUI as Sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

Sg.theme("Topanga")

clock = Sg.Text('', key="clock")
label = Sg.Text("Type in a todo")
input_box = Sg.InputText(tooltip="Enter todo", key="todo")
add_button = Sg.Button(image_source='add.png',
                       tooltip='Add Todo Item',
                       image_size=(160, 30),
                       mouseover_colors='LightBlue2',
                       key="Add")
list_box = Sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True, size=(45, 10))
edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")
exit_button = Sg.Button("Exit")

window = Sg.Window("My todo app",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 16))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + "\n")
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = values['todo'] + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                Sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                Sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case Sg.WIN_CLOSED:
            break
window.close()
