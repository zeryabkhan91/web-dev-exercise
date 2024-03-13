from utils.tests import KanbanTestCase


class TicketUpdateViewTestCase(KanbanTestCase):
    def test_get(self):
        # make a post with status and rank fields
        response = self.client.post(
            f'/helpdesk/ticket/{self.t_1.id}/',
            data={
                'status': self.s_doing.id,
                'rank': 1
            },
            follow=False,
        )
        self.assertEqual(
            response.status_code,
            302  # Redirect means success
        )
