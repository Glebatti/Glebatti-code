from pydantic import BaseModel, validator, Field
from datetime import date
from typing import List


class Genre(BaseModel):
    name: str


class Author(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str
    age: int = Field(..., gt=15, lt=90, description='Author age must be more than 15 and less 90')

    # @validator('age')
    # def check_age(cls, v):
    #     if v < 15 > 90:
    #         raise ValueError('Author age must be more than 15')
    #     return v



class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre] = []
    pages: int = 10



class BookOut(Book):
    id: int