from email import message
from random import randint
from uuid import uuid4
from datetime import datetime
import src.repository.TodoRepository as todoRepo


class TodoService:

    def create(payload):
        data = {
            "id": randint(1, 100),
            "title": payload.title,
            "description": payload.description,
            "finished_at": 0,
            "created_at": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            "deleted_at": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
        }

        todo = todoRepo.TodoRepository.create(data)
        return todo

    def get_all():
        todo = todoRepo.TodoRepository.get_all()
        data = []
        for i in todo:
            if i['deleted_at'] == "":
                data.append(i)

        return data

    def get_one(id):
        todo = todoRepo.TodoRepository.get_one(id)
        if todo['deleted_at'] == "":
            return todo
        else:
            return {"message": "data not found"}

    def update(id, payload):
        todo = todoRepo.TodoRepository.get_one(id)
        if todo:
            data = todoRepo.TodoRepository.update(id, payload)
            return data
        else:
            return {"message": "data not found"}

    def todo_finish(id):
        todo = todoRepo.TodoRepository.get_one(id)
        if todo:
            data = todoRepo.TodoRepository.todo_finish(id)
            return {"message": "data berhasil diupdate"}
        else:
            return {"message": "data not found"}

    def delete(id):
        todo = todoRepo.TodoRepository.get_one(id)
        if todo:
            data = todoRepo.TodoRepository.delete(id)
            return {"message": "data berhasil diupdate"}
        else:
            return {"message": "data not found"}
