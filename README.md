## Как запустить.

- Клонировать репозиторий
    ```bash
    git clone git@github.com:CaDiBob/test_task.git
    ```
- Перейти в папку с проектом
    ```bash
    cd test_task
    ```
- Переименовать файл `.env.example` в `.env` и заполнить переменные окружения\
    POSTGRES_HOST= `хост базы данных`\
    POSTGRES_PORT= `порт базы данных`\
    POSTGRES_USER= `имя пользователябазы данных`\
    POSTGRES_PASSWORD= `пароль пользователя базы данных`\
    POSTGRES_DB= `имя базы данных`

#### Запустить используя docker.
- Установить [docker](https://docs.docker.com/engine/install/) если не установлен.
- Собрать и запустить контейнер
    ```bash
    docker compose build
    docker compose up -d
    ```
#### Запустить локально.
- Установить [uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)
    ```bash
    # On macOS and Linux.
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
    ```PowerShell
    # On Windows.
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
- Установить зависимости
    ```bash
    uv sync
    ```
- Применить миграции к базе данных
    ```bash
    uv run alembic upgrade head
    ```

- Запустить проект локально
    ```bash
    uv run uvicorn app.main:app --reload
    ```
Документацию API после запуска проекта будет досупна по адресу: http://localhost:8000/docs
