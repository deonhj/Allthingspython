todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit.").strip().upper()

    match user_action:
        case 'ADD':
            todo = input("enter a todo:")
            todos.append(todo)
        case 'SHOW' | 'DISPLAY':
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")
        case 'EDIT':
            number = int(input("Number of the item you want to edit:"))
            todos[number - 1] = input("Enter the new item:")
        case 'EXIT':
            print('Bye!')
            break
        case 'COMPLETE':
            number = int(input("Number of the item you want to complete:"))
            todos.pop(number - 1)
        case _:
            print("That was not a valid option.")



