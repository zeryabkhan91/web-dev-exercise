from board import models


def boards(request):
    return {'boards': models.KanbanBoard.objects.all()}
