### Как запустить проект

1. Создайте файл .env в корне проекта. Используйте файл .env_example как образец. Основные параметры .env файла:
    - DATABASE_URL
    - POSTGRES_USER
    - POSTGRES_PASSWORD
    - POSTGRES_DB

2. Очистите старые контейнеры (опционально). Если вы ранее запускали проект и хотите начать с чистого состояния,
   выполните:
    - docker-compose down -v

3. Запустите проект. Для его запуска, выполните команду
    - docker-compose up

4. После успешного запуска функционал проекта будет доступен по адресу:
   http://localhost:7000/docs - здесь вы найдёте документацию, где можно протестировать все доступные эндпоинты.

