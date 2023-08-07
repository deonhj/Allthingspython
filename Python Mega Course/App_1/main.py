while True:
    user_action = input("Type add, show, edit, complete or exit.").strip().upper()

    if 'ADD' in user_action or 'NEW' in user_action:
        todo = user_action[4:] + '\n'

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'SHOW' in user_action:

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            print(f"{index + 1}. {item}")

    elif 'EDIT' in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo:")
        todos[number] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'COMPLETE' in user_action:

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        number = int(user_action[9:])
        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)

    elif 'EXIT' in user_action:
        print('Bye!')
        break

    else:
        print("Command is not valid.")

print("Bye!")

