from asyncpg import UniqueViolationError

from db_api.schemas import Jokes


async def add_joke(jokes: str, category: str):
    try:
        joke = Jokes(jokes=jokes, category=category, rating=0)
        await joke.create()
    except UniqueViolationError:
        print("Анекдот не добавлен")


async def select_all_jokes():
    jokes = await Jokes.query.gino.all()
    return jokes


async def select_joke(joke_id):
    joke = await Jokes.query.where(Jokes.joke_id == joke_id).gino.first()
    return joke


async def select_category_jokes(category):
    jokes = await Jokes.query.where(Jokes.category == category).gino.all()
    return jokes


async def change_rating(joke_id, changes: int):
    joke = await select_joke(joke_id)
    await joke.update(rating=joke.rating + changes).apply()
