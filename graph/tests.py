from django.test import TestCase
from django.core.management import call_command


class ViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Load data in test db
        """
        call_command('loaddata', 'db.json', verbosity=0)

    def test_get_list_operation_status_ok(self):
        response = self.client.get('/operations/')
        self.assertEqual(response.status_code, 200)

    def test_post_graph_status_ok(self):
        """
        Testing add graph
        """
        response = self.client.post('/graph/', {"vector": [4, 8, 4, 16]}, format='json')
        self.assertEqual(response.status_code, 200)

    def test_get_graph_status_status_ok(self):
        """
        Testing get graph
        """
        response = self.client.get('/graph/?id=1', format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_graph_status_not_found(self):
        """
        Testing delete graph
        """
        response = self.client.delete('/graph/?id=4', format='json')
        self.assertEqual(response.status_code, 404)
