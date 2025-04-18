# Задание: Разработка API для управления складом.

## Как запустить.

- Клонировать репозиторий
    ```bash
    git clone git@github.com:CaDiBob/test_task.git
    ```
- Перейти в папку с проектом
    ```bash
    cd test_task
    ```

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

- Запустить проект локально
    ```bash
    uv run uvicorn app.main:app --reload
    ```
Документацию API после запуска проекта будет досупна по адресу: http://localhost:8000/docs
