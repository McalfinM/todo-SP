
from src.services import TodoService


class TodoController:
    def createTodo(payload):
        data = TodoService.TodoService.create(payload)
        return data

    def get_all():
        data = TodoService.TodoService.get_all()
        return data

    def get_one(id):
        data = TodoService.TodoService.get_one(id)
        print(data)
        return data

    def update(id, payload):
        data = TodoService.TodoService.update(id, payload)

        return data

    def update_finish(id):
        data = TodoService.TodoService.todo_finish(id)

        return data

    def delete(id):
        data = TodoService.TodoService.delete(id)

        return data
