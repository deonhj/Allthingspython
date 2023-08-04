while True:
    user_action = input("Type add, show, edit, complete or exit.").strip().upper()

    match user_action:
        case 'ADD' | 'A':
            todo = input("enter a todo:") + '\n'

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'SHOW' | 'S':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")
        case 'EDIT' | 'E':
            number = int(input("Number of the item you want to edit:"))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo:")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'EXIT' | 'X':
            print('Bye!')
            break
        case 'COMPLETE' | 'C':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            number = int(input("Number of the item you want to complete:"))
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        case _:
            print("That was not a valid option.")



