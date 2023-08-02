while True:
    user_action = input("Type add, show, edit, complete or exit.").strip().upper()

    match user_action:
        case 'ADD' | 'A':
            todo = input("enter a todo:") + '\n'
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'SHOW' | 'S':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")
        case 'EDIT' | 'E':
            number = int(input("Number of the item you want to edit:"))
            todos[number - 1] = input("Enter the new item:")
        case 'EXIT' | 'X':
            print('Bye!')
            break
        case 'COMPLETE' | 'C':
            number = int(input("Number of the item you want to complete:"))
            todos.pop(number - 1)
        case _:
            print("That was not a valid option.")



