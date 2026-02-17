from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

BACKEND_URL = "http://localhost:8000"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "Файл не найден"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Файл не выбран"}), 400

    # Отправляем файл в бэкенд
    files = {'file': (file.filename, file.stream, file.mimetype)}
    try:
        resp = requests.post(f"{BACKEND_URL}/upload", files=files, timeout=30)
    except Exception as e:
        return jsonify({"error": f"Ошибка связи с бэкендом: {str(e)}"}), 500

    if resp.status_code != 200:
        return jsonify({"error": "Бэкенд вернул ошибку"}), 500
    return resp.json()

@app.route('/ids')
def get_ids():
    try:
        resp = requests.get(f"{BACKEND_URL}/ids", timeout=10)
    except Exception as e:
        return jsonify({"error": f"Ошибка связи с бэкендом: {str(e)}"}), 500
    if resp.status_code != 200:
        return jsonify({"error": "Данные не загружены"}), 500
    return resp.json()

@app.route('/data')
def get_data():
    id = request.args.get('id')
    params = {}
    if id:
        params['id'] = id

    try:
        resp = requests.get(f"{BACKEND_URL}/data", params=params, timeout=10)
    except Exception as e:
        return jsonify({"error": f"Ошибка связи с бэкендом: {str(e)}"}), 500
    if resp.status_code != 200:
        return jsonify({"error": "Нет данных"}), 500
    return resp.json()


if __name__ == '__main__':
    app.run(port=5001, debug=True)