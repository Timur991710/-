from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def all_user() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def new_users(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',example='Timur')],
                    age: Annotated[int, Path(gt=18, le=120, description='Enter age', example='37')]) -> str:
    current_index = str(int(max(users, key= str)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f'User {current_index} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def user(user_id: Annotated[str,Path(min_length=1, max_length=100, description='Enter User ID', example='12')],
               username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',example='Timur')],
                age: Annotated[int, Path(gt=18, le=120, description='Enter age', example='37')]
               ) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is updated"


@app.delete ('/user/{user_id}')
async def user_delete (user_id: Annotated[str, Path(min_length=1, max_length=100, description='Enter User ID', example='0')]) -> str:
    users.pop(user_id)
    return f'Delete user {user_id}'


"""Запуск файла 
python -m uvicorn module_16_3:app
"""