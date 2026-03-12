# Mari Feng School Bot 🔮

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Aiogram](https://img.shields.io/badge/aiogram-3.x-orange.svg)
![Status](https://img.shields.io/badge/status-production-green.svg)
![Architecture](https://img.shields.io/badge/architecture-modular-brightgreen.svg)

Профессиональное решение для автоматизации онлайн-школы Mari_Feng. Бот заменяет громоздкие конструкторы, предоставляя пользователям премиальный интерфейс, моментальный отклик и бесшовную интеграцию с платежной системой Stripe.

## 🚀 Key Features

* **Premium UI/UX**: Полное избавление от системных сообщений конструкторов (Cancel/Cancelled и т.д.). Чистый интерфейс на Inline-кнопках.
* **Modular Design**: Бизнес-логика полностью отделена от контента. Все тексты, расписания и ссылки вынесены в независимый модуль для легкого масштабирования.
* **Smart Scheduling**: Интеллектуальная система вывода расписания — общие календари и локальные даты для конкретных образовательных программ.
* **Direct Payments**: Глубокая интеграция со Stripe Checkout через гиперссылки и Callback-кнопки.

## 🛠 Tech Stack

* **Core**: Python 3.10+
* **Framework**: [Aiogram 3.x](https://docs.aiogram.dev/) (Asynchronous OOP)
* **Environment**: [Python-dotenv](https://pypi.org/project/python-dotenv/)
* **Infrastructure**: Ubuntu 24.04 LTS + Systemd (Service protection 24/7)

## 🏗 Project Structure

```text
├── main.py          # Точка входа и конфигурация Dispatcher
├── handlers.py      # Обработка команд и Callback-запросов (Business Logic)
├── keyboards.py     # Фабрика динамических клавиатур
├── texts.py         # Модуль хранения контента и цен (Data Layer)
├── config.py        # Загрузка и валидация переменных окружения
└── marifeng.service # Конфигурация для системного демона Linux
