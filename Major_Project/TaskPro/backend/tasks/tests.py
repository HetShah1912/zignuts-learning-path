from datetime import timedelta
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Task

class TaskAPITests(APITestCase):

    def setUp(self):
        # Create two separate users
        self.user1 = User.objects.create_user(
            username="user1",
            password="TestPass123!"
        )
        self.user2 = User.objects.create_user(
            username="user2",
            password="TestPass123!"
        )

        # Authenticate as user1 for most tests
        self.client = APIClient()
        self.client.force_authenticate(user=self.user1)
        self.task_url = "/api/auth/tasks/"
        self.due_date = (
            timezone.localdate() + timedelta(days=2)
        ).isoformat()
        self.task_data = {
            "title": "Learn Django REST Framework",
            "description": "Practise automated testing",
            "priority": "high",
            "due_date": self.due_date,
            "status": "pending",
        }

    def test_create_task(self):
        response = self.client.post(
            self.task_url,
            self.task_data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(
            Task.objects.first().user,
            self.user1
        )

    def test_list_own_tasks(self):
        Task.objects.create(
            user=self.user1,
            **self.task_data
        )

        response = self.client.get(self.task_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_user_cannot_see_other_users_tasks(self):
        Task.objects.create(
            user=self.user2,
            **self.task_data
        )

        response = self.client.get(self.task_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_update_task(self):
        task = Task.objects.create(
            user=self.user1,
            **self.task_data
        )
        response = self.client.patch(
            f"{self.task_url}{task.id}/",
            {"title": "Updated task"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.title, "Updated task")

    def test_delete_task(self):
        task = Task.objects.create(
            user=self.user1,
            **self.task_data
        )

        response = self.client.delete(
            f"{self.task_url}{task.id}/"
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=task.id).exists())

    def test_unauthenticated_request_is_rejected(self):
        self.client.force_authenticate(user=None)

        response = self.client.get(self.task_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_missing_title_is_rejected(self):
        invalid_data = self.task_data.copy()
        invalid_data.pop("title")

        response = self.client.post(
            self.task_url,
            invalid_data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEqual(Task.objects.count(), 0)

    def test_search_by_title(self):
        Task.objects.create(
            user=self.user1,
            **self.task_data
        )

        response = self.client.get(
            self.task_url,
            {"search": "Django"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_by_priority(self):
        Task.objects.create(
            user=self.user1,
            **self.task_data
        )

        response = self.client.get(
            self.task_url,
            {"priority": "high"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
