from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Annotated
from .database import get_session
from .users.models import User
from .schemas import UserSchema


app = FastAPI()

SessionDependence = Annotated[AsyncSession, Depends(get_session)]


@app.get('/users')
async def get_users(session: SessionDependence):
    query = select(User)
    result = await session.execute(query)
    return result.all()

@app.post('/users')
async def post_users(data: UserSchema, session: SessionDependence):
    create = User(
		name=data.name, email=data.email
	)
    session.add(create)
    await session.commit()
    return create
