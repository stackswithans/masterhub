from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.


class UsersViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_users_view(self):
        timeslot = [[True for i in range(6)] for x in range(12)]
        res = self.client.post(
            reverse("apiv2-masters"),
            data={
                "utype": "MS",
                "first_name": "Sténio",
                "last_name": "Jacinto",
                "email": "random@email.com",
                "password": "awesome",
                "gender": "M",
                "telephone": "922532203",
                "academic_degree": 0,
                "knowledge_areas": [2, 2],
                "occupation": "Estudante",
                "timeslot": timeslot,
            },
            content_type="application/json",
        )
