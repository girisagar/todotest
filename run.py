from todo import ToDoList, ToDo


class Interact:
    def __init__(self):
        self.todo_list = ToDoList()

    def list_todo(self):
        self.todo_list.print()

    def add_todo(self):
        title = input("Type a todo: ")
        todo = ToDo(title)
        self.todo_list.add(todo)

    def update_todo(self):
        self.list_todo()
        todo_index = int(input("Please choose the index to update: "))
        new_title = input("Please enter new title: ")
        self.todo_list.update(todo_index, new_title)

    def delete_todo(self):
        self.list_todo()
        todo_index = int(input("Please choose the index to delete: "))
        self.todo_list.delete(todo_index)

    def request_action(self):
        print("l: List all the todos")
        print("a: Add new todo")
        print("u: update todo")
        print("d: delete todo")
        print("q: quit")

        action = input("Please choose one of the options above: ")
        return action

    def do_action(self, user_input):
        if user_input == 'l':
            self.list_todo()
        elif user_input == 'a':
            self.add_todo()
        elif user_input == 'u':
            self.update_todo()
        elif user_input == 'd':
            self.delete_todo()
        elif user_input == 'q':
            exit()
        else:
            print(f"WARN!: You choose wrong option")

    def start(self):
        while True:
            print(f"\n")
            user_input = self.request_action()
            self.do_action(user_input)


if __name__ == '__main__':
    interaction = Interact()
    interaction.start()
