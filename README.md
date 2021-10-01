# WABot

WhatsApp bot for communication with employees

![alt text](https://img.shields.io/badge/python-3.9.7-black)

### Bot initialization
####Open the bot/wabot.py file and write your ApiUrl and token into the WABot constructor class
```
class WABot():
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['messages']
        self.body = json['messages'][0]['body']
        self.APIUrl = 'https://eu287.chat-api.com/'
        self.token = 'asd'
```

### Run the Bot

#### Install poetry
```shell
pip install poetry
```
 
#### Install the project dependencies
```shell
cd src && poetry install
```

#### Spawn a shell within the virtual environment
```shell
poetry shell
```
####Download ngrok https://ngrok.com/download
####Run and enter the command ngrok http 80
####Go to the file WABot/settings.py
```
cd WABot
```
####Change the MY_NGROK_HOST variable from the current variable to "{Your link ngrok}"
####Go back to the src directory
```
cd ..
```
####Execute the following commands
```
python manage.py migrate
python manage.py runserver 80
```


## Bot commands
1. New employee registration
```
/registration
+79999999999
Иванов Иван Ивановч
Должность
Отдел
```

2. Sending messages to an employee

```
/message_user
+79999999999
Сообщение
```

3. Sending messages to all department employees

```
/message_department
Название_отдела
Сообщение
```
