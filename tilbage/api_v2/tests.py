from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.


class UsersViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_student(self):
        res = self.client.post(
            reverse("apiv2-students"),
            data={
                "first_name": "Sténio",
                "last_name": "Jacinto",
                "email": "random1@email.com",
                "password": "awesome",
                "gender": "M",
                "telephone": "922532203",
            },
            content_type="application/json",
        )
        self.assertEqual(res.status_code, 200)
        body = res.json()
        self.assertEqual(body["email"], "random1@email.com")
        self.assertEqual(body["utype"], "ST")
        self.assertIsNotNone(body.get("access_token"))
        self.assertIsNotNone(body.get("refresh_token"))

    def test_create_master(self):
        timeslot = [[True for i in range(6)] for x in range(12)]
        res = self.client.post(
            reverse("apiv2-masters"),
            data={
                "first_name": "Sténio",
                "last_name": "Jacinto",
                "email": "random@email.com",
                "password": "awesome",
                "gender": "M",
                "telephone": "922532203",
                "academic_degree": 0,
                "knowledge_areas": [1, 2],
                "occupation": "Estudante",
                "timeslot": timeslot,
            },
            content_type="application/json",
        )
        self.assertEqual(res.status_code, 200)
        body = res.json()
        self.assertEqual(body["utype"], "MS")
        self.assertEqual(body["email"], "random@email.com")
        self.assertFalse(body["activated"])
