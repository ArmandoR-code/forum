from django.http import HttpResponse
from .models import Board
from django.shortcuts import render

def home(request):
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)


#Create your views here.

def home(request):
    """ Atiende la perición GET / """ 
    return render(request, "boards/home.html")
    


