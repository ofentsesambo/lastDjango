from django.shortcuts import render
from .models import Board

# Create your views here.

# def home(requets):
#     return HttpResponse('Hello, World')

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})
    

    # for board in boards:
    #     boards_names.append(board.name)

    #     response_html = '<br>'.join(boards_names)

    #     return HttpResponse(response_html)