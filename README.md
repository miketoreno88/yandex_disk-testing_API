# Автоматизированное тестирование веб-приложения
Данны тест выводит в файл file_name_and_folder.txt список всех доступных папок и файлов находящихся в на даске https://disk.yandex.ru.
## О проекте
Проект представляет собой пример организации API теста с использованием языка Python и библиотек pytest и requests.

## Описание тест-кейса:
Предусловие:
●Авторизоваться в сервисе Yandex
Шаги:
●Выполнить запрос на получение всех папок и файлов на диске
●Вывести список доступных папок и файлов
Ожидаемый результат:
●Отображается список доступных папок и файлов
Постусловие:
●Разлогиниться

## Запуск тестов

1. Установка зависимостей:
   ```bash
   pip install -r requirements.txt
2. Запуск тестов:
   ```bash
   pytest

## Как добавить новые тесты
1. Создать новый файл с тестами в директории tests/.
2. Для взаимодействия с элементами страницы использовать Page Object модели.
3. Для входных раличных данных использовать параметризацию тестов с помощью @pytest.mark.parametrize
