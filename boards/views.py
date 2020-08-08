from django.shortcuts import render, get_object_or_404
from .models import Board

# Create your views here.

# def home(requets):
#     return HttpResponse('Hello, World')

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})  

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'new_topic.html', {'board': board})
    # for board in boards:
    #     boards_names.append(board.name)

    #     response_html = '<br>'.join(boards_names)

    #     return HttpResponse(response_html)