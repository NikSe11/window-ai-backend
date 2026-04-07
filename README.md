# AI Chat Backend (FastAPI)

Простой backend-сервис на FastAPI с интеграцией OpenAI API.

О проекте

Проект разработан в рамках изучения backend-разработки на Python. Основной упор сделан на понимание работы API, асинхронности и взаимодействия с внешними сервисами.

Функционал

- REST API
- Обработка запросов через FastAPI
- Асинхронные вызовы (async/await)
- Интеграция с OpenAI API
- Валидация данных через Pydantic

Запуск проекта

1. Клонировать репозиторий:


git clone <your_repo>
cd <project>


2. Создать виртуальное окружение:


python -m venv venv
venv\Scripts\activate


3. Установить зависимости:


pip install -r requirements.txt


4. Создать .env файл:


OPENAI_API_KEY=your_key


5. Запустить сервер:


uvicorn main:app --reload


Эндпоинты

GET /health
Проверка сервера

POST /chat
Отправка сообщения в AI

```json
{
  "message": "Привет"
}
