from email import message
from random import randint
from uuid import uuid4
from datetime import datetime
import src.repository.TodoRepository as todoRepo


class TodoService:

    def create(payload):
        data = {
            "id": randint(1, 999),
            "title": payload.title,
            "description": payload.description,
            "finished_at": "",
            "created_at": datetime.today().strftime('%d-%m-%Y %H:%M:%S'),
            "updated_at": datetime.today().strftime('%d-%m-%Y %H:%M:%S'),
            "deleted_at": "",
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
        if todo:
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
            None

    def todo_finish(id):
        todo = todoRepo.TodoRepository.get_one(id)
        if todo:
            data = todoRepo.TodoRepository.todo_finish(id)
            return {"message": "data berhasil diupdate"}
        else:
            None

    def delete(id):
        todo = todoRepo.TodoRepository.get_one(id)
        if todo:
            data = todoRepo.TodoRepository.delete(id)
            return {"message": "data berhasil diupdate"}
        else:
            None
