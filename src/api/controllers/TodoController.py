
from src.services import TodoService
from fastapi import HTTPException


class TodoController:
    def createTodo(payload):
        data = TodoService.TodoService.create(payload)
        return {"message": "data berhasil ditambahkan"}

    def get_all():
        data = TodoService.TodoService.get_all()
        return data

    def get_one(id):
        data = TodoService.TodoService.get_one(id)
        if data is None:
            raise HTTPException(status_code=404, detail="data not found")
        else:
            return data

    def update(id, payload):
        data = TodoService.TodoService.update(id, payload)

        if data is None:
            raise HTTPException(status_code=404, detail="data not found")
        else:
            return data

    def update_finish(id):
        data = TodoService.TodoService.todo_finish(id)

        if data is None:
            raise HTTPException(status_code=404, detail="data not found")
        else:
            return data

    def delete(id):
        data = TodoService.TodoService.delete(id)

        if data is None:
            raise HTTPException(status_code=404, detail="data not found")
        else:
            return data
