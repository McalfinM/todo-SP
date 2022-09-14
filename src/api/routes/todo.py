from fastapi import APIRouter
import src.api.request.todo as request
import src.api.controllers.TodoController as controller

router = APIRouter()


@router.post("/create", status_code=201)
async def create(payload: request.TodoRequest):
    data = controller.TodoController.createTodo(payload)
    return data


@router.get("/get", status_code=200)
async def get_all():
    data = controller.TodoController.get_all()
    return data


@router.get("/get/{id}")
async def get_one(id):
    data = controller.TodoController.get_one(id)
    return data


@router.put("/update/{id}", status_code=200)
async def update(id, payload: request.TodoRequest):
    data = controller.TodoController.update(id, payload)
    return data


@router.patch("/finish/{id}", status_code=200)
async def update(id):
    data = controller.TodoController.update_finish(id)
    return data


@router.delete("/delete/{id}", status_code=200)
async def delete(id):
    data = controller.TodoController.delete(id)
    return data
