# ml-api_images
Проект по распознованию животных

1) Клонировать репозиторий git clon

2) Создайте виртуальное окружение python

python -m venv venv

3) Активируйте виртуальное окружение python

venv\Scripts\activate.bat - для Windows
source venv/bin/activate - для Linux и MacOS

4) Установите необходимые зависимости

pip install -r requirements.txt --no-cache-dir

5) Запустите приложение

uvicorn main:app

6) Приложение откроется по ссылке - http://localhost:8000