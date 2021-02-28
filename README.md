# WhatsApp Bot
Бот для рассылки сообщений сотрудникам

## Установка
В папке с проектом:
    pip install virtualenv
    virtualenv env
Запустить env/Scripts/activate.bat
    pip install -r requirements.txt
Открыть файл bot/wabot.py и в конструкторе класса ввести свои ApiUrl и token

```
class WABot():
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['messages']
        self.body = json['messages'][0]['body']
        self.APIUrl = 'https://eu287.chat-api.com/'
        self.token = 'asd'
```
Скачать ngrok https://ngrok.com/download
Запустить и ввести команду ngrok http 80
Перейти в папку с проектом и запустить
python manage.py runserver 80
После этих действий чат-бот в WA будет работать

## Команды чат-бота
1. Регистрация нового сотрудника
```
/registration
+79999999999
Иванов Иван Ивановч
Должность
Отдел
```

2. Отправка сообщений сотруднику

```
/message_user
+79999999999
Сообщение
```

3. Отправка сообщений всем сотрудникам отдела

```
/message_department
Название_отдела
Сообщение
```
