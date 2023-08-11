import functions as f

while True:
    user_action = input("Type add, show, edit, complete or exit.").strip().upper()

    if user_action.startswith("ADD") or user_action.startswith("NEW"):
        todo = user_action[4:] + '\n'

        todos = f.get_todos()

        todos.append(todo)

        f.write_todos(todos)

    elif user_action.startswith("SHOW"):

        todos = f.get_todos()

        todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            print(f"{index + 1}. {item}")

    elif user_action.startswith("EDIT"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = f.get_todos()

            new_todo = input("Enter new todo:")
            todos[number] = new_todo.upper() + '\n'

            f.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue  # the while will run again from the start

    elif user_action.startswith("COMPLETE"):
        try:
            todos = f.get_todos()

            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            f.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print(f"Please enter a number. ")
            continue
        except ValueError:
            print(f"That is not a valid number, please enter a number. ")

    elif user_action.startswith("EXIT"):
        print('Bye!')
        break
    else:
        print("Command is not valid.")
