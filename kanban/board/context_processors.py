from board import models


def boards(request):
    boards = models.KanbanBoard.objects.all()
    return {'boards': boards}
