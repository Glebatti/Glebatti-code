from fastapi import FastAPI
from schemas import Book, BookOut

app = FastAPI()


@app.post('/book', response_model=BookOut)
def create_book(item: Book):
    # book = item.dict()
    # book["id"] = 3
    return BookOut(**item.dict(), id=3)


#response_model_include={"pages", "date"}