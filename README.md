🐳 FastAPI Docker App

Простое FastAPI-приложение в Docker-контейнере с примерами GET/POST запросов и HTML-формой.

🚀 Быстрый старт

# Сборка образа
docker build -t fastapi-docker-app .

# Запуск контейнера
docker run -d -p 8000:8000 --name fastapi-app fastapi-docker-app
Приложение будет доступно по адресу: http://localhost:8000

📚 Эндпоинты
GET	/	Приветственное сообщение
GET	/hello/{name}	Персонализированное приветствие
GET	/items/	HTML-форма для добавления предмета
POST	/items/	Создание предмета (принимает JSON)
Пример POST-запроса:

json
{
  "name": "Кружка",
  "price": 12.99,
  "in_stock": true
}

📖 Swagger UI
Интерактивная документация доступна по адресу:
👉 http://localhost:8000/docs

🐳 Управление контейнером
bash
# Остановка
docker stop fastapi-app

# Удаление
docker rm fastapi-app

# Просмотр логов
docker logs fastapi-app
