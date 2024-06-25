from sqlalchemy import BigInteger, Column, Integer, String, sql

from db_api.db_gino import BaseModel


class Jokes(BaseModel):
    __tablename__ = "jokes"
    joke_id = Column(Integer, primary_key=True, autoincrement=True)
    jokes = Column(String(1000))
    category = Column(String(20))
    rating = Column(BigInteger)

    query: sql.select
