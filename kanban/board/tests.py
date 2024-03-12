from utils.tests import KanbanTestCase


class ColumnTestCase(KanbanTestCase):
    def test_get_tickets(self):
        self.assertEqual(
            list(self.column_todo.get_tickets()),
            [self.t_1, self.t_4],
        )


class DashBoardViewTestCase(KanbanTestCase):
    def test_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.board.name)


class BoardViewTestCase(KanbanTestCase):
    def test_get(self):
        response = self.client.get(f'/board/{self.board.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.board.name)
        self.assertContains(response, self.column_todo.name)
        self.assertContains(response, self.t_1.title)
