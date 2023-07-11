from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author
from typing import List

app = FastAPI()


@app.post('/book')
def create_book(item: Book, author: Author, quantity: int = Body(...)):
    return {"item": item, "author": author, "quantity": quantity}


@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    return {"author": author}


@app.get('/book')
def get_book(q: List[str] = Query(['test', 'test2'], min_length=2, max_length=5, description="Search book",
                                  deprecated=True)):
    return q
