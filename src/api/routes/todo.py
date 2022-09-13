from fastapi import APIRouter, Request
import src.api.request.todo as request
import src.api.controllers.TodoController as controller

router = APIRouter()


@router.post("/create", status_code=201)
async def create(payload: request.TodoRequest):
    data = controller.TodoController.createTodo(payload)
    return {"data": data, "message": "todo berhasil ditambahkan"}


@router.get("/get", status_code=200)
async def get_all():
    data = controller.TodoController.get_all()
    return data


@router.get("/get/{id}", status_code=200)
async def get_one(id):
    data = controller.TodoController.get_one(id)
    return data


@router.post("/update/{id}", status_code=200)
async def update(id, payload: request.TodoRequest):
    data = controller.TodoController.update(id, payload)
    return data


@router.post("/finish/{id}", status_code=200)
async def update(id):
    data = controller.TodoController.update_finish(id)
    return data


@router.post("/delete/{id}", status_code=200)
async def delete(id):
    data = controller.TodoController.delete(id)
    return data
