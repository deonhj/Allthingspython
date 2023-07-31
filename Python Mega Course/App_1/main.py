todos = []

while True:
    user_action = input("Type add, show, edit or exit.").strip().upper()

    match user_action:
        case 'ADD':
            todo = input("enter a todo:")
            todos.append(todo)
        case 'SHOW' | 'DISPLAY':
            for item in todos:
                print(item)
        case 'EDIT':
            number = int(input("Number of the item you want to edit:"))
            todos[number - 1] = input("Enter the new item:")
        case 'EXIT':
            print('Bye!')
            break
        case _:
            print("That was not a valid option.")



