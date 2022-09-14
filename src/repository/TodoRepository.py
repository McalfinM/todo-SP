from operator import mod
import src.models.TodoModel as model
import json
from datetime import date, datetime


class TodoRepository:

    def create(payload):
        filename = "list_todo.json"
        with open(filename, "r") as file:
            data = json.load(file)

        data.append(payload)

        with open(filename, "w") as file:
            json.dump(data, file)

        print(payload)
        return payload

    def get_all():
        filename = "list_todo.json"
        with open(filename, "r") as file:
            data = json.load(file)

        return data

    def get_one(id):
        filename = "list_todo.json"
        with open(filename, "r") as file:
            data = json.load(file)

        for i in data:
            if i['id'] == int(id):
                print(i['title'])
                return {
                    "id": i['id'],
                    "title": i['title'],
                    "description": i['description'],
                    "finished_at": i['finished_at'],
                    "created_at": i['created_at'],
                    "updated_at": i['updated_at'],
                    "deleted_at": i['deleted_at']
                }

    def update(id, payload):
        filename = "list_todo.json"

        with open(filename, 'r+', encoding='utf-8') as f:
            my_list = json.load(f)

            for obj in my_list:

                if obj['id'] == int(id):
                    obj['title'] = payload.title
                    obj['description'] = payload.description
                    # my_list.pop(idx))

        with open(filename, 'w') as f:
            json.dump(my_list, f)

        return {"message": "data berhasil di update"}

    def todo_finish(id):
        filename = "list_todo.json"

        with open(filename, 'r+', encoding='utf-8') as f:
            my_list = json.load(f)

            for obj in my_list:

                if obj['id'] == int(id):
                    obj['finished_at'] = datetime.today().strftime(
                        '%Y-%m-%d %H:%M:%S')
                    # my_list.pop(idx))

        with open(filename, 'w') as f:
            json.dump(my_list, f)

        return {"message": "data berhasil di update"}

    def delete(id):
        filename = "list_todo.json"

        with open(filename, 'r+', encoding='utf-8') as f:
            my_list = json.load(f)

            for obj in my_list:

                if obj['id'] == int(id):
                    obj['deleted_at'] = datetime.today().strftime(
                        '%Y-%m-%d %H:%M:%S')
                    # my_list.pop(idx))

        with open(filename, 'w') as f:
            json.dump(my_list, f)

        return {"message": "data berhasil di hapus"}
