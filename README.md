# Fullstack QA API Testing Framework

Это базовый фреймворк для автоматизации API-тестирования с использованием Python и библиотеки `requests`.

## О проекте

Проект включает:

- Абстрактный базовый клиент (`base_client.py`) с универсальным методом для HTTP-запросов
- Клиент (`client.py`) с бизнес-логикой для API Reqres.in
- Конфигурацию (`config.py`) с базовым URL и API ключом
- Логирование запросов и ответов в консоль через `logging`
- Тесты на успешный и неуспешный логин с использованием `pytest`
- Фикстуры для удобного запуска тестов (`conftest.py`)
- Настройки pytest (`pytest.ini`) с включённым логированием в консоль

## Установка

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# или
.venv\Scripts\activate     # Windows

pip install -r requirements.txt
