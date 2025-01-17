from fastapi import FastAPI, status, Body, HTTPException, Request, Form
from fastapi.responses import  HTMLResponse
from typing import  List, Annotated
from pydantic import BaseModel, Field
from fastapi.templating import Jinja2Templates
from starlette.datastructures import FormData

app = FastAPI()
templates = Jinja2Templates(directory="templatesPro")




class User(BaseModel):
    id: int
    username: str
    age: int


class UserCreate(BaseModel):
    username: str = Field(min_length=5, max_length=100, description="Введите имя пользователя")
    age: int = Field(gt=18, lt=120, description="Введите возраст пользователя")


users: List[User] = []

@app.get("/")
async def all_user(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html',{'request': request, 'users': users })


@app.get(path="/user/{user_id}")
async def user(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse('users.html',{'request': request, 'user': users[user_id - 1]})


@app.post(path='/user/{username}/{age}',  response_model = User)
async def new_users(user: UserCreate):
    new_id = max((t.id for t in users), default=0) + 1
    new_user = User(id = new_id, username = user.username, age = user.age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}', response_model = User)
async def update_user(user_id: int, user: UserCreate):
    for i in users:
        if i.id == user_id:
            i.username = user.username
            i.age = user.age
            return i
    raise HTTPException(status_code=404, detail="Пользователь не найден")




@app.delete ('/user/{user_id}', response_model=dict)
async def user_delete (user_id: int):
    for i, t in enumerate(users):
        if t.id == user_id:
            del users[i]
            return {"detail": "Пользователь удален"}
    raise HTTPException(status_code=404, detail="Пользователь не найден")


"""Запуск файла 
python -m uvicorn module_16_5:app
"""