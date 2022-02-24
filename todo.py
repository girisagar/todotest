import os


class ToDo():
    def __init__(self, title):
        self.title = title

    def update(self, new_title):
        self.title = new_title


class ToDoList():
    def __init__(self):
        self.filename = '/tmp/todolist.txt'
        self.todos = []
        self.load()

    def add(self, todo):
        """add a new todo"""
        self.todos.append(todo)
        self.save()

    def update(self, todo_index, new_title):
        """update any todo for a given index"""
        todo = self.todos[todo_index]
        todo.update(new_title)
        self.save()

    def delete(self, todo_index):
        """delete any todo for a given index"""
        del self.todos[todo_index]
        self.save()

    def print(self):
        """Print all the todo in the list"""
        print("\n********* List of all the todos **********")
        if self.todos:
            for index, todo in enumerate(self.todos):
                print(f"{index:<2}. {todo.title}")
        else:
            print("No todo found")
        print("************************************\n")

    def save(self):
        """save list of todos to a file"""
        with open(self.filename, 'w') as fd:
            for todo in self.todos:
                fd.write(f"{todo.title}\n")

    def load(self):
        """load from file to list"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as fd:
                for line in fd.readlines():
                    title = line.strip("\n")
                    todo = ToDo(title)
                    self.todos.append(todo)
