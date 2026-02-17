import os
import shutil
import pandas as pd
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI()

# Разрешаем запросы с фронтенда (порт 5000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Хранилище загруженных данных (в памяти для простоты)
data_store = {}

def parse_csv(filepath: str):
    """
    Читает CSV с колонками: timestamp, id, data
    Возвращает DataFrame.
    """
    df = pd.read_csv(filepath)
    # Проверяем наличие нужных колонок
    required = ['timestamp', 'id', 'data']
    if not all(col in df.columns for col in required):
        raise ValueError("CSV должен содержать колонки: timestamp, id, data")
    return df

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        df = parse_csv(filepath)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка парсинга CSV: {str(e)}")

    # Сохраняем DataFrame и список уникальных ID
    data_store['df'] = df
    data_store['ids'] = sorted(df['id'].unique().tolist())
    data_store['filename'] = file.filename

    return {"ids": data_store['ids'], "message": "Файл успешно загружен"}

@app.get("/ids")
def get_ids():
    if 'ids' not in data_store:
        raise HTTPException(status_code=404, detail="Данные не загружены")
    return {"ids": data_store['ids']}

@app.get("/data")
def get_data(id: Optional[int] = None, from_time: Optional[float] = None, to_time: Optional[float] = None):
    if 'df' not in data_store:
        raise HTTPException(status_code=404, detail="Данные не загружены")

    df = data_store['df']
    if id is not None:
        df = df[df['id'] == id]
    if from_time is not None:
        df = df[df['timestamp'] >= from_time]
    if to_time is not None:
        df = df[df['timestamp'] <= to_time]

    # Преобразуем в список словарей для JSON
    result = df.to_dict(orient='records')
    return result