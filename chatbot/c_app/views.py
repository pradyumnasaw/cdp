from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ChatLog

CDP_DOCS = {
    'segment': 'https://segment.com/docs/',
    'mparticle': 'https://docs.mparticle.com/',
    'lytics': 'https://docs.lytics.com/',
    'zeotap': 'https://docs.zeotap.com/home/en-us/',
}

def chatbot_ui(request):
    return render(request, 'c_app/index.html')

def fetch_documentation_answer(question):
    lower_question = question.lower()

    if 'segment' in lower_question:
        return f"Refer Segment Docs: {CDP_DOCS['segment']}"
    elif 'mparticle' in lower_question:
        return f"Refer mParticle Docs: {CDP_DOCS['mparticle']}"
    elif 'lytics' in lower_question:
        return f"Refer Lytics Docs: {CDP_DOCS['lytics']}"
    elif 'zeotap' in lower_question:
        return f"Refer Zeotap Docs: {CDP_DOCS['zeotap']}"

    return "I can only assist with 'how-to' questions related to Segment, mParticle, Lytics, and Zeotap."

@api_view(['POST'])
def ask_question(request):
    question = request.data.get('question', '')

    answer = fetch_documentation_answer(question)

    ChatLog.objects.create(question=question, answer=answer)

    return Response({'question': question, 'answer': answer})
