from django.shortcuts import render
from django.http import Http404 , JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core import serializers
from chatterbot import ChatBot
import json
import nltk
import ssl
import requests

chatbot = ChatBot("angelium generic")
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.english')
# Create your views here.
@api_view(['POST'])
def chat_bot(text):
    r = json.loads(text.body)
    input_data=r['text']
    print(input_data)
    response = chatbot.get_response(input_data)
    return HttpResponse (response)