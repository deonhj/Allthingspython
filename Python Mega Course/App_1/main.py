while True:
    user_action = input("Type add, show, edit, complete or exit.").strip().upper()

    if user_action.startswith("ADD") or user_action.startswith("NEW"):
        todo = user_action[4:] + '\n'

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("SHOW"):

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            print(f"{index + 1}. {item}")

    elif user_action.startswith("EDIT"):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo:")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid")
            continue  # the while will run again from the start

    elif user_action.startswith("COMPLETE"):
        try:
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
        except IndexError:
            print(f"Please enter a number between {1} and {len(todos)}")
            continue
        except ValueError:
            print(f"That is not a valid number, please enter a number between {1} and {len(todos)}")

    elif user_action.startswith("EXIT"):
        print('Bye!')
        break

    else:
        print("Command is not valid.")

print("Bye!")

