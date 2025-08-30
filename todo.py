class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title

    @property
    def todos(self):
        return self._todos

    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError

        self.todos.append(todo)

    def __str__(self):
        todo_list = [f"----- {self.title} -----"] + ([str(todo) for todo in self.todos])
        return "\n".join(todo_list)

    def __len__(self):
        return len(self.todos)

    def first(self):
        return self.todos[0]

    def last(self):
        return self.todos[-1]

    def to_list(self):
        return self.todos[:]

    def todo_at(self, idx):
        return self.todos[idx]

    def mark_done_at(self, idx):
        self.todo_at(idx).done = True

    def mark_undone_at(self, idx):
        self.todo_at(idx).done = False

    def mark_all_done(self):
        self.each(lambda todo: self.mark_done(todo.title))

    def mark_all_undone(self):
        self.each(lambda todo: self.mark_undone(todo.title))

    def all_done(self):
        return all(todo.done for todo in self.todos)

    def remove_at(self, idx):
        self.todos.pop(idx)

    def each(self, callback):
        for todo in self.todos:
            callback(todo)

    def select(self, callback):
        new_list = TodoList(self.title)
        for todo in filter(callback, self.todos):
            new_list.add(todo)

        return new_list

    def find_by_title(self, title):
        title_list = self.select(lambda todo: todo.title == title)
        return title_list.todo_at(0)

    def done_todos(self):
        return self.select(lambda todo: todo.done)

    def undone_todos(self):
        return self.select(lambda todo: not todo.done)

    def mark_done(self, title):
        self.find_by_title(title).done = True

    def mark_undone(self, title):
        self.find_by_title(title).done = False


class Todo:
    IS_DONE = "X"
    IS_UNDONE = " "

    def __init__(self, title):
        self._title = title
        self.done = False

    @property
    def title(self):
        return self._title

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, done):
        self._done = done

    def __str__(self):
        marker = Todo.IS_DONE if self.done else Todo.IS_UNDONE
        return f"[{marker}] {self.title}"

    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented

        return self.done == other.done and self.title == other.title

empty_todo_list = TodoList('Nothing Doing')
def setup():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')

    todo2.done = True

    todo_list = TodoList("Today's Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)

    return todo_list

def step_8():
    print('--------------------------------- Step 8')
    todo_list = setup()

    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [ ] Go to gym

    todo_list.mark_all_done()
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room
    # [X] Go to gym

    todo_list.mark_all_undone()
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room
    # [ ] Go to gym

step_8()