import requests
import pytest

# Замените на ваш токен Яндекс.Диска
token = 'y0_AgAAAABwdZ3rAADLWwAAAADry4p3vKzQ-oLsSfKEXOxOVu8Dt0RZiV8'

# URL для запроса к API Яндекс.Диска
base_url = 'https://cloud-api.yandex.net/v1/disk/resources'

# Начальный путь (корневая папка)
initial_path = '/'

# Заголовки для запроса (с токеном)
headers = {
    'Authorization': f'OAuth {token}'
}

# Функция для обхода папок и записи имен файлов и папок в файл
def process_folder(folder_path, file):
    try:
        # Формируем URL для текущей папки
        folder_url = f'{base_url}?path={folder_path}'

        # Выполняем GET-запрос к API Яндекс.Диска для текущей папки
        response = requests.get(folder_url, headers=headers)

        # Проверяем успешность запроса
        response.raise_for_status()

        # Проверяем, что код ответа равен 200
        assert response.status_code == 200

        # Получаем JSON-данные для текущей папки
        data = response.json()

        # Итерируемся по элементам вложенного списка items
        for item in data['_embedded']['items']:
            # Получаем имя элемента
            item_name = item['name']
            # Записываем имя элемента в файл
            file.write(item_name + '\n')

            # Если элемент является папкой, вызываем эту же функцию для обхода внутренних файлов и папок
            if item['type'] == 'dir':
                process_folder(item['path'], file)

    except Exception as e:
        pytest.fail(f'Произошла ошибка: {str(e)}')

def test_yandex_disk_api():
    try:
        # Открываем файл для записи имен
        with open('file_name_and_folder.txt', 'w', encoding='utf-8') as file:
            # Начинаем обход с корневой папки '/'
            process_folder(initial_path, file)

        print('Имена файлов и папок успешно записаны в файл.')
    except Exception as e:
        pytest.fail(str(e))
