import PySimpleGUI as Sg
from zip_extractor import extract_archive

Sg.theme("Black")

label1 = Sg.Text("Select archive:")
input1 = Sg.Input()
choose_button1 = Sg.FileBrowse("Choose", key="archive")

label2 = Sg.Text("Select destination:")
input2 = Sg.Input()
choose_button2 = Sg.FolderBrowse("Choose", key="folder")

extract_button = Sg.Button("Extract")
output_label = Sg.Text(key="output", text_color="green")

col1 = Sg.Column([[label1], [label2]])
col2 = Sg.Column([[input1], [input2]])
col3 = Sg.Column([[choose_button1], [choose_button2]])

window = Sg.Window("Archive Extractor",
                   layout=[[col1, col2, col3],
                           [extract_button, output_label]])


while True:
    event, values = window.read()
    print(event, values)
    extract_archive(values["archive"], values["folder"])
    window["output"].update(value="Extract completed!")

window.close()
