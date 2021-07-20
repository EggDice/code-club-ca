class TodoApp:
  DATABASE_FILE = 'todos.txt'
  command = None
  argument = None

  def __init__(self, argv):
    self.command, self.argument = self.parse_arguments(argv)

  def parse_arguments(self, argv):
    if len(argv) > 2:
      return argv[1:]
    return argv[1], None

  def run(self):
    if self.command == 'add':
      self.add_new(self.argument)
    elif self.command == 'list':
      self.list_all()
    elif self.command == 'delete':
      self.delete_by_index(int(self.argument) - 1)

  def add_new(self, new_todo):
    todos = self.read_todos()
    todos.append(new_todo)
    self.write_todos(todos)

  def list_all(self):
    for i, line in enumerate(self.read_todos()):
      print(f'{i + 1} - {line[:-1]}')

  def delete_by_index(self, index):
    todos = self.read_todos()
    del todos[index]
    self.write_todos(todos)

  def read_todos(self):
    with open(self.DATABASE_FILE) as file:
      return file.readlines()

  def write_todos(self, todos):
    with open(self.DATABASE_FILE, 'w') as file:
      file.writelines(todos)

