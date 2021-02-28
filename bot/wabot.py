import json
import requests
import datetime
from .models import UserOfBot


class WABot():    
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['messages']
        self.body = json['messages'][0]['body']
        self.APIUrl = 'https://eu287.chat-api.com/'
        self.token = 'asd'
   
    def send_requests(self, method, data):
        url = f"{self.APIUrl}{method}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    def send_message(self, phone, text):
        data = {"phone" : phone,
                "body" : text}  
        answer = self.send_requests('sendMessage', data)
        return answer

    def welcome(self,chatID, noWelcome = False):
        welcome_string = ''
        if (noWelcome == False):
            welcome_string = "Приветствую!\n"
        welcome_string += """Здесь вы можете:
        1. Зарегистрировать нового сотрудника:
        \tФормат:\n\
        \t/registration\n\
        \t+79999999999\n\
        \tИванов Иван Ивановч\n\
        \tДолжность\n\
        \tОтдел
        2. Отправить сообщение сотруднику:
        \tФормат:\n\
        \t/message_user\n\
        \t+79999999999\n\
        \tСообщение
        3. Отправить сообщение отделу:\n
        \tФормат:\n\
        \t/message_department\n\
        \t+79999999999\n\
        \tСообщение"""
        return self.send_message(chatID, welcome_string)
    
    def registration(self, chatID):
        info = self.body.split("\n")
        try:
            UserOfBot.objects.create(
                phone_number=info[1],
                name=info[2],
                position=info[3],
                department=info[4]
            )
            return self.send_message(chatID, "Сотрудник зарегистрирован")
        except IndexError:
            return self.send_message(chatID, f"Ошибка формы сообщения\nПроверьте форму сообщения и попробуйте еще раз")

    def send_message_to_user(self, chatID):
        info = self.body.split("\n")
        try:
            self.send_message(info[1], f"Сообщение от {chatID}:\n{info[2]}")
            return self.send_message(chatID, f"Сотруднику с номером телефона {info[1]} отправлено сообщение")
        except IndexError:
            return self.send_message(chatID, f"Ошибка формы сообщения\nПроверьте форму сообщения и попробуйте еще раз")

    def send_message_to_department(self, chatID):
        info = self.body.split("\n")
        try:
            users = UserOfBot.objects.filter(department=info[1])
            for user in users:
                self.send_message(user.phone_number, f"Сообщение от {chatID}:\n{info[2]}")
            return self.send_message(
                chatID,
                f"Сотрудникам отдела {info[1]} отправлены сообщения"
            ) if users else self.send_message(
                chatID,
                f"Такого отдела не существует"
            )
        except IndexError:
            return self.send_message(chatID, f"Ошибка формы сообщения\nПроверьте форму сообщения и попробуйте еще раз")

    def processing(self):
        if self.dict_messages != []:
            for message in self.dict_messages:
                text = message['body'].split()
                if not message['fromMe']:
                    id  = message['chatId']
                    if text[0].lower() == "/start":
                        return self.welcome(id)
                    elif text[0].lower() == "/registration":
                        return self.registration(id)
                    elif text[0].lower() == "/message_user":
                        return self.send_message_to_user(id)
                    elif text[0].lower() == "/message_department":
                        return self.send_message_to_department(id)
                    else:
                        return self.welcome(id, True)
                else: return 'NoCommand'
