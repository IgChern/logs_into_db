# Fix_Logs

### Описание
Django приложение для обработки и агрегации лога.

### Структура проекта
В составе приложения имеется Management command, которая на вход принимает ссылку на лог файл определенного формата, парсит и записывает в БД. Ссылка на файл для теста
[https://drive.google.com/file/d/18Ss9afYL8xTeyVd0ZTfFX9dqja4pBGVp/view?usp=sharin](https://drive.google.com/file/d/18Ss9afYL8xTeyVd0ZTfFX9dqja4pBGVp/view?usp=sharin)
В приложении есть модель, которая описывает распарсенные данные из лога. Отображение загруженых данных реализовано через Django admin и API (DRF).


## Требования для пользования приложением

Убедитесь, что Docker и Docker-Compose установлены на вашем ПК.


### 1. Склонируйте репозиторий:

    git clone https://github.com/IgChern/logs_into_db

### 2. Перейдите по пути проекта:

    cd logs_into_db

### 3. Создайте файл .env со своими собственными настройками:

    POSTGRES_NAME=<your_settings>
    POSTGRES_USER=<your_settings>
    POSTGRES_PASSWORD=<your_settings>
    POSTGRES_HOST=<your_settings>
    POSTGRES_PORT=<your_settings>
    SECRET_KEY=<your_settings>

### 4. Соберите и запустите Docker контейнер:

    docker-compose build
    docker-compose up

### 5. Доступ к интерфейсу проекта:  
1. [http://127.0.0.1:8000/api/logs/](http://127.0.0.1:8000/api/logs/) - API интерфейс для работы с данными (реализована пагинация, фильтр и поиск)
2. [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) - API документация
3. [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/) - API документация

### 6. Запуск тестов для проверки модели и парсинга из файла:

    docker ps
    docker exec -it <DockerID_fix_logs-django> python3 manage.py test
    docker exec -it <DockerID_fix_logs-django> python3 manage.py parse_logs "https://drive.google.com/uc?id=18Ss9afYL8xTeyVd0ZTfFX9dqja4pBGVp"




### 7. Остановка Docker контейнера:

    docker-compose down
