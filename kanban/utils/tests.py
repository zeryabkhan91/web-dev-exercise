from django.test import TestCase
from board.models import KanbanBoard, Column
from helpdesk.models import Ticket, Status, Engineer, Category, Priority


class KanbanTestCase(TestCase):
    def setUp(self):
        self.p = Priority(name='High', sort_order=1, color='ff0000')
        self.p.save()

        self.c = Category(name='Desktop')
        self.c.save()

        self.s_todo = Status(name='Todo')
        self.s_todo.save()
        self.s_doing = Status(name='Doing')
        self.s_doing.save()
        self.s_done = Status(name='Done')
        self.s_done.save()

        self.e_alice = Engineer(name='Alice')
        self.e_alice.save()

        self.e_bob = Engineer(name='Bob')
        self.e_bob.save()

        self.t_1 = Ticket(
            title='Test 1', status=self.s_todo, category=self.c, priority=self.p,
        )
        self.t_1.save()
        self.t_1.assigned_to.add(self.e_alice)

        self.t_2 = Ticket(
            title='Test 2', status=self.s_doing, category=self.c, priority=self.p,
        )
        self.t_2.save()
        self.t_2.assigned_to.add(self.e_bob)

        self.t_3 = Ticket(
            title='Test 3', status=self.s_done, category=self.c, priority=self.p,
        )
        self.t_3.save()
        self.t_3.assigned_to.add(self.e_bob)
        self.t_3.assigned_to.add(self.e_alice)

        self.t_4 = Ticket(
            title='Test 4', status=self.s_todo, category=self.c, priority=self.p,
        )
        self.t_4.save()
        # t_4 is unassigned

        self.board = KanbanBoard(name='Test Board')
        self.board.save()

        self.column_todo = Column(board=self.board, name='Todo')
        self.column_todo.save()
        self.column_todo.statuses.add(self.s_todo)

        self.column_doing = Column(board=self.board, name='Doing')
        self.column_doing.save()
        self.column_doing.statuses.add(self.s_doing)

        self.column_done = Column(board=self.board, name='Done')
        self.column_done.save()
        self.column_done.statuses.add(self.s_done)
