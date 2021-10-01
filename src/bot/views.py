from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .wabot import WABot
import json
from rest_framework.response import Response


class Bot(ViewSet):
    def create(self, request):
        bot = WABot(json.loads(request.body))
        return Response(bot.processing())
