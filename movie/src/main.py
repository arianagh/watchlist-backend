from fastapi import FastAPI

from src.core.containers import AppContainer
from src.infrastructures.fastapi.api.routes import routers

app = FastAPI()

container = AppContainer()
app.container = container

app.include_router(routers)


# from fastapi import Fast;API
# from pydantic import BaseModel
#
# app = FastAPI()
#
#
# class Movie(BaseModel):
#     id: int
#     name: str
#     director_id: int
#
#
# movies: list[Movie] = []
#
#
# @app.post("/")
# async def create_movie(movie: Movie):
#     movies.append(movie)
#     return movie
#
#
# @app.get("/{movie_id}")
# async def get_movie(movie_id: int):
#     for movie in movies:
#         if movie.id == movie_id:
#             return movie
#     return {"error": "Movie not found"}
#
#
# @app.delete("/{movie_id}")
# async def delete_movie(movie_id: int):
#     for movie in movies:
#         if movie.id == movie_id:
#             movies.remove(movie)
#             return {"message": "Movie deleted"}
#     return {"error": "Movie not found"}
